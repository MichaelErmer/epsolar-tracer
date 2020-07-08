
from pyepsolartracer.client import EPsolarTracerClient
from pyepsolartracer.registers import registers,coils
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

from configparser import ConfigParser
from colorama import init as colorama_init
from colorama import Fore, Back, Style
from time import time, sleep, localtime, strftime
from unidecode import unidecode
import json
import sys
import os.path
import argparse
import paho.mqtt.client as mqtt
import sdnotify


# project data
project_name = 'Tracer MQTT'
project_url = ''

# defaults
default_base_topic = 'tracer'

# Intro
colorama_init()
print(Fore.GREEN + Style.BRIGHT)
print(project_name)
print('Source:', project_url)
print(Style.RESET_ALL)

# Systemd Service Notifications - https://github.com/bb4242/sdnotify
sd_notifier = sdnotify.SystemdNotifier()

# Logging function
def print_line(text, error = False, warning=False, sd_notify=False, console=True):
    timestamp = strftime('%Y-%m-%d %H:%M:%S', localtime())
    if console:
        if error:
            print(Fore.RED + Style.BRIGHT + '[{}] '.format(timestamp) + Style.RESET_ALL + '{}'.format(text) + Style.RESET_ALL, file=sys.stderr)
        elif warning:
            print(Fore.YELLOW + '[{}] '.format(timestamp) + Style.RESET_ALL + '{}'.format(text) + Style.RESET_ALL)
        else:
            print(Fore.GREEN + '[{}] '.format(timestamp) + Style.RESET_ALL + '{}'.format(text) + Style.RESET_ALL)
    timestamp_sd = strftime('%b %d %H:%M:%S', localtime())
    if sd_notify:
        sd_notifier.notify('STATUS={} - {}.'.format(timestamp_sd, unidecode(text)))

# Argparse
parser = argparse.ArgumentParser(description=project_name, epilog='For further details see: ' + project_url)
parser.add_argument('--config_dir', help='set directory where config.ini is located', default=sys.path[0])
parse_args = parser.parse_args()

# Load configuration file
config_dir = parse_args.config_dir

config = ConfigParser(delimiters=('=', ), inline_comment_prefixes=('#'))
config.optionxform = str
try:
    with open(os.path.join(config_dir, 'config.ini')) as config_file:
        config.read_file(config_file)
except IOError:
    print_line('No configuration file "config.ini"', error=True, sd_notify=True)
    sys.exit(1)

sleep_period = config['Daemon'].getint('period', 300)
daemon_enabled = config['Daemon'].getboolean('enabled', True)
base_topic = config['MQTT'].get('base_topic', default_base_topic).lower()

# Eclipse Paho callbacks - http://www.eclipse.org/paho/clients/python/docs/#callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print_line('MQTT connection established', console=True, sd_notify=True)
        print()
    else:
        print_line('Connection error with result code {} - {}'.format(str(rc), mqtt.connack_string(rc)), error=True)
        #kill main thread
        os._exit(1)


def on_publish(client, userdata, mid):
    #print_line('Data successfully published.')
    pass

# MQTT connection
print_line('Connecting to MQTT broker ...')
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_publish = on_publish
mqtt_client.will_set('{}/$announce'.format(base_topic), payload='{}', retain=True)

if config['MQTT'].getboolean('tls', False):
    # According to the docs, setting PROTOCOL_SSLv23 "Selects the highest protocol version
    # that both the client and server support. Despite the name, this option can select
    mqtt_client.tls_set(
        ca_certs=config['MQTT'].get('tls_ca_cert', None),
        keyfile=config['MQTT'].get('tls_keyfile', None),
        certfile=config['MQTT'].get('tls_certfile', None),
        tls_version=ssl.PROTOCOL_SSLv23
    )

mqtt_username = os.environ.get("MQTT_USERNAME", config['MQTT'].get('username'))
mqtt_password = os.environ.get("MQTT_PASSWORD", config['MQTT'].get('password', None))

if mqtt_username:
    mqtt_client.username_pw_set(mqtt_username, mqtt_password)
try:
    mqtt_client.connect(os.environ.get('MQTT_HOSTNAME', config['MQTT'].get('hostname', 'localhost')),
                        port=int(os.environ.get('MQTT_PORT', config['MQTT'].get('port', '1883'))),
                        keepalive=config['MQTT'].getint('keepalive', 60))
except:
    print_line('MQTT connection error. Please check your settings in the configuration file "config.ini"', error=True, sd_notify=True)
    sys.exit(1)
else:
    mqtt_client.loop_start()
    sleep(1.0) # some slack to establish the connection

# choose the serial client
serialclient = ModbusClient(method='rtu', port='/dev/ttyXRUSB0', baudrate=115200, stopbits = 1, bytesize = 8, timeout=1)
#serialclient = None


# choose the serial client
client = EPsolarTracerClient(serialclient = serialclient)
client.connect()

response = client.read_device_info()
announce = dict()
announce['Manufacturer'] = str(response.information[0])
announce['Model'] = str(response.information[1])
announce['Version'] = str(response.information[2])
mqtt_client.publish('{}/$announce'.format(base_topic), json.dumps(announce), retain=True)
print_line("Manufacturer:" + repr(response.information[0]))
print_line("Model:" + repr(response.information[1]))
print_line("Version:" + repr(response.information[2]))

sd_notifier.notify('READY=1')

while True:
    for reg in registers:
        #print
        #print reg
        value = client.read_input(reg.name)
        #print_line(value)
        mqtt_client.publish('{}/registers/{}/unitShort'.format(base_topic, reg.name), reg.unit()[1], 1, True)
        mqtt_client.publish('{}/registers/{}/unitLong'.format(base_topic, reg.name), reg.unit()[0], 1, True)
        mqtt_client.publish('{}/registers/{}/value'.format(base_topic, reg.name), float(value), 1, True)

        #if value.value is not None:
        #    print client.write_output(reg.name,value.value)

    for reg in coils:
        #print
        #print reg
        value = client.read_input(reg.name)
        #print_line(value)
        mqtt_client.publish('{}/coils/{}/unitShort'.format(base_topic, reg.name), reg.unit()[1], 1, True)
        mqtt_client.publish('{}/coils/{}/unitLong'.format(base_topic, reg.name), reg.unit()[0], 1, True)
        mqtt_client.publish('{}/coils/{}/value'.format(base_topic, reg.name), float(value), 1, True)
        #print client.write_output(reg.name,value.value)

    print_line('All metrics published', console=False, sd_notify=True)

    if daemon_enabled:
        print_line('Sleeping ({} seconds) ...'.format(sleep_period))
        sleep(sleep_period)
        print()
    else:
        print_line('Execution finished in non-daemon-mode', sd_notify=True)
        mqtt_client.disconnect()
        break

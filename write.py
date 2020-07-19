
from pyepsolartracer.client import EPsolarTracerClient
from pyepsolartracer.registers import registers,coils
#from test.testdata import ModbusMockClient as ModbusClient
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

import sys

# configure the client logging
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

# choose the serial client
serialclient = ModbusClient(method='rtu', port='/dev/ttyXRUSB0', baudrate=115200, stopbits = 1, bytesize = 8, timeout=1)
#serialclient = None


# choose the serial client
client = EPsolarTracerClient(serialclient = serialclient)
client.connect()

client.write_output("Battery Capacity", 408); # 400 if parellelized
client.write_output("Battery Type", 0x0000); # = custom
client.close()

client.connect()
#client.write_output("High Volt.disconnect", 15.0)
client.write_output("Charging limit voltage", 14.6)
client.write_output("Over voltage reconnect", 14.8)
client.write_output("Equalization voltage", 14.6) # not required with agm
client.write_output("Boost voltage", 13.8)
client.write_output("Float voltage", 13.4)

client.write_output("Boost reconnect voltage", 13.2)
client.write_output("Low voltage reconnect", 12.2)
client.close()


from pyepsolartracer.client import EPsolarTracerClient
from pyepsolartracer.registers import registers,coils
#from test.testdata import ModbusMockClient as ModbusClient
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

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

response = client.read_device_info()
print "Manufacturer:", repr(response.information[0])
print "Model:", repr(response.information[1])
print "Version:", repr(response.information[2])

client.write_output(sys.argv[1], sys.argv[2]);

client.close()
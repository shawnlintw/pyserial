import sys
import serial
import serial.tools.list_ports
from time import sleep
import time

target_VCP_vidpid='0403:6015'


ports = list(serial.tools.list_ports.comports())
for p in ports:
	if (p.hwid.find(target_VCP_vidpid)!=-1):
		print p.device
		SLS_COMPORT=p.device
		
serial=serial.Serial(SLS_COMPORT, 115200, timeout=0)

while 1:

	try:
		message=serial.readline()
		sleep(0.05)
		if message != '':
			sys.stdout.write(message)
			sys.stdout.flush()
		if (message.find('Ready')!=-1):
			serial.write("")

	except	serial.SerialTimeoutException:
		print ('Data could not be read')

		
		
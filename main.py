import spidev
import time

spi = spidev.SpiDec()
spi.open(0, 0) #bus 0, dev 0
spi.max_speed_hz = 400000

def read_esp():
	response = spi.xfer2([0x00]) #to receive data
	return response[0]

while True:
	data = read_data()
	print("received:",data)
	time.sleep(1)

import serial
import time

ser = serial.Serial(
	"/dev/serial0",
	115200,
	timeout=1)

ser.write(b"GET\n")
time.sleep(0.1)
data = ser.read_all()
print(data.decode('utf-8', errors='replace'))

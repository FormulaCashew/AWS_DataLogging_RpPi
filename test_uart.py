import serial
import time
import serial

SERIAL_PORT = "/dev/serial0"
BAUD_RATE = 115200

def init_uart():
	try:
		ser = serial.Serial(SERIAL_PORT,BAUD_RATE,timeout=1)
		print("initialized")
		return ser
	except Exception:
		print(f"Error: {Exception}")

def send_command(ser):
	try:
		command = "GET\n"
		ser.write(command.encode('utf-8'))
		print(f"Sent command")
	except Exception as e:
		print(f" Failed to read response: {e}")

def read_uart(ser):
	try:
		response = ser.readline().decode('utf-8').strip()
		print(f"Received: {response}")
		return response
	except Exception as e:
		print(f"Failed to read response: {e}")
		return ""

if __name__ == "__main__":
	ser = init_uart()
	if not ser:
		print(f"Exiting")
		exit (1)
	try:
		while True:
			send_command(ser)
			time.sleep(0.2)
			temp = read_uart(ser)
	except Exception as e:
		print(f"error: {e}")
	finally:
		ser.close()

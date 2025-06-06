import serial
import time
import requests
import datetime
import os

URL = "API_URL"

UART_PORT="/dev/ttyS0"
BAUD_RATE=115200 #This is actually smtg on the lines of 71455 bps

LOG_FILE = "data.txt"

def log_temperature(temperatura: str):
	timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
	with open(LOG_FILE, "a") as f:
        	f.write(f"{timestamp},{temperatura}\n")
	print(f"Data stored")

def read_command():
	try:
		with serial.Serial(UART_PORT,BAUD_RATE,timeout=2) as ser:
			command="GET\n"
			ser.write(command.encode('utf-8'))
			print(f"Command Sent")
			temperatura = ser.readline().decode().strip()
			print(f"Received {temperatura}")
			return temperatura
	except Exception as e:
		print(f"Error UART:", e)
		return None

def send_aws(temperatura: str):
	payload = {"temperatura": temperatura}
	headers = {"Content-Type": "application/json"}
	try:
		response = requests.post(URL, json=payload, headers=headers)
		print(f"Status; {response.status_code}")
		print(f"Response: {response.text}")
		if response.status_code == 200:
			print(f"Enviado a AWS: {temperatura} C")
	except Exception as e:
		print(f"Error al enviar a AWS: {e}")
		traceback.print_exec()

if __name__ == "__main__":
	print("iniciando monitoreo")
	try:
		if os.path.exists(LOG_FILE):
			if os.stat(LOG_FILE).st_size == 0:
				open(LOG_FILE, "a").write(f"date,temperature\n")
		else:
			open(LOG_FILE, "a").write(f"date,temperature\n")
		while True:
			temp = read_command()
			if temp:
				log_temperature(temp)
				send_aws(temp)
			time.sleep(1)
	except KeyboardInterrupt:
		print("\nInterrupted by user")

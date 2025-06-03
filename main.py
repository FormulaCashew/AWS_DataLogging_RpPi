import serial
import time
import requests

URL = "API-URL"

UART_PORT="/dev/ttyS0"
BAUD_RATE=115200 #This is actually smtg on the lines of 71455 bps

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
		while True:
			temp = read_command()
			if temp:
				send_aws(temp)
			time.sleep(1)
	except KeyboardInterrupt:
		print("\nInterrupted by user")

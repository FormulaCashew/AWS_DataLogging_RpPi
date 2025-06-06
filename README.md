# SPI to AWS Data Transfer

This project involves reading data from an UART device connected to a Raspberry Pi 3B and sending the received data to AWS via an API.
The goal is to establish a seamless data pipeline from a local device (via SPI) to the cloud (via AWS).


## Prerrequisites

Before starting, make sure you have the following:

- **Raspberry Pi 3B** with Raspian OS installed
- A sensor or device connected to the Pi via **UART**
- **Python 3** installed on the Raspberry Pi
- **AWS Account** with acces to API Gateway, IoT Core, or any other service you want to send data to
- Internet connection for the Raspberry Pi



## Installation on Raspberry Pi

## 1. Set Up the Raspberry Pi

### Enable SPI on the Raspberry Pi

use the commands:

```bash
sudo raspi-config // Enable SPI in Interface Options > Serial Interface > Enable
sudo reboot
```

## 2. Create a virtual environment

```
sudo apt update

sudo apt install python3-venv python3-pip -y

mkdir ~/esp_temp_monitor
cd ~/esp_temp_monitor

python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requierements.txt
```

## 3. Configure AWS

### Using  API Gateway + Lambda (HTTP REST)

Create an API Gateway REST
Connect with a Lambda function
Change main.py as required
Lambda can store data in DynamoDB or S3

### Using AWS IoT Core (MQTT)

Create a "Thing" in AWS IoT Core
Download certificates:
- certificate.pem.crt
- private.key
- AmazonRootCA1.pem
Configure the endpoint and credentials in main.py

## 4. Execute the script
```bash
sudo python3 main.py
```

## 5. (Optional) Check data

Using the data stored one may check the acquired data and use it as desired

Originally intended to use with:
https://github.com/FormulaCashew/RaspberryPi-Flask-graph

# SPI to AWS Data Transfer

This project involves reading data from an SPI device connected to a Raspberry Pi 3B and sending the received data to AWS via an API.
The goal is to establish a seamless data pipeline from a local device (via SPI) to the cloud (via AWS).

## Prerrequisites

Before starting, make sure you have the following:

- **Raspberry Pi 3B** with Raspian OS installed
- A sensor or device connected to the Pi via **SPI**
- **Python 3** installed on the Raspberry Pi
- **AWS Account** with acces to API Gateway, IoT Core, or any other service you want to send data to
- Internet connection for the Raspberry Pi

## Installation

## 1. Set Up the Raspberry Pi

### Enable SPI on the Raspberry Pi

use the commands:

sudo raspi-config // Enable SPI in Interface Options > SPI > Enable
sudo reboot

## 2. Create a virtual environment

## 3. Configure AWS

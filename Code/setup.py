import os
import sys
import time
flag=0x00
for x in range(1,4):
	if os.system("sudo apt-get update") == 0:
		flag=flag | 0x01
		break
for x in range(1,4):
	if os.system("sudo apt-get install -y i2c-tools") == 0:
		flag=flag | 0x02
		break
for x in range(1,4):
	if os.system("sudo apt-get install -y python3-smbus") == 0:
		flag=flag | 0x04
		break
for x in range(1,4):
	if os.system("sudo pip3 install adafruit-pca9685") == 0:
		flag=flag | 0x08
		break
for x in range(1,4):
	if os.system("sudo pip3 install rpi_ws281x") == 0:
		flag=flag | 0x10
		break
for x in range(1,4):
	if os.system("sudo pip3 install mpu6050-raspberrypi") == 0:
		flag=flag | 0x20
		break
for x in range(1,4):
	if os.system("sudo apt-get install -y libqtgui4 python3-dev libqt4-test python3-pyqt5 ") == 0:
		flag=flag | 0x40
		break
for x in range(1,4):
	if os.system("sudo apt-get install -y libopencv-dev python3-opencv") == 0:
		flag=flag | 0x80
		break

if flag==0xFF:
        print("\nNow the installation is successful.")
        print("\nPlease restart raspberry pi")
else:
	print ("\nSome libraries have not been installed yet. Please run 'sudo python setup.py' again")
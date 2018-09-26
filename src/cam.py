## Copyright 2018 (c) Alex Ellis
## MIT License

import signal
import sys
from picamera import PiCamera

import RPi.GPIO as GPIO
import time
from datetime import datetime
import threading
import unicornhat as uh

camera = None
pin = 23
off_pin = 16
tilt_pin = 11

def init():
	global pin
	global off_pin

	GPIO.setmode(GPIO.BCM)

	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(off_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(tilt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	GPIO.add_event_detect(pin, GPIO.FALLING, bouncetime=1500)
	GPIO.add_event_callback(pin, press)

	GPIO.add_event_detect(off_pin, GPIO.FALLING, bouncetime=1500)
	GPIO.add_event_callback(off_pin, off_press)

taking = False

def off_press(val):
	print("We want to turn the camera off")

	global status
	status.clear()

	import subprocess
	cmdCommand = "shutdown -h now"
	process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)

def press(val):
	print("Button pressed")
	global shutter
	global tilt_pin
	tilt_val = GPIO.input(tilt_pin)
	print("Tilt", tilt_val)
	shutter.take(tilt_val)

def close():
	global status
	status.clear()

def loop():
	while True:
		try:
			time.sleep(0.01)
		except KeyboardInterrupt:
			print("Closing")
			break
	close()
	sys.exit(1)

class Shutter(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.taking = False
		self.shots = 0

	def run(self):
		while(True):
			if self.shots > 0:
				self.shots = 0
				self.takeNow()
			time.sleep(0.01)

	def set_camera(self, cam):
		self.camera = cam

	def take(self, tilt):
		self.tilt = tilt
		self.shots = self.shots + 1

	def set_status(self, status):
		self.status = status

	def takeNow(self):
		if self.taking == True:
			print("Still taking a shot")
			return

		self.status.taking()

		self.camera.resolution = (3280, 2464)
		self.camera.start_preview()
		self.camera.hflip = True
		self.camera.vflip = True

		if self.tilt == 1:
			self.camera.exif_tags["IFD0.Orientation"] = "6"
		else:
			self.camera.exif_tags["IFD0.Orientation"] = "1"

		# self.camera.rotation = rotation

		preview = 1

		time.sleep(preview)

		file = "{:%Y-%m-%d-%H_%M_%S}.jpg".format(datetime.now())
		self.camera.capture(file)
		print("Took " + file)

		self.status.available()

		self.taking = False
class Status:
	def __init__(self):
		uh.set_all(0,0,0)
		uh.brightness(0.75)	# Dim down slightly
		uh.show()
		self.available()

	def available(self):
		uh.set_all(0, 255, 0)
		uh.show()
	def taking(self):
		uh.set_all(255, 0, 0)
		uh.show()
	def clear(self):
		uh.set_all(0, 0, 0)
		uh.show()

camera = PiCamera()
status = Status()
shutter = Shutter()
shutter.set_camera(camera)
shutter.set_status(status)
shutter.start()

init()
loop()

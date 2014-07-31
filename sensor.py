#!/usr/bin/python2

import importlib
import os
import time
import requests
import threading

from etc import init

print ""
config = init.test_config()
init.pesan("SUKSES", "Menjalankan aplikasi...")

def loop(intv, method):
	threading.Timer(intv, loop, [intv, method]).start()
	method()

def sensor():
	for file in os.listdir("modules/"):
		if file.endswith(".py") and not file.startswith("__init__"):
			plugin = importlib.import_module("modules." + file[:-3])
			plugin.migrate(config)

# Jalankan sensor
loop(3, sensor)
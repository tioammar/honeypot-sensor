import json
import MySQLdb
import os.path
import requests
import sys

def pesan(val, teks):
	if val == "TIPS":
		print "\033[93m[TIPS]\033[0m " + teks
	
	if val == "SUKSES":
		print "\033[92m[SUKSES]\033[0m " + teks
	
	if val == "GAGAL":
		print "\033[91m[GAGAL]\033[0m " + teks
		
	if val == "PESAN":
		print "\033[94m[PESAN]\033[0m " + teks

def test_config():
	pesan("PESAN", "Membuka konfigurasi")
	try:
		config_file = open('configuration')
	except IOError:
		pesan("GAGAL", "Konfigurasi tidak ditemukan!")
		sys.exit(0)

	pesan("PESAN", "Memeriksa konfigurasi")
	try:
		config = json.load(config_file)
		config_file.close()
	except ValueError:
		pesan("GAGAL", "Konfigurasi rusak")
		sys.exit(0)

	pesan("PESAN", "URL: "+config['url'])

	try:
		r = requests.get(config['url'] + "token")
		tok = r.json()
		config['token'] = tok['token']
		pesan("PESAN", "TOKEN: "+config['token'])
	except TypeError:
		pesan("GAGAL", "URL Salah!")
		sys.exit(0)

	return config
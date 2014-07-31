import json
import requests

from etc import main

def migrate(config):

	# Mengambil data dari kippo - auth

	result = main.select(config['honeypot']['kippo'], 'SELECT id, session, success, hex(username), hex(password), timestamp FROM auth', 'mysql')
	jeson = json.dumps(result, separators=(',',':'))
	send = main.transfer('kippo_auth', jeson, config['url'])

	if send:
		main.delete(config['honeypot']['kippo'], 'DELETE FROM auth', 'mysql')

	# Mengambil data dari kippo - client

	result = main.select(config['honeypot']['kippo'], 'SELECT * FROM clients', 'mysql')
	jeson = json.dumps(result, separators=(',',':'))
	send = main.transfer('kippo_clients', jeson, config['url'])

	if send:
		main.delete(config['honeypot']['kippo'], 'DELETE FROM clients', 'mysql')

	# Mengambil data dari kippo - downloads

	result = main.select(config['honeypot']['kippo'], 'SELECT * FROM downloads', 'mysql')
	jeson = json.dumps(result, separators=(',',':'))
	send = main.transfer('kippo_downloads', jeson, config['url'])

	if send:
		main.delete(config['honeypot'],['kippo'], 'DELETE FROM downloads', 'mysql')

	# Mengambil data dari kippo - input

	result = main.select(config['honeypot']['kippo'], 'SELECT * FROM input', 'mysql')
	jeson = json.dumps(result, separators=(',',':'))
	send = main.transfer('kippo_input', jeson, config['url'])

	if send:
		main.delete(config['honeypot']['kippo'], 'DELETE FROM input', 'mysql')

	# Mengambil data dari kippo - sessions

	result = main.select(config['honeypot']['kippo'], 'SELECT * FROM sessions', 'mysql')
	jeson = json.dumps(result, separators=(',',':'))
	send = main.transfer('kippo_sessions', jeson, config['url'])

	if send:
		main.delete(config['honeypot']['kippo'], 'DELETE FROM sessions')

	# Mengambil data dari kippo - ttylog

	result = main.select(config['honeypot']['kippo'], 'SELECT id, session, hex(ttylog) FROM ttylog', 'mysql')
	jeson = json.dumps(result, separators=(',',':'))
	send = main.transfer('kippo_ttylog', jeson, config['url'])

	if send:
		main.delete(config['honeypot']['kippo'], 'DELETE FROM ttylog')
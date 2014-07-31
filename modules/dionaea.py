import json
import requests

from etc import main

def migrate(config):

	# Mengambil data dari dionaea - connections

	result = main.select(config['honeypot']['dionaea'], 'SELECT * FROM connections', 'sqlite')
	jeson = json.dumps(result, separators=(',',':'))
	send = main.transfer('dionaea_connections', jeson, config['url'])

	if send:
		main.delete(config['honeypot']['dionaea'], 'DELETE FROM connections')

	# Mengambil data dari dionaea - downloads

	result = main.select(config['honeypot']['dionaea'], 'SELECT * FROM downloads', 'sqlite')
	jeson = json.dumps(result, separators=(',',':'))
	send = main.transfer('dionaea_downloads', jeson, config['url'])

	if send:
		main.delete(config['honeypot']['dionaea'], 'DELETE FROM downloads')
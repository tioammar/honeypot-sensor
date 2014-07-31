import json
import requests

from etc import main
from etc import handler

def migrate(config):

	# Mengambil data p0f - log

	result = handler.readlog(config['honeypot']['p0f'])
	jeson = json.dumps(result, separators=(',',':'))
	send = main.transfer('p0f_fingerprint', jeson, config['url'])
import os
import re
import string

def readlog(config):
	logfile = open(config['path'])
	log = logfile.readlines()
	logfile.close()
	lines = []
	data = []

	for line in log:
		lines.append(line)
	for strip in lines:
		m = re.search('(?<=cli=)[a-zA-Z0-9_ .:]+', strip)
		n = re.search('(?<=os=)[a-zA-Z0-9_ .:]+', strip)
		ip = m.group(0)
		if n:
			os = n.group(0)
		else:
			os = "null"
		datax = "_".join([ip, os])
		data1 = datax.split("_", 2)
		data.append(data1)

	return data
import base64
import datetime
import MySQLdb
import requests
import sqlite3 as lite

from MySQLdb import converters

def select(config, query, dbms):
	if dbms.lower() == 'mysql':
		dbcon = MySQLdb.connect(config['host'],config['user'],config['pass'],config['name'])
		cursor = dbcon.cursor()
	elif dbms.lower() == 'sqlite':
		dbcon = lite.connect(config['path'])
		cursor = dbcon.cursor()

	try:
		cursor.execute(query)
		results = cursor.fetchall()

		data = []

		for result in results:
			data0 = []
			lenght = len(result)
			index  = 0

			while index < lenght:
				if(type(result[index]) is datetime.datetime):
					data0.append(result[index].strftime( '%Y-%m-%d %H:%M:%S' ))
				else:
					data0.append(result[index])

				index = index + 1
			data.append(data0)
	except Exception as e:
		print e

	dbcon.close()
	return data


def delete(config, query):
	dbcon = MySQLdb.connect(config['host'],config['user'],config['pass'],config['name'])
	cursor = dbcon.cursor()

	try:
		cursor.execute(query)
		dbcon.commit()
	except Exception as e:
		dbcon.rollback()

	dbcon.close()

def transfer(medium, json, url):
	data = {"medium": medium, "data":base64.b64encode(json)}
	r = requests.post(url + 'index.php', data=data)
	print medium
	print r.text

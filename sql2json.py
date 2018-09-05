#!/usr/bin/python

import json as simplejson
import sqlite3
from sqlite3 import Error

connection = sqlite3.connect('characters.db')
cursor = connection.cursor()

query = "Select * from characters"
results = cursor.execute(query)

JSON = []
 
for row in results:
    JSON.append({'id': row[0],'fname': row[1],'lmame': row[2],'phone': row[3]})

connection.close()

print simplejson.dumps(JSON)
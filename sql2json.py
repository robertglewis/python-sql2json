#!/usr/bin/python3

import json as simplejson
import sqlite3
from sqlite3 import Error

connection = sqlite3.connect('characters.db')
cursor = connection.cursor()

query = "Select * from characters"
results = cursor.execute(query)

names = list(map(lambda x: x[0], cursor.description))

JSON = []
for row in results:
    r = {}
    for i in range(len(names)):
        r[names[i]] = row[i]
    JSON.append(r)

connection.close()

print(simplejson.dumps(JSON))

#!/usr/bin/python

import sys
from sys import argv
import psycopg2

conn = psycopg2.connect("dbname=sensor user=pi host=localhost")
cur = conn.cursor()
cur.execute("select createdon, name, value from reading WHERE createdon >NOW() - interval '1 days'")

body = '''{{
  "x": [ {} ],
  "{}": [ {} ]
}}'''

# Iterate through the result of curA
x = ""
k = ""
v = ""
for arr in cur.fetchall():
  if (len(x) > 0):
    x = x + ","
    v = v + "," 
  else:
    k = str(arr[1])
  x = x + "\"" + arr[0].strftime("%Y-%m-%d %H:%M:%S") + "\""
  v = v + str(arr[2])

print(body.format(x, k, v)) 

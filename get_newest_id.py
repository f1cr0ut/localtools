#!/usr/bin/python3.5
import sqlite3
import os
import sys

encode_mode = 'utf8'

def Println(s):
	sys.stdout.buffer.write((s+'\n').encode(encode_mode))

def MainDisp(db_name, table_name):
	if not os.path.exists(db_name):
		print("db not found")
		return
	conn = sqlite3.connect(db_name)
	conn.cursor()
	sql = u"select ROWID from " + table_name + " order by id desc limit 1;"
	for row in conn.execute(sql):
		Println(str(row[0]))
	conn.close()

if __name__ == '__main__':
	if len(sys.argv) <= 2:
		print("need db name on argv[1]")
		print("need table name on argv[2]")
		print("\noptions:\n-sjis: print as shift-jis characters. default is utf8")
		sys.exit(1)
	show_detail = True
	db_name = sys.argv[1]
	table_name = sys.argv[2]
	count = 0
	for arg in sys.argv:
		if count < 2:
			count += 1
			continue
		if arg == "-sjis":
			encode_mode = 'sjis'
	MainDisp(db_name, table_name)

#!/usr/bin/python3.5
import sqlite3
import os
import sys

encode_mode = 'utf8'

def MainDisp(db_name, Id, show_detail):
	if not os.path.exists(db_name):
		print("db not found")
		return
	conn = sqlite3.connect(db_name)
	sql = u"update schedule set finished=1, deleted=1 where id=" + str(Id) + ";"
	conn.execute(sql)
	conn.commit()
	conn.close()

if __name__ == '__main__':
	if len(sys.argv) <= 1:
		print("need id to delete")
		sys.exit(1)
	show_detail = True
#	db_name = sys.argv[1]
	db_name = "DB/todo.db"
#	title_str = sys.argv[2]
	Id = sys.argv[1]
	for arg in sys.argv:
		if arg == "-s":
			show_detail = False
		if arg == "-sjis":
			encode_mode = 'sjis'
	MainDisp(db_name, Id, show_detail)

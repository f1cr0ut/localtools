#!/usr/bin/python3.5
import sqlite3
import os
import sys

encode_mode = 'utf8'

def Println(s):
	sys.stdout.buffer.write((s+'\n').encode(encode_mode))

def MainDisp(db_name, show_detail):
	if not os.path.exists(db_name):
		print("db not found")
		return
	conn = sqlite3.connect(db_name)
	conn.cursor()
	sql = u"select id, created, title, body from diary where deleted=0 order by created desc;"
	bodynum = 3
	for row in conn.execute(sql):
		print_str = "| "
		count = 0
		for c in row:
			if count == bodynum:
				count += 1
				continue
			print_str += str(c).replace('\n','') + " | "
			count += 1
		print_str = print_str.rstrip(" | ")
		# print title line
		Println(print_str)
		# print ticket status
		if show_detail == True:
			# print details
			if row[bodynum] != None and row[bodynum] != "":
				detail = row[bodynum].replace('\r\n', '\n')
				detail = detail.replace('\r', '\n')
				Println('\t' + detail.replace('\n', '\n\t'))
			Println("")
	conn.close()

if __name__ == '__main__':
#	if len(sys.argv) <= 1:
#		print("need db name")
#		sys.exit(1)
	show_detail = True
#	db_name = sys.argv[1]
	db_name = "DB/diary.db"
	for arg in sys.argv:
		if arg == "-s":
			show_detail = False
		if arg == "-sjis":
			encode_mode = 'sjis'
	MainDisp(db_name, show_detail)

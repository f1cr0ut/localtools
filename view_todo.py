#!/usr/bin/python3.5
import sqlite3
import os
import sys

encode_mode = 'utf8'

def Println(s):
	sys.stdout.buffer.write((s+'\n').encode(encode_mode))

def PrintSub(conn, sql):
	re = conn.execute(sql)
	count = 0
	ss = "";
	for r in re:
		if r[0] != "":
			detail = r[0].replace('\r\n', '\n')
			detail = detail.replace('\r', '\n')
			detail = detail.replace('\n', '\n\t')
			ss += "\t内容:\n\t" + str(detail) + "\n"
		if r[1] != "":
			ss += "\t開始日:" + str(r[1]) + "\n"
		if r[2] != "":
			ss += "\t終了日:" + str(r[2]) + "\n"
		if r[3] != "":
			ss += "\t場所:" + str(r[3]) + "\n"
		if r[4] != "":
			ss += "\t予算:" + str(int(r[4]))
		if r[5] != "":
			ss += str(r[5])+ "\n\t"
		count += 1
	if count >= 1:
		Println(ss)

def MainDisp(db_name, show_detail):
	if not os.path.exists(db_name):
		print("db not found")
		return
	conn = sqlite3.connect(db_name)
	conn.cursor()
	sql = u"select id, created, title, body, deadline from schedule where deleted=0 order by deadline asc;"
	bodynum = 3
	deadlinenum = 4
	for row in conn.execute(sql):
		print_str = "| "
		count = 0
		for c in row:
			if count == deadlinenum or count == bodynum:
				continue
			print_str += str(c).replace('\n','') + " | "
			count += 1
		print_str = print_str.rstrip(" | ")
		# print title line
		Println(print_str)
		# print ticket status
		if show_detail == True:
			if row[deadlinenum] != None and row[deadlinenum] != "":
				Println('	期限:' + row[deadlinenum])
			PrintSub(conn, u"select description, start_day, end_day, place, price, price_unit from additional_info where parent_id="+str(row[0])+";")
			# print details
			if row[bodynum] != None and row[bodynum] != "":
				Println("詳細:")
				detail = row[bodynum].replace('\r\n', '\n')
				detail = detail.replace('\r', '\n')
				Println('\t' + detail.replace('\n', '\n\t'))
	conn.close()

if __name__ == '__main__':
#	if len(sys.argv) <= 1:
#		print("need db name")
#		sys.exit(1)
	show_detail = True
#	db_name = sys.argv[1]
	db_name = "DB/todo.db"
	for arg in sys.argv:
		if arg == "-s":
			show_detail = False
		if arg == "-sjis":
			encode_mode = 'sjis'
	MainDisp(db_name, show_detail)

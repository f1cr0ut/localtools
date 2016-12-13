#!/usr/bin/python3.5
import sqlite3
import os
import sys

encode_mode = 'utf8'

def Println(s):
	sys.stdout.buffer.write((s+'\n').encode(encode_mode))

def PrintSub(conn, sql, disp, sharp):
	re = conn.execute(sql)
	ss = disp
	count = 0
	for r in re:
		ss += ("#" if sharp == True else "") + str(r[0]) + ", "
		count += 1
	if count > 0:
		ss = ss.rstrip(", ")
		Println(ss)

def MainDisp(db_name, show_detail):
	if not os.path.exists(db_name):
		print("db not found")
		return
	conn = sqlite3.connect(db_name)
	conn.cursor()
	sql = u"select id, priority, title, body, progress, deadline, category from ticket where deleted=0 order by priority desc;"
	bodynum = 3
	prioritynum = 1
	progressnum = 4
	deadlinenum = 5
	categorynum = 6
	for row in conn.execute(sql):
		print_str = "| "
		count = 0
		for c in row:
			if count == progressnum or count == deadlinenum or count == categorynum or count == bodynum:
				continue
			if count == prioritynum:
				print_str += "pri:" + str(c).replace('\n','') + " | "
			else:
				print_str += str(c).replace('\n','') + " | "
			count += 1
		print_str = print_str.rstrip(" | ")
		# print title line
		Println(print_str)
		# print ticket status
		if show_detail == True:
			Println('	カテゴリ:' + str(row[categorynum]))
			Println('	進捗:' + str(float(row[progressnum]) * 100) + "%")
			if row[deadlinenum] != None:
				Println('	期限:' + row[deadlinenum])
			PrintSub(conn, u"select related_ticket_id from related_ticket_id where deleted=0 and parent_ticket_id="+str(row[0])+";", "	子チケット:", True)
			PrintSub(conn, u"select parent_ticket_id from related_ticket_id where deleted=0 and related_ticket_id="+str(row[0])+";", "	親チケット:", True)
			PrintSub(conn, u"select text from ticket_tags where deleted=0 and parent_ticket_id="+str(row[0])+";", "	関連タグ:", False)
			PrintSub(conn, u"select worker from ticket_authors where deleted=0 and parent_ticket_id="+str(row[0])+";", "	担当者:", False)
			# print details
			if row[bodynum] != "" and row[bodynum] != None:
				Println("詳細:")
				detail = row[bodynum].replace('\r\n', '\n')
				detail = detail.replace('\r', '\n')
				Println('\t' + detail.replace('\n', '\n\t'))
			Println('')
	conn.close()

if __name__ == '__main__':
#	if len(sys.argv) <= 1:
#		print("need db name")
#		sys.exit(1)
	show_detail = True
#	db_name = sys.argv[1]
	db_name = "dat.sqlite3"
	for arg in sys.argv:
		if arg == "-s":
			show_detail = False
		if arg == "-sjis":
			encode_mode = 'sjis'
	MainDisp(db_name, show_detail)

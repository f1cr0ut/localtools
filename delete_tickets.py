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

def MainDisp(db_name, Id, show_detail):
	if not os.path.exists(db_name):
		print("db not found")
		return
	conn = sqlite3.connect(db_name)
	sql = u"insert into ticket_last_update_stamp(parent_id, description) values(" + str(Id) + ", 'deleted from command');"
	conn.execute(sql)
	conn.commit()
	try:
		sql = u"update related_ticket_id set deleted=1 where parent_ticket_id=" + str(Id) + ";"
		conn.execute(sql)
		conn.commit()
	except:
		pass
	try:
		sql = u"update ticket set finished=1, deleted=1 where id=" + str(Id) + ";"
		conn.execute(sql)
		conn.commit()
	except:
		pass
	try:
		sql = u"update ticket_tags set finished=1, deleted=1 where parent_ticket_id=" + str(Id) + ";"
		conn.execute(sql)
		conn.commit()
	except:
		pass
	try:
		sql = u"update ticket_authors set deleted=1 where parent_ticket_id=" + str(Id) + ";"
		conn.execute(sql)
		conn.commit()
	except:
		pass
	try:
		sql = u"update related_revision set deleted=1 where parent_id=" + str(Id) + ";"
		conn.execute(sql)
		conn.commit()
	except:
		pass
	conn.close()

if __name__ == '__main__':
#	if len(sys.argv) <= 1:
#		print("need db name")
#		sys.exit(1)
	show_detail = True
#	db_name = sys.argv[1]
	db_name = "dat.sqlite3"
	Id = sys.argv[1]
	for arg in sys.argv:
		if arg == "-s":
			show_detail = False
		if arg == "-sjis":
			encode_mode = 'sjis'
	MainDisp(db_name, Id, show_detail)

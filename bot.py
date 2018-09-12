import time
from threading import Thread
import action
import baekjoon
import snucsepl
import initialize
import irc
from config import *


def read_msg(conn):
	while True:
		in_text = str(conn.get_text())
		try:
			message = in_text.split('PRIVMSG')[1].split(':')[1]
		except:
			continue
		action.react(conn, message)

def update_boj(conn, aclist):
	while True:
		aclist = baekjoon.update_aclist(conn, aclist, boj_username)
		time.sleep(5)

def update_snucsepl(conn, boardlist):
	while True:
		boardlist = snucsepl.update_boardlist(conn, boardlist)
		time.sleep(60)


if __name__ == '__main__':
	conn, aclist, boardlist = initialize.initialize()
	conn.send(channel, ':wave:')
	if bool_respond_message:
		t1 = Thread(target=read_msg, args=(conn,))

	if bool_update_boj:
		t2 = Thread(target=update_boj, args=(conn, aclist))

	if bool_update_pl:
		t3 = Thread(target=update_snucsepl, args=(conn, boardlist))

	if bool_respond_message:
		t1.start()

	if bool_update_boj:
		t2.start()

	if bool_update_pl:
		t3.start()

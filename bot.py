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

	t1 = Thread(target=read_msg, args=(conn,))
	t2 = Thread(target=update_boj, args=(conn, aclist))
	t3 = Thread(target=update_snucsepl, args=(conn, boardlist))

	t1.start()
	t2.start()
	t3.start()

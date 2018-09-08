import time
from threading import Thread
import action
import baekjoon
import initialize
import irc
from config import *


def read_msg(conn):
	while True:
		in_text = str(conn.get_text())
		print(in_text)
		message = in_text.split('PRIVMSG')[1].split(':')[1]
		if(message[:2] == '!q'):
			if(in_text[:17] == ':veydpz!uid282417'):
				exit()
			else:
				conn.send(channel, "!q는 봇 주인만 사용 가능합니다.")
		action.react(conn, message)
		time.sleep(1)

def update_boj(aclist):
	while True:
		aclist = baekjoon.update_aclist(conn, aclist, boj_username)
		time.sleep(5)


if __name__ == '__main__':
	conn, aclist = initialize.initialize()

	t1 = Thread(target=read_msg, args=(conn,))
	t2 = Thread(target=update_boj, args=(aclist,))

	t1.start()
	t2.start()

import action
import baekjoon
from config import *

def repeat(conn, aclist):
	try:
		in_text = str(conn.get_text())
		message = in_text.split('PRIVMSG')[1].split(':')[1]
		if(message[:2] == '!q'):
			if(in_text[:17] == ':veydpz!uid282417'):
				return '<quit>'
			else:
				conn.send(channel, "!q는 봇 주인만 사용 가능합니다.")
		action.react(conn, message)
		print(in_text)
		aclist = baekjoon.update_aclist(conn, aclist, boj_username)
		return '<continue>'
	except IndexError:
		return '<error>'

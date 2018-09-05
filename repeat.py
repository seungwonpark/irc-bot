import action
from config import *

def repeat(conn):
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
		return '<continue>'
	except IndexError:
		return '<error>'

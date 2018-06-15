import requests
import time

from config import *
from irc import *
from action import *

irc = IRC()
irc.connect(server, channel, port, nickname)

while True:
	try:
		in_text = str(irc.get_text())
		message = in_text.split('PRIVMSG')[1].split(':')[1]
		if(message[:2] == '!q'):
			if(in_text[:17] == ':veydpz!uid282417'):
				break
			else:
				irc.send(channel, "!q는 봇 주인만 사용 가능합니다.")
	except IndexError:
		continue
	react(irc, message)
	print(in_text)
	time.sleep(1)

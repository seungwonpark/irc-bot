from coin import *
from config import *

def react(irc, message):
	if(message[:2] == '!c'):
		message = '!c btc'
	if(message[:3] == '!c '):
		ticker = message[3:].strip().upper()
		price = get_coinprice(ticker, "KRW")
		if(price == -1):
			out_text = '%s는 업비트, 고팍스에 없는 코인입니다.' % (ticker)
		else:
			out_text = '%s는 현재 %d원입니다.' % (ticker, price)
		irc.send(channel, out_text)
	if(message[:2] == '!h'):
		irc.send(channel, 'https://github.com/seungwonpark/irc-bot#features')

import coin
from config import *

def react(conn, message):
	message = message.strip()
	print(message)
	if message == '!c':
		message = '!c btc'
	if message[:3] == '!c ':
		ticker = message[3:].strip().upper()
		price = coin.get_coinprice(ticker, "KRW")
		if price == -1:
			out_text = '%s는 업비트, 고팍스에 없는 코인입니다.' % (ticker)
		else:
			if price > 100:
				out_text = '%s는 현재 %s원입니다.' % (ticker, "{:,}".format(int(price)))
			else:
				out_text = '%s는 현재 %.1lf원입니다.' % (ticker, price)
		conn.send(channel, out_text)
	if message == '!h':
		conn.send(channel, 'https://github.com/seungwonpark/irc-bot#features')

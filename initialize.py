from config import *
import irc

def initialize():
	conn = irc.IRC()
	conn.connect(server, channel, port, nickname)
	return conn

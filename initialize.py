from config import *
import irc
import baekjoon

def initialize():
	conn = irc.IRC()
	conn.connect(server, channel, port, nickname)
	aclist = baekjoon.get_aclist(boj_username)
	return conn, aclist

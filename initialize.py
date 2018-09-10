from config import *
import irc
import baekjoon
import snucsepl

def initialize():
	conn = irc.IRC()
	conn.connect(server, channel, port, nickname)
	aclist = baekjoon.get_aclist(boj_username)
	boardlist = snucsepl.get_boardlist()
	return conn, aclist, boardlist

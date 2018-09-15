import requests
import re
import time
from config import *
from bs4 import BeautifulSoup
import emoji

def get_text(username=boj_username):
	req = requests.get('https://acmicpc.net/user/%s' % username)
	return req.text

def get_aclist(username=boj_username):
	html = get_text(username)
	soup = BeautifulSoup(html, 'html.parser')
	ac_html = soup.select("div.col-md-9 > div > div.panel-body")[0]
	probno = ac_html.select("span.problem_number > a")
	probname = ac_html.select("span.problem_title > a")
	probno = [x.text for x in probno]
	probname = [x.text for x in probname]
	ret = []
	for x, y in zip(probno, probname):
		ret.append((x, y))
	return ret

def post_ac(conn, prob):
	probno, probname = prob
	message = ':white_check_mark: :%s: %s boj.kr/%s' % \
		(emoji.get_positive_emoji(), probname, probno)
	conn.send(channel, message)

def post_dbg(conn, prob):
	probno, probname = prob
	message = ':stew: :hammer: %s boj.kr/%s' % (probname, probno)
	conn.send(channel, message)

def update_aclist(conn, aclist_old, username=boj_username):
	try:
		aclist_now = get_aclist(username)
	except:
		return aclist_old
	
	for prob in aclist_now:
		if prob not in aclist_old:
			post_ac(conn, prob)
	for prob in aclist_old:
		if prob not in aclist_now:
			post_dbg(conn, prob)
	return aclist_now

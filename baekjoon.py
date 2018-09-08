import requests
import re
from config import *
from bs4 import BeautifulSoup

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
	probno = prob[0]
	probname = prob[1]
	message = 'AC: %s boj.kr/%s' % (probname, probno)
	conn.send(channel, message)

def update_aclist(conn, aclist_old, username=boj_username):
	aclist_now = get_aclist(username)
	print('There were %d solved problems, found %d solved problems now.' %
		(len(aclist_old), len(aclist_now))
	)
	for prob in aclist_now:
		if prob not in aclist_old:
			post_ac(conn, prob)
	return aclist_now

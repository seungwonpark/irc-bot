import requests
import re
from config import *
from bs4 import BeautifulSoup

def get_text(username=boj_username):
	req = requests.get('https://acmicpc.net/user/%s' % username)
	return req.text

def get_aclist(username=boj_username):
	html = get_text(username)
	temp = re.findall(r'class="result-ac">(.*)</a></span>', html)
	return zip(temp[0::2], temp[1::2])

def post_ac(conn, probno):
	probno = prob[0]
	probname = prob[1]
	message = 'AC: %s boj.kr/%s' % (probname, probno)
	conn.send(channel, message)

def update_aclist(conn, aclist_old, username=boj_username):
	aclist_now = get_aclist(username)
	for prob in aclist_now:
		if prob not in aclist_old:
			post_ac(conn, prob)
	return aclist_now

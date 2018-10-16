import requests
import re
import time
import html
from config import *

def spam(x):
	post_title = x[1]

	# if title does not contain Korean
	if len(re.findall(r'[가-힣]+', post_title)) == 0:
		return True

	return False

def get_boardlist():
	req = requests.get('https://ropas.snu.ac.kr/phpbb/viewforum.php?f=47')
	req.encoding = 'utf-8'
	prefix = '<td class="row1" width="100%"><span class="topictitle">'
	suffix = '</a></span><span class="gensmall"><br />'
	boardlist = re.findall(r'%s(.*?)%s' % (prefix, suffix), req.text)
	post_info = []
	for x in boardlist:
		now_id = re.findall(r'viewtopic\.php\?t=(.*?)&amp;', x)[0]
		now_title = html.unescape(x.split('class="topictitle">')[1])
		post_info.append((now_id, now_title))
	return post_info

def post(conn, post_id):
	url = 'https://ropas.snu.ac.kr/phpbb/viewtopic.php?t=%s' % post_id
	req = requests.get(url)
	req.encoding = 'utf-8'
	post_title = re.findall(r'<title> :: 주제 보기 - (.*?)</title>', req.text)[0]
	post_poster = re.findall(r'</a><b>(.*?)</b></span><br /><span class="postdetails">', req.text)[0]
	message = 'PL: %s | %s' % (post_title, post_poster)
	conn.send(channel, message)
	conn.send(channel, url)

def update_boardlist(conn, boardlist_old):
	# prevent from alerting same post twice
	boardlist_new = list(set(boardlist_old + get_boardlist()))
	print('%s\t found %d post' % (time.strftime('%y/%m/%d %H:%M:%S'), len(boardlist_new)))
	for x in boardlist_new:
		if x not in boardlist_old:
			# debuging messages
			print(boardlist_old)
			print(boardlist_new)
			print(x)
			if not spam(x):
				post(conn, x[0])
	return boardlist_new

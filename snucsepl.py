import requests
import re
from config import *

def get_boardlist():
	req = requests.get('https://ropas.snu.ac.kr/phpbb/viewforum.php?f=47')
	req.encoding = 'utf-8'
	prefix = '<td class="row1" width="100%"><span class="topictitle">'
	suffix = '</a></span><span class="gensmall"><br />'
	boardlist = re.findall(r'%s(.*)%s' % (prefix, suffix), req.text)
	post_info = []
	for x in boardlist:
		now_id = re.findall(r'viewtopic\.php\?t=(.*)&amp;', x)[0]
		now_title = x.split('class="topictitle">')[1]
		post_info.append((now_id, now_title))

def post(conn, post_id):
	url = 'https://ropas.snu.ac.kr/phpbb/viewtopic.php?t=%s' % post_id
	req = requests.get(url)
	req.encoding = 'utf-8'
	post_title = re.findall(r'<title> :: 주제 보기 - (.*)</title>', req.text)
	post_poster = re.findall(r'</a><b>(.*)</b></span><br /><span class="postdetails">', req.text)
	message = '%s | %s\n%s' % (post_poster, post_title, url)
	conn.send(channel, message)

def update_boardlist(conn, boardlist_old):
	boardlist_new = get_boardlist()
	for x in boardlist_new:
		if x not in boardlist_old:
			post(conn, x[0])

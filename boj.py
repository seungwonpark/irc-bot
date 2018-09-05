import requests
import re
from bs4 import BeautifulSoup

def get_aclist(username):
	req = requests.get('https://acmicpc.net/user/%s' % username)
	html = req.text
	temp = re.findall(r'class="result-ac">(.*)</a></span>')
	num = temp[0::2]
	probname = t
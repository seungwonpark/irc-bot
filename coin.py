import requests

code_format = 'CRIX.UPBIT.{to_currency}-{from_currency}'
baseurl = "https://crix-api-cdn.upbit.com/v1/crix/candles/minutes/60?code="

def get_coinprice(from_currency, to_currency):
	# params are case-insensitive
	req = requests.get(baseurl + code_format.format(from_currency=from_currency, to_currency=to_currency))
	li = req.json()
	if(len(req.text) < 150): # error
		return -1
	else:
		return li[0]["tradePrice"]

import json
import requests
from texttospeech import texttospeech
def thathinh():
	type_data = input("bạn thả thính cho nam hay nữ? nếu là nam nhập boy nữ nhập girl: ")
	full_url = 'https://manhict.tech/thathinh' + "?type" + type_data
	get = requests.get(full_url)
	data = get.text
	parse_json = json.loads(data)
	infomation = parse_json['result']['data'] 
	texttospeech(infomation)
import json
import requests
from texttospeech import texttospeech
def keobuabao():
	while True:
		url = 'https://manhict.tech/game/kbb?choose='
		choose = input("nhập kéo búa bao: ")
		full_url = url + choose 
		get = requests.get(full_url)
		data = get.text
		parse_json = json.loads(data)
		computer_choose = parse_json['computerChoose']
		you_choose = choose
		ketqua = parse_json['result']
		result = """bạn chọn {you_choose} \nmáy chọn {computer_choose} \nbạn {ketqua}""".format(you_choose = you_choose, computer_choose = computer_choose, ketqua = ketqua)
		if("lose" in result):
			print(result.replace("lose", "thua")) 
			texttospeech(result)
		elif("win" in result):
			print(result.replace("win", "thắng"))
			texttospeech(result)
		elif("hòa" in result):
			print(result)
			texttospeech(result)
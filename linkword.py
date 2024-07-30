import requests 
import json
from texttospeech import texttospeech
def linkword():
	texttospeech("chào mừng bạn đến với nối từ, nơi thể hiện vốn từ phong phú của bạn")
	while True:
		choose = 'https://manhict.tech/game/linkword?word='
		yourchoose = input("nhập từ để bắt đầu chơi nói từ: ")
		full_url = choose + yourchoose
		get = requests.get(full_url)
		data = get.text
		load = json.loads(data)
		if (" " in yourchoose):
			result = load['text']
			print(result)
			if ("thua" in result):
				print(result.replace("thua", "thắng"))
			else: 
				print(" ")
		elif (" " not in yourchoose):
			error = load['error']
			print(error)
		#elif ("quit game" in yourcehoos):
			#print("------------------------------------end game------------------------------------")
			#break
		else:
			print(" ")
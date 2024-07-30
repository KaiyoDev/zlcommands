import requests
from texttospeech import texttospeech
def translate():
	texttospeech("nhập câu cần dịch vào đây")
	api_url = "https://manhict.tech/trans?query="
	word = input("nhập câu cần dịch: ")
	full_url = '{api_url}{word}'.format(api_url = api_url, word = word)
	x =  requests.get(full_url)
	data = x.json()
	result = data["result"]
	type1 = data["type"]
	full_result = result + "\n" + type1 
import requests
import json
from texttospeech import texttospeech
def dovui():
	url = 'https://manhict.tech/game/dovuiv1'
	get = requests.get(url)
	data = get.text
	json = json.loads(data)
	cau_hoi = json['questions']
	a = json['a']
	b = json['b']
	c = json['c']
	d = json['d']
	dap_an = json['dapan']
	result = """{cau_hoi} \nA.{a}\nB.{b}\nC.{c}\nD.{d}""".format(cau_hoi = str(cau_hoi), a = str(a), b = str(b), c = str(c), d = str(d))
	print(result)
	cau_tra_loi = input("nhập câu trả lời vào đây: ")
	if(cau_tra_loi) == dap_an:
		print("câu trả lời chính xác, đáp án là {dap_an}").format(dap_an = str(dap_an))
	if(cau_tra_loi) != dap_an:
		print("chưa chính xác rồiiiii:((, đáp án là {dap_an}").format(dap_an = str(dap_an))
import requests
import json
from texttospeech import texttospeech
def covid19():
	full_url = 'https://manhict.tech/covid?country=viet%20nam'
	get = requests.get(full_url)
	data = get.text
	parse_json = json.loads(data)
	data1 = parse_json['data']['danso']
	data2 = parse_json['data']['dangdieutri']
	data3 = parse_json['data']['ca_nhiem_moi']
	data4 = parse_json['data']['hoiphuc']
	data5 = parse_json['data']['total']
	data6 = parse_json['data']['tong_ca_tu_vong']
	result = """thông tin về dịch bệnh cô vít 19 tại Việt Nam như sau: dân số {data1} người, tổng số ca nhiễm: {data5}, số ca đang điều trị {data2} ca, số bệnh nhân đã khỏi bệnh: {data4} bệnh nhân, ca nhiễm mới: {data3}, tổng số ca dã tử vong: {data6}""".format(data1 = str(data1), data2 = str(data2), data3 = str(data3), data4 = str(data4), data5 = str(data5), data6 = str(data6))
	print(result)
	texttospeech(result)
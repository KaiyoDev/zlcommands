import requests
import json
from texttospeech import texttospeech
def taixiu():
	texttospeech("chào mừng bạn đến với tài xỉu")
	print("chào mừng bạn đến với game tài xỉu (nhập hd để biết luật chơi)")
	start = input("nhập start để bắt đầu game, nhập hd để biết luật chơi hoặc nhập quit để thoát trò chơi: ")
	if (start == "hd"):
		print("luật chơi tài xỉu như sau: \n có 3 cách chơi \n cách 1: cược tài/xỉu. Nếu cược xỉu Sẽ thắng cược khi tổng số điểm của 3 xúc xắc là từ 4 đến 10. Nếu cược tài Sẽ thắng cược khi tổng số điểm của 3 xúc xắc là từ 11 đến 17. \n cách 2: cược chẵn/lẻ. Nếu cược chẵn sẽ thắng cược khi tổng số điểm của 3 xúc xắc là 4,6,8,10,12,14,16. Nếu cược lẻ sẽ thắng cược khi tổng số điểm của 3 xúc xắc là 5,7,9,11,13,15,17. \n cách 3: cược số. Thắng cược khi kết quả của 1 trong 3 xúc xắc hiển thị đúng con số mà người chơi đã chọn. cách 1 có 1 trường hợp đặc biệt đó là bộ ba bất kì nhưng do mình sẽ không làm kiểu chơi này vậy nên chúng ta vẫn sẽ chơi như thường")
	elif (start == "start"):
		print("\n-----------------------------bắt đầu game-----------------------------\n")
		while True:
			method = input("chọn cách cược (nếu không hiểu có thể dùng lệnh hd để biết rõ luật chơi hơn): ")
			base_url = 'https://manhict.tech/game/v2/taixiu?method='
			api_key = '&apikey=KeyTest'
			full_url = base_url + method + api_key
			get = requests.get(full_url)
			data = get.text
			parse_json = json.loads(data)
			if (method == "tai"):
				bat1 = parse_json['mở bát']['one']
				bat2 = parse_json['mở bát']['two']
				bat3 = parse_json['mở bát']['three']
				tong = parse_json['người chơi']['chất']
				nha_cai = parse_json['nhà cái']
				nha_cai_ra = parse_json['mở bát']['total']
				chat = parse_json['người chơi']['chất']
				ketqua = parse_json['ketqua']['total']
				result = """nhà cái ra {nha_cai_ra} ({nha_cai}), bạn chọn {tong}. Bạn {ketqua}""".format(nha_cai = str(nha_cai), tong = str(tong), chat = str(chat), ketqua = str(ketqua), nha_cai_ra = str(nha_cai_ra))
				if ("lose" in result):
					print(result.replace("lose", "thua"))
				elif ("win" in result):
					print(result.replace("win", "thắng"))
			elif (method == "xiu"):
				bat1 = parse_json['mở bát']['one']
				bat2 = parse_json['mở bát']['two']
				bat3 = parse_json['mở bát']['three']
				tong = parse_json['người chơi']['chất']
				nha_cai = parse_json['nhà cái']
				nha_cai_ra = parse_json['mở bát']['total']
				chat = parse_json['người chơi']['chất']
				ketqua = parse_json['ketqua']['total']
				result = """nhà cái ra {nha_cai_ra} ({nha_cai}), bạn chọn {tong}. Bạn {ketqua}""".format(nha_cai = str(nha_cai), tong = str(tong), chat = str(chat), ketqua = str(ketqua), nha_cai_ra = str(nha_cai_ra))
				if ("lose" in result):
					print(result.replace("lose", "thua"))
				elif ("win" in result):
					print(result.replace("win", "thắng"))
			elif (method == "chan"):
				bat1 = parse_json['mở bát']['one']
				bat2 = parse_json['mở bát']['two']
				bat3 = parse_json['mở bát']['three']
				tong = parse_json['người chơi']['chất']
				nha_cai = parse_json['nhà cái']
				chat = parse_json['mở bát']['total']
				ketqua = parse_json['ketqua']['total']
				result = """nhà cái ra {chat} ({nha_cai}) bạn cược {tong} . Bạn {ketqua}""".format(nha_cai = str(nha_cai), tong = str(tong), chat = str(chat), ketqua = str(ketqua))
				if ("lose" in result):
					print(result.replace("lose", "thua"))
				elif ("win" in result):
					print(result.replace("win", "thắng"))
			elif (method == "le"):
				bat1 = parse_json['mở bát']['one']
				bat2 = parse_json['mở bát']['two']
				bat3 = parse_json['mở bát']['three']
				tong = parse_json['người chơi']['chất']
				nha_cai = parse_json['nhà cái']
				chat = parse_json['mở bát']['total']
				ketqua = parse_json['ketqua']['total']
				result = """nhà cái ra {chat} ({nha_cai}) bạn cược {tong}. Bạn {ketqua}""".format(nha_cai = str(nha_cai), tong = str(tong), chat = str(chat), ketqua = str(ketqua))
				if ("lose" in result):
					print(result.replace("lose", "thua"))
				elif ("win" in result):
					print(result.replace("win", "thắng"))
			elif (method == "so"):
				value = input("nhập số bạn muốn đặt cược (nếu không hiểu có thể gõ lệnh hd để biết luật chơi): ")
				base_url_so = 'https://manhict.tech/game/v2/taixiu?method=so&'
				api_key_so = '&apikey=KeyTest'
				full_url_so = base_url_so + "value=" + value + api_key_so
				get_so = requests.get(full_url_so)
				data_so = get_so.text
				parse_json_so = json.loads(data_so)
				you = parse_json_so['người chơi']['total']
				ketqua2 = parse_json_so['ketqua']['total']
				ketqua_so = parse_json_so['mở bát']['bộ']
				result = """bạn chọn {you}, kết quả là {ketqua_so}. bạn {ketqua2}""".format(ketqua2 = str(ketqua2), ketqua_so = str(ketqua_so), you = str(you))
				if ("lose" in result):
					print(result.replace("lose", "thua"))
				elif ("win" in result):
					print(result.replace("win", "thắng"))
			elif (method == "hd"):
				print("luật chơi tài xỉu như sau: \n có 3 cách chơi \n cách 1: cược tài/xỉu. Nếu cược xỉu Sẽ thắng cược khi tổng số điểm của 3 xúc xắc là từ 4 đến 10. Nếu cược tài Sẽ thắng cược khi tổng số điểm của 3 xúc xắc là từ 11 đến 17. \n cách 2: cược chẵn/lẻ. Nếu cược chẵn sẽ thắng cược khi tổng số điểm của 3 xúc xắc là 4,6,8,10,12,14,16. Nếu cược lẻ sẽ thắng cược khi tổng số điểm của 3 xúc xắc là 5,7,9,11,13,15,17. \n cách 3: cược số. Thắng cược khi kết quả của 1 trong 3 xúc xắc hiển thị đúng con số mà người chơi đã chọn. cách 1 có 1 trường hợp đặc biệt đó là bộ ba bất kì nhưng do mình sẽ không làm kiểu chơi này vậy nên chúng ta vẫn sẽ chơi như thường")
			elif (method == "quit"):
				print("-----------------------------end game-----------------------------")
				break
			else:
				print("cú pháp không hợp lệ, vui lòng gõ lại")
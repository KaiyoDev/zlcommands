import webbrowser
from texttospeech import texttospeech
def google_search():
	texttospeech("nhập thứ bạn cần tìm kiếm trên google vào đây")
	result = input("nhập thứ cần tìm kiếm trên google: ")
	search_url = "https://www.google.com/search?q=" + result + "&sxsrf=APq"
	webbrowser.register('chrome',
		None,
		webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
	webbrowser.get('chrome').open(search_url)
	texttospeech("đây là các kết quả tìm kiếm")
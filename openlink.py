import webbrowser
from texttospeech import texttospeech
def open_link():
	texttospeech("dán linh bạn cần mở trên chờ rom vào đây")
	result = input("dán link vào đây: ")
	url = result
	webbrowser.register('chrome',
		None,
		webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
	webbrowser.get('chrome').open(url)
	texttospeech("đã mở linh")
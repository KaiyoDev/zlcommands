from youtube_search import YoutubeSearch
import webbrowser
from texttospeech import texttospeech
import json
def openvideoytb():
    texttospeech("nhập từ khóa vào đây để mở video diu túp với từ khóa đó")
    keyword = input("nhập từ khóa cần tìm kiếm trên youtube: ")  
    search = YoutubeSearch('{keyword}'.format(keyword = keyword), max_results=1).to_json()
    search_dict = json.loads(search)
    for v in search_dict['videos']:
        result = 'https://www.youtube.com/watch?v=' + v['id']
        webbrowser.register('chrome',
            None,
            webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(result)
    texttospeech("đã mở video youtube từ từ khóa")
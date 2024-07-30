from texttospeech import texttospeech
from youtube_search import YoutubeSearch
import requests, json
def youtube():
    texttospeech("nhập từ khóa vào đây để mở video diu túp")
    keyword = input("nhập từ khóa cần tìm kiếm trên youtube: ")  
    search = YoutubeSearch('{keyword}'.format(keyword = keyword), max_results=10).to_json()
    search_dict = json.loads(search)
    for v in search_dict['videos']:
        result = 'https://www.youtube.com/watch?v=' + v['id'] + " - " + v['title'] + " kênh " + v['channel']
        print(result)
    texttospeech("đây là các kết quả tìm kiếm, bạn có cóp py linh vi deo bạn muốn xem rồi dùng lệnh mở video diu túp để mở vi deo")
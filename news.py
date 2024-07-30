import requests
from bs4 import BeautifulSoup
from texttospeech import texttospeech
def news():
    url='https://kenh14.vn'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    for x in headlines:
        print(x.text.strip())
    texttospeech("đây là các bài báo mới nhất hôm nay")
from speechtotext import speechtotext
from texttospeech import texttospeech
from youtubesearch import youtube
from weather import weather
from dictionary import dictionary
import time
from linkword import linkword
from dovui import dovui
from taixiu import taixiu
from thathinh import thathinh
from news import news
from keobuabao import keobuabao
from translate import translate
from openvideoytb import openvideoytb
from openfile import openfile
from xsmb import xsmb
from covid19 import covid19
from openlink import open_link
from search import google_search
from help import support
texttospeech("xin chào, tôi có thể giúp gì cho bạn") 
while True:
    text = input("nhập vào đây để nói chuyện với bot: ")
    if ("ban la ai" in text):
        texttospeech("tôi là trợ lý ảo AI")
    elif ("thoi tiet" in text):
        weather()
    elif ("tong thong" in text):
        texttospeech("tổng thống Mỹ hiện tại là dâu bai đần")
    elif ("tim video" in text):
        youtube()
    elif ("thoi gian" in text):
        time = time.localtime()
        tm_wday = time.tm_wday 
        tm_mday = time.tm_mday
        tm_mon = time.tm_mon
        tm_hour = time.tm_hour
        tm_min = time.tm_min
        tm_sec = time.tm_sec
        tm_year = time.tm_year
        result = """hôm nay là ngày {tm_mday} tháng {tm_mon} năm {tm_year} lúc {tm_hour} giờ {tm_min} phút {tm_sec} giây""".format(tm_wday = tm_wday, tm_sec = tm_sec, tm_hour = tm_hour, tm_mday = tm_mday, tm_min = tm_min, tm_mon = tm_mon, tm_year = tm_year)
        texttospeech(result)
    elif ("mo google chrome" in text):
        openfile()
    elif ("wikipedia" in text):
        dictionary()
    elif ("ban co the" in text):
        support()
    elif ("mo link" in text):
        open_link()
    elif ("tim kiem" in text):
        google_search()
    elif ("google dich" in text):
        translate()
    elif ("mo video ytb" in text):
        openvideoytb()
    elif ("doc bao" in text):
        news()
    elif ("covid19" in text):
        covid19()
    elif ("xsmb" in text):
        xsmb()
    elif ("thathinh" in text):
        thathinh()
    elif ("choi tai xiu" in text):
        taixiu()
    elif ("choi keo bua bao" in text):
        keobuabao()
    elif ("do vui" in text):
        dovui()
    elif ("noi tu" in text):
        linkword()
    elif ("tam biet" in text):
        texttospeech("tạm biệt")
        SystemExit()
        break
    else:
        texttospeech("xin lỗi, tôi không hiểu câu này")
import json
import requests 
from texttospeech import texttospeech
url1 = 'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'
get1 = requests.get(url1)
data1 = get1.text
json1 = json.loads(data1)
idd = json1['deck_id']
boc_bai = 'https://deckofcardsapi.com/api/deck/' + idd + '/draw/?count=1'
get2 = requests.get(boc_bai)
data2 = get2.text
json2 = json.loads(data2)
card = json2['cards'][0]['code']
card1 = json2['cards'][1]['code']
#bich
if card == "2S":
	card = "2 bich"
if card == "3S":
	card = "3 bich"
if card == "4S":
	card = "4 bich"
if card == "5S":
	card = "5 bich"
if card =="6S":
	card = "6 bich"
if card == "7S":
	card = "7 bich"
if card == "8S":
	card = "8 bich"
if card == "9S":
	card = "9 bich"
#tep
if card == "2C":
	card = "2 tep"
if card == "3C":
	card = "3 tep"
if card == "4C":
	card = "4 tep"
if card == "5C":
	card = "5 tep"
if card == "6C":
	card = "6 tep"
if card == "7C":
	card = "7 tep"
if card == "8C":
	card = "8 tep"
if card == "9C":
	card = "9 tep"
#do
if card == "2D":
	card = "2 do"
if card == "3D":
	card = "3 do"
if card == "4D":
	card = "4 do"
if card == "5D":
	card = "5 do"
if card == "6D":
	card = "6 do"
if card == "7D":
	card = "7 do"
if card == "8D":
	card = "8 do"
if card == "9D":
	card = "9 do"
#co
if card == "2H":
	card = "2 co"
if card == "3H":
	card = "3 co"
if card == "4H":
	card = "4 co"
if card == "5H":
	card = "5 co"
if card == "6H":
	card = "6 co"
if card == "7H":
	card = "7 co"
if card == "8H":
	card = "8 co"
if card == "9H":
	card = "9 co"
#card1
if card1 == "2S":
	card1 = "2 bich"
if card1 == "3S":
	card1 = "3 bich"
if card1 == "4S":
	card1 = "4 bich"
if card1 == "5S":
	card1 = "5 bich"
if card1 =="6S":
	card1 = "6 bich"
if card1 == "7S":
	card1 = "7 bich"
if card1 == "8S":
	card1 = "8 bich"
if card1 == "9S":
	card1 = "9 bich"
#tep
if card1 == "2C":
	card1 = "2 tep"
if card1 == "3C":
	card1 = "3 tep"
if card1 == "4C":
	card1 = "4 tep"
if card1 == "5C":
	card1 = "5 tep"
if card1 == "6C":
	card1 = "6 tep"
if card1 == "7C":
	card1 = "7 tep"
if card1 == "8C":
	card1 = "8 tep"
if card1 == "9C":
	card1 = "9 tep"
#do
if card1 == "2D":
	card1 = "2 do"
if card1 == "3D":
	card1 = "3 do"
if card1 == "4D":
	card1 = "4 do"
if card1 == "5D":
	card1 = "5 do"
if card1 == "6D":
	card1 = "6 do"
if card1 == "7D":
	card1 = "7 do"
if card1 == "8D":
	card1 = "8 do"
if card1 == "9D":
	card1 = "9 do"
#co
if card1 == "2H":
	card1 = "2 co"
if card1 == "3H":
	card1 = "3 co"
if card1 == "4H":
	card1 = "4 co"
if card1 == "5H":
	card1 = "5 co"
if card1 == "6H":
	card1 = "6 co"
if card1 == "7H":
	card1 = "7 co"
if card1 == "8H":
	card1 = "8 co"
if card1 == "9H":
	card1 = "9 co"
print(card, card1)
print(boc_bai)
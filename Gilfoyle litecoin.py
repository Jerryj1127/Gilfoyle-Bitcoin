import requests
import json
from playsound import playsound
#rupee_value-->OLD= 'https://api.exchangeratesapi.io/latest?base=USD&symbols=INR'
lwr_thr= int(input('Enter the lower threshold : '))
up_thr= int(input('Enter the upper threshold : '))

rupee_url= 'https://api.coincap.io/v2/rates/indian-rupee'
lite_url= 'https://api.coincap.io/v2/rates/litecoin'
cflag =True
rflag =True
def getrupee():
    while rflag:
        response_rupee = requests.get(rupee_url)
        response_rupee_json = response_rupee.json()
        rupee_in_usd =float(response_rupee_json['data']['rateUsd'])
        timestamp_rupee = response_rupee_json['timestamp']
        usd_in_rupee = 1/rupee_in_usd
        return usd_in_rupee
        break
def getlite():
    while cflag:
        response_coin=requests.get(lite_url)
        response_coin_json=response_coin.json()
        priceusd =float(response_coin_json['data']['rateUsd'])
        timestamp_coin= response_coin_json['timestamp']
        #print(priceusd)
        return priceusd
        break
#print(type(response_json))
#print(response_json)

while True:
    priceusd= getlite()
    rupee= getrupee()
    litecoin= (priceusd*rupee)
    if litecoin>up_thr or litecoin<lwr_thr:
        playsound('litecoin.wav')
    print('Price of litecoin:',litecoin)


#def flagger:
#    flag=0
#    if litecoin>up_thr:
 #       flag+=1


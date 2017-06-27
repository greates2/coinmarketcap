import requests
from pprint import pprint
from urllib.parse import urlencode


def main():
    URL = 'https://api.coinmarketcap.com/v1/'
    ticker = 'ticker/'
    currency = {
        'dgb': 'digibyte',
        'ltc': 'litecoin',
        'doge': 'dogecoin',
    }
    get_currency = input("Выберите валюту из {}".format([x for x in currency]))

    r = requests.get(url=(URL + ticker + currency[get_currency]))
    # print(URL + ticker + currency[get_currency], params=params)
    pprint("Цена за {} равняется {} USD".format(get_currency.upper(), r.json()[0]['price_usd']))


main()

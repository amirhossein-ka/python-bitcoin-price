import requests
import time


while True:
    res = requests.get(
        "https://api.livecoin.net/exchange/ticker?currencyPair=BTC/USD")

    price = (res.json())

    value = ("The highest price is {} USD and the last price is {} USD").format(
        price['high'], price['last'])
    print(value)

    time.sleep(30)

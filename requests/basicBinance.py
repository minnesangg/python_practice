import requests

url = 'https://api.binance.com/api/v3/ticker/price'
btc_prices = []
try:
    response = requests.get(url, params={'symbol': 'BTCUSDT'})
    price = float(response.json()['price'])
    btc_prices.append(price)
    print(btc_prices)
except requests.exceptions.ConnectionError:
    print('Connection error')

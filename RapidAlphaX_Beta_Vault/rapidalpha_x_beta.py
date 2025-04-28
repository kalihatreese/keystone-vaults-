from alpaca_trade_api import REST
import os

API_KEY = 'YOUR_ALPACA_API_KEY'
API_SECRET = 'YOUR_ALPACA_SECRET_KEY'
BASE_URL = 'https://paper-api.alpaca.markets'

api = REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

symbol = 'AAPL'
qty = 1

def rapidalpha_trade():
    print(f'Submitting buy order for {symbol}...')
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
    print(f'Order submitted for {symbol}''')

rapidalpha_trade()

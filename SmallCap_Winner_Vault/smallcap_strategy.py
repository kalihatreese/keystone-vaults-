import ccxt
import time

profit_target = 1.25
symbol = 'BSC/NEWCOIN'
amount = 1

exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET_KEY'
})

def smallcap_sniper():
    print(f'Placing order for {symbol}...')
    buy_order = exchange.create_market_buy_order(symbol, amount)
    buy_price = buy_order['average']

    print(f'Bought at {buy_price}, monitoring for profit...')
    target_price = buy_price * profit_target

    while True:
        ticker = exchange.fetch_ticker(symbol)
        current_price = ticker['last']

        if current_price >= target_price:
            print(f'Target hit! Selling at {current_price}')
            exchange.create_market_sell_order(symbol, amount)
            break
        time.sleep(5)

smallcap_sniper()

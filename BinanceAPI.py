import os
from symtable import Symbol
from binance.client import Client
from binance.spot import Spot 

# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')
client = Client(api_key, api_secret)

def getTimeStamp(client):
    # Get server timestamp
    print(client.time())

def getAccBalance(client):
    # Get account and balance information
    print(client.account())

# This is our function to initialize a trade using the Binance API; all params must be in between single quotes
# except for quantity and price
def makeTrade(symbol, side):
    params = {
    'symbol': "'" + symbol + "'",
    'side': side,
    'type': 'MARKET',
    'timeInForce': 'GTC',
    'quantity': calculateQuantity(symbol),
    'price': getLatestPrice(symbol)
    }
    response = client.new_order(**params)
    print(response)

# ticker has to be of type "BTCUSDT"
def getLatestPrice(ticker):
    # get latest price from Binance API
    asset_price = client.get_symbol_ticker(Symbol="'" + ticker + "'")

def calculateQuantity(symbol):
    return (getAccBalance(client) * .02) / getLatestPrice(symbol)

def sell(symbol):
    makeTrade(symbol, 'SELL')

def buy(symbol):
    makeTrade(symbol, 'BUY')


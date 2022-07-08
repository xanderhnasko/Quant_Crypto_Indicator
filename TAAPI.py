# Import the requests library
import requests
import BinanceAPI
from BinanceAPI import *
import csv


#True if MACD value is greater than MACD signal
is_positive = None

# Define endpoint
endpoint = "https://api.taapi.io/bulk"

# Define a JSON body with parameters to be sent to the API
parameters = {
    "secret": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjJiYjVlYjM2YzI4YjU1Y2Q1NzgzOTVmIiwiaWF0IjoxNjU2NDQ2NjQzLCJleHAiOjMzMTYwOTEwNjQzfQ.sH0kilANcSYI6kwSn3cQzOcIgVjQzhdwJ3wspfYl64g",
    "construct": {
        "exchange": "binance",
        "symbol": "BTC/USDT",
        "interval": "1h",
        "indicators": [
            {
                # MACD Backtracked 0
                "id": "My custom id",
                "indicator": "macd",
                "backtrack": 0
            },

            {
                # MACD Backtracked 1
                "id": "My custom id",
                "indicator": "macd",
                "backtrack": 1
            }
        ]
    }
}

csvfile = 'BTC_USD_Bitstamp_minute_2022-07-07.csv'
reader = csv.reader(csvfile, delimiter= ' ', quotechar= '|')

# Gets the moving average
def get_moving_average_volume(filename):
    avg = 0
    tracker = 0
    next(reader)
    for row in reader:
        avg += reader[row, 6]
        tracker += 1
    return avg/tracker
        
        
while(True):
    # Send POST request and save the response as response object
    response = requests.post(url=endpoint, json=parameters)

    # Extract data in json format
    result = response.json()

    # Print result
    print(result)

    print(result.get('data')[0].get('result').get('valueMACD'))
    print(result.get('data')[0].get('result').get('valueMACDSignal'))
    value_0 = result.get('data')[0].get('result').get('valueMACD')
    signal_0 = result.get('data')[0].get('result').get('valueMACDSignal')

    value_1 = result.get('data')[1].get('result').get('valueMACD')
    signal_1 = result.get('data')[1].get('result').get('valueMACDSignal')

    #is_positive is True if value > signal, if we find that the value < signal now,
    #the value line has dropped below signal, indicating a sell. Vice versa for buy
    if is_positive == True and (value_0 - signal_0 < 0):
        if(reader[len(next(reader)), 5] >= get_moving_average_volume(csvfile)):
            print("Sell")
            BinanceAPI.sell(parameters["construct"]["symbol"])
            # TODO write logic to initiate the sell order

    elif is_positive == False and (value_0 - signal_0 > 0):
        if(reader[len(next(reader)), 5 ] >= get_moving_average_volume(csvfile)):
            print("Buy")
            BinanceAPI.buy(parameters["construct"]["symbol"])
            # TODO write logic to initiate the buy order

    #Updates the value of is_positive based on current MACD value and signal
    if(value_0 - signal_0 > 0):
        is_positive = True
    elif (value_0 - signal_0 == 0):
        is_positive = is_positive
    else:
        is_positive = False

    
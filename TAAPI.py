# Import the requests library
import requests

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

    if value_0 == signal_0:
        if value_1 > signal_1:
            print("Sell")
        else:
            print("Buy")

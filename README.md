# Quant-Crypto-Indicator-bot
 
 - Currently experimenting with applying NLP models to see if a competitive advantage in sell/buy-news trading can be consistently achieved, particularly in low MC coins
 
## Implemented:
 - uses exchange API keys to execute live-time trades over any coin market
 - Uses medium-term moving average and short-term trend data to establish grounds for trade execution
 - Confirms Moving Average Convergence/Divergence signals with corss-referenced buy/sell volume data to weed-out false positive signals
 - Uses triggered trailing stop-loss to exit trades once a certain profit margin has been achieved
 
## To do
1. Simulate trades over large periods of time, generalize results.
2. Integrate neural network for V2, cross test with V1 volume.

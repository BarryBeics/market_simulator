import random
import matplotlib.pyplot as plt
import json
import pandas as pd
import numpy as np
from functions import snap_to_moving_average, next_move

# STEP 1. BUILD A PERMUTATION
# This must be a whole int, e.g. 3 will result in the volatility being able to go between -3.9% & + 3.9% making a range of 7.8%
volatility = 1
# Set the parameters you want to test
stop_loss = -0.075
take_profit = 0.05
market_momentum = 0.02
# Choose how long in seconds you wish to be in a trade before timeing out and exiting the trade.
time_in_trade = 900

# STEP 2. RUN A TRADE
crypo_price = 29387

# When looking for a trend pattern over what period are you looking for confimation 3600 time_in_trade is 1 hour
trend_confirmation = 3600

# Set up values
actual_price = crypo_price
average_price = crypo_price

gain_over_period = crypo_price * market_momentum
average_price_increment = gain_over_period / trend_confirmation

open_to_trade = True
take_profit_amount = crypo_price + (crypo_price * take_profit)
stop_loss_amount = crypo_price + (crypo_price * stop_loss)

snap_back = snap_to_moving_average(time_in_trade)
count = 0



#Gather data for mpl (matplotlib)
mpl_secs = []
mpl_Avg = []
mpl_tp = []
mpl_sl = []
mpl_price = []
for sec in range(time_in_trade):
    average_price += average_price_increment

    if sec == snap_back[count]:
        actual_price = average_price
        count += 1
    else:
        move = next_move(volatility)
        move_amount = average_price * move
        total_move = average_price_increment + move_amount
        actual_price = total_move + actual_price

    mpl_secs.append(sec+1)
    mpl_Avg.append(round(average_price,2))
    mpl_tp.append(take_profit_amount)
    mpl_sl.append(stop_loss_amount)
    mpl_price.append(round(actual_price,2))


    if actual_price >= take_profit_amount and open_to_trade == True:
        break

    if actual_price <= stop_loss_amount and open_to_trade == True:
        break

    if sec == (time_in_trade -1) and open_to_trade == True:
        break

each_trade = {
'Second': mpl_secs,
'Avg_price' : mpl_Avg,
'tp': mpl_tp,
'sl': mpl_sl,
'Price': mpl_price
}
price_data = each_trade


price_action = json.dumps(price_data, indent = 2)
with open('data/price_action.json', 'w') as f:
    f.write(price_action)

data = json.load(open("data/price_action.json"))

df = pd.DataFrame.from_dict(data)

print(df)
def set_boundary(ax1):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('gray')
    ax.spines['bottom'].set_color('gray')


fig = plt.figure(figsize=(8,4))
ax = plt.subplot(111)
ax.plot(df.Second, df.Avg_price, label='Avg Price')
ax.plot(df.Second, df.tp, label='Take Profit', color='green')
ax.plot(df.Second, df.sl, label='Stop Loss', color='red')
ax.plot(df.Second, df.Price, marker='o', markersize=3, alpha=0.4, label='Actual Price', color='magenta')
set_boundary(ax)
plt.xlabel('Trade duration in seconds')
plt.ylabel('Crypto Price')
plt.title('Trade example')
plt.legend()
plt.show()


import random
import json
import pandas as pd
import numpy as np
from functions import snap_to_moving_average, next_move

# Here we enter the values that will make up each permutation
volatility = [6,7,8,9]

# the higher the tolerence figure the closer the price hugs the moving average
stop_loss = [ -0.07, -0.08]
take_profit = [0.03, 0.04]
market_momentum = [0.05, 0.06, 0.07]
time_in_trade = [600, 900]

trades_list = []

permutaion_counter = 0
# These five nested for loops build up each permutation ahead of the market simulation being carried out one each
for vol in volatility:
    for stop in stop_loss:
        for take in take_profit:
            for mark in market_momentum:
                for time in time_in_trade:

                    permutaion_counter += 1

                    each_trade = {  'volatility': vol,
                                    'stop_loss' :stop,
                                    'take_profit':take,
                                    'market_momentum' : mark,
                                    'time_in_trade' : time

                                     }
                    trades_list.append(each_trade)


#saving the data
    trade_result = json.dumps(trades_list, indent = 2)
    with open('data/permutations.json', 'w') as f:
        f.write(trade_result)

print(permutaion_counter)


f = open('data/permutations.json')


crypo_price = 29387

# When looking for a trend pattern over what period are you looking for confimation 3600 time_in_trade is 1 hour
trend_confirmation = 3600


for i in data:
    stop_loss = i['stop_loss']
    take_profit = i['take_profit']
    tol_range = i['tolerance']
    market_momentum = i['market_momentum']
    ATR = i['volatility']
    permutaion_counter += 1


    #reports on the activity for each permutation
    successes = 0
    win = 0
    losses = 0
    timed_out = 0
    total_fees = 0
    profit = 0
    trade_profit = 0
    time_in_win_trade = []
    time_in_loss_trade = []

    market_momentum_price = crypo_price
    carried_balance = opening_steak

    gain_over_period = market_momentum_price * market_momentum
    momentum_increment = gain_over_period / watching_period


    price_moves = []

    for instance in range(number_of_trades):
        carried_price = crypo_price

        trade_open = True
        take_profit_amount = carried_price + (carried_price * take_profit)
        stop_loss_amount = carried_price + (carried_price * stop_loss)

        correction = []
        workings = 0
        for n in range(100):
            random_select = random.randint(20, 101)
            workings += random_select
            if workings >= seconds + 100:
                break
            correction.append(workings)
        next = 0
        selector = 0

        market_price = carried_price
        market_momentum_price = carried_price
        mpl_secs = []
        mpl_Avg = []
        mpl_tp = []
        mpl_sl = []
        mpl_price = []
        for x in range(seconds):
            market_momentum_price += momentum_increment

            selector = correction[next]
            if x == selector:
                market_price = market_momentum_price
                next += 1
            else:
                big_random = random.randint(0, ATR)
                decimal_random = random.randint(0, 9)
                decimal = decimal_random / 10
                change = big_random + decimal
                fliper = random.randint(-1, 1)
                move = (change * fliper)
                move_amount = market_momentum_price * (move/tol_range)


                move_per_secound = move_amount / 60
                total_move = momentum_increment + move_per_secound
                market_price = total_move + market_price

            mpl_secs.append(x+1)
            mpl_Avg.append(round(market_momentum_price,2))
            mpl_tp.append(take_profit_amount)
            mpl_sl.append(stop_loss_amount)
            mpl_price.append(round(market_price,2))


            if market_price >= take_profit_amount and trade_open == True:
                gain = carried_balance * take_profit
                carried_balance += gain
                fee = carried_balance * trading_fee_rate
                carried_balance -= fee
                win += 1
                time_in_win_trade.append(x+1)
                profit += gain
                total_fees += fee
                trade_open = False



            if market_price <= stop_loss_amount and trade_open == True:
                loss = carried_balance * stop_loss
                carried_balance += loss
                fee = carried_balance * trading_fee_rate
                carried_balance -= fee
                carried_price = market_price
                losses += 1
                time_in_loss_trade.append(x+1)
                profit += loss
                total_fees += fee
                trade_open = False


            if x == (seconds -1) and trade_open == True:
                fee = carried_balance * trading_fee_rate
                carried_price = market_price
                timed_out += 1
                total_fees += fee

                change_percentage = market_price / crypo_price
                bal_gain = opening_steak * change_percentage

                change = (market_price - carried_price)/carried_price*100

                trade_profit = bal_gain - opening_steak
                trade_open = False

            carried_price = market_price


        percentage = ((trade_profit) / opening_steak)* 100
        each_trade = {
        'Second': mpl_secs,
        'Avg_price' : mpl_Avg,
        'tp': mpl_tp,
        'sl': mpl_sl,
        'Price': mpl_price
        }
        price_moves = each_trade

        number_of_trades

        if win > 0:
            win_average = Average(time_in_win_trade)
        if losses > 0:
            loss_average = Average(time_in_loss_trade)

        # sum all the entries time_into_trade and dived byt len so as to work out verage tim into trade we are stoped out

        percentage = ((profit - total_fees) / opening_steak)* 100
        win_precentage =  (win / number_of_trades)*100


    each_trade = {  'cash money' : profit,
                    'volatility': ATR,
                    'take profit':take_profit,
                    'stopLoss': stop_loss,
                    'market momentum' : market_momentum,
                    'Profit': round(percentage,1),
                    'Wins:': win,
                    'timed out trades': timed_out,
                    'losses': losses,
                     }

    trades_list.append(each_trade)

#saving the data
    trade_result = json.dumps(trades_list, indent = 2)
    with open('data/trades.json', 'w') as f:
        f.write(trade_result)

# Closing file
f.close()


#specify that all columns should be shown
pd.set_option('max_columns', None)

data = pd.DataFrame(json.load(open("data/trades.json")))

df = data.nlargest(20,'Profit')


trade_width = df['take profit'] - df['stopLoss']

df['trade_width'] = trade_width

#df.sort_values(by=['Profit'])
print(df)


df2 = df["volatility"].mean(),df["take profit"].mean(),df["stopLoss"].mean(),df["market momentum"].mean()
print(df2)
This applications seek to identify which permutations offer the highest probability of success when trading.

First take a look at & run the single_trade_graph.py file. This will produce a visual representation of how the simulator can recreate trading conditions. This intention is to create a realist trading simulation that replicates an assets in a an upward momentum.

The Theory is that due to momentum bias, which everway thr market is going people believe it will continue. The goal therefore is to identify coins in an upward momentum and try to scalp just a small profit on a regular basis.

The goal of this simulator is to help identify which permutaion of parameters gives the best probability of success for this trading strategy.

The Law of Diminishing returns is a bell curve you can envisage that for example as you start with a small amount of volatility you don't get much opportunity for a success full trade. As the amount increase the opportunites increase but there soon becomes point of diminishing returns.

Now this is true for each of the 5 parameters we are exploring:




| PARAMETERS        | TOO LOW         | TOO HIGH.     |
| --------------- |:-----------------------------------:| --------------------------:|
| Volatility      | it will take ages to fill the order | becomes too unpredicatble |
| Stop Loss       | you get whiped out at the slightest blip in price      |  the sum cost of your losses adds up quickly |
| Take Profit     | fee's will eat up most of our profit      |    it will take too long to fill and the moment may be lost and the trade may turn against too frequently. |
| Market momentum | we end up trading all the time      |    the trades are too far n few in between |
| Time in Trade   | not enough time to till the order   |    you capital is stuck in one trade and you may miss too many better trade |
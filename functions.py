import random

def snap_to_moving_average(time_in_trade):
    # This function produces a list of incremented times that determines when the price will snap back to the average.
    occurrences = []
    seconds = 0
    for n in range(100):
        time = random.randint(20, 101)
        seconds += time
        if seconds >= time_in_trade + 100:
            break
        occurrences.append(seconds)
    return(occurrences)

def next_move(volatility):
    # The function generates unpreditable volatility as you would get in a real market but is limited up to the prescribed volatility value'
    big_random = random.randint(0, volatility)
    decimal_random = random.randint(0, 9)
    decimal = decimal_random / 10
    change = big_random + decimal
    fliper = random.randint(-1, 1)
    move = (change * fliper)/100
    move = move / 6
    return(move)

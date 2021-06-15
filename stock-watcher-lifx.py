from time import sleep
import atexit

import ally

from lights import charizard
from colors import DIM_RED, DIM_BLUE, DIM_CYAN, DIM_GREEN, MID_RED

SYMBOL = 'vmeo'


def update_light(error=False, bid_price=0, open_price=0):
    if error:
        charizard.set_color(DIM_RED)
        charizard.set_waveform(is_transient=False, color=MID_RED, period=1000, cycles=5, duty_cycle=1,
                               waveform=1)
        return

    if bid_price == 0:  # outside market hours
        charizard.set_color(DIM_CYAN)
        return

    if bid_price > open_price:
        charizard.set_color(DIM_GREEN)
    elif bid_price < open_price:
        charizard.set_color(DIM_RED)
    else:
        charizard.set_color(DIM_BLUE)


def main():
    a = ally.Ally()

    charizard.set_power('on')
    charizard.set_color(DIM_CYAN)

    quotes = a.quote(symbols=SYMBOL, fields=['opn', 'bid'], dataframe=False)

    open_price = float(quotes[0]['opn'])
    bid_price = float(quotes[0]['bid'])

    update_light(bid_price=bid_price, open_price=open_price)

    try:
        for quote in a.stream(SYMBOL):
            bid_price = float(quote['bid'])
            update_light(bid_price=bid_price, open_price=open_price)
    except:
        print('there was an error')
        update_light(error=True)
        print('sleeping...')
        sleep(5)
        raise


if __name__ == '__main__':
    atexit.register(lambda: charizard.set_power('off'))
    main()

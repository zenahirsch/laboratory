#!/usr/bin/python3

import atexit
import os
from datetime import datetime
from time import sleep

import requests
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from requests.exceptions import HTTPError

from lights import blastoise

CRON_INTERVAL_SEC = 300  # How often to run covid check in background

scheduler = BackgroundScheduler()


def get_covid_data(yesterday=False, two_days_ago=False):
    payload = {
        'yesterday': 'true' if yesterday else 'false',
        'twoDaysAgo': 'true' if two_days_ago else 'false',
    }

    r = requests.get('https://disease.sh/v3/covid-19/all', params=payload)
    data = r.json()
    return data


def main():
    yesterday_data = get_covid_data(yesterday=True)
    two_days_ago_data = get_covid_data(two_days_ago=True)
    yesterday_cases = yesterday_data['todayCases']
    two_days_ago_cases = two_days_ago_data['todayCases']

    print('yesterday:', yesterday_cases)
    print('two days ago:', two_days_ago_cases)

    if yesterday_cases < two_days_ago_cases:
        print('green')
        blastoise.set_hue(16173, 1000)
    elif yesterday_cases > two_days_ago_cases:
        print('red')
        blastoise.set_hue(65535, 1000)
    else:
        print('blue')
        blastoise.set_hue(29814, 1000)

blastoise.set_power('on')
blastoise.set_brightness(3000)
blastoise.set_saturation(55000)

scheduler.add_job(func=main, trigger='interval', seconds=CRON_INTERVAL_SEC, coalesce=True,
                  next_run_time=datetime.now(), id='main')
scheduler.start()

# when app stops running
atexit.register(lambda: scheduler.shutdown())
atexit.register(lambda: blastoise.set_power('off'))

app = Flask(__name__)


@app.route('/laboratory/covid', methods=['POST'])
def respond():
    return {
        'message': 'This will do something with the light!'
    }


if __name__ == "__main__":
    app.run(port=5001)

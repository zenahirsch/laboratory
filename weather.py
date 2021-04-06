#!/usr/bin/python3

import atexit
import os
from datetime import datetime
from time import sleep

import requests
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from lifxlan import Light
from requests.exceptions import HTTPError

LOCATION = '606b30f5fa596500089fcbff'  # Home
CRON_INTERVAL_SEC = 120  # How often to run check_weather in background
TIMESTEPS = '1h'  # timeline interval
PRECIPITATION_PROBABILITY_THRESHOLD = 40  # Percent change of rain must be above this to notify

COLOR_COOLER = [29814, 65535, 3000, 3500]
COLOR_WARMER = [58275, 65535, 3000, 3500]
COLOR_SAME = [16173, 65535, 3000, 3500]
COLOR_RAIN = [43634, 65535, 3000, 3500]
COLOR_ERROR = [65535, 65535, 3000, 3500]

bulbasaur = Light('d0:73:d5:65:ac:9b', '192.168.86.20')
scheduler = BackgroundScheduler()


def get_weather_data(location, fields, units='imperial'):
    url = 'https://api.tomorrow.io/v4/timelines'

    querystring = {
        'location': location,
        'fields': fields,
        'units': units,
        'timesteps': TIMESTEPS,
        'apikey': os.getenv('CLIMACELL_SECRET_KEY'),
    }

    r = requests.request('GET', url, params=querystring)
    r.raise_for_status()

    return r.json()


def update_light(now_temp, next_temp, precipitation_probability):
    print(f"Updating light: {now_temp} | {next_temp} | {precipitation_probability}")
    likely_to_rain = precipitation_probability > PRECIPITATION_PROBABILITY_THRESHOLD

    bulbasaur.set_power('on')

    if now_temp > next_temp:
        print('Getting cooler')
        bulbasaur.set_color(COLOR_COOLER)
    elif now_temp < next_temp:
        print('Getting warmer')
        bulbasaur.set_color(COLOR_WARMER)
    else:
        print('Staying the same')
        bulbasaur.set_color(COLOR_SAME)

    sleep(1)

    if likely_to_rain:
        print('Likely to rain')
        bulbasaur.set_waveform(is_transient=True, color=COLOR_RAIN, period=1000, cycles=CRON_INTERVAL_SEC, duty_cycle=1,
                               waveform=1)


def check_weather():
    print('Checking weather...')
    try:
        weather = get_weather_data(location=LOCATION, fields=['temperature', 'precipitationProbability'])
    except HTTPError as e:
        status_code = e.response.status_code
        headers = e.response.headers

        bulbasaur.set_power('on')
        bulbasaur.set_color(COLOR_ERROR)

        if status_code == 429:
            retry_after = int(headers['retry-after'])
            print(f"Rate limited for {retry_after} seconds...")
            scheduler.pause_job('check_weather')
            sleep(retry_after)
            scheduler.resume_job('check_weather')

        raise

    timelines = weather['data']['timelines']
    intervals = timelines[0]['intervals']
    now = intervals[0]['values']
    next = intervals[1]['values']

    update_light(round(now['temperature']), round(next['temperature']), next['precipitationProbability'])


scheduler.add_job(func=check_weather, trigger='interval', seconds=CRON_INTERVAL_SEC, coalesce=True,
                  next_run_time=datetime.now(), id='check_weather')
scheduler.start()

# when app stops running
atexit.register(lambda: scheduler.shutdown())
atexit.register(lambda: bulbasaur.set_power('off'))

app = Flask(__name__)


@app.route('/laboratory/weather', methods=['POST'])
def respond():
    return {
        'message': 'This will do something with the light!'
    }


if __name__ == "__main__":
    app.run()

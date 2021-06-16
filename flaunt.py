#!/usr/bin/python3

import atexit
from datetime import datetime
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

from lights import laboratory
from colors import MID_RAINBOW

CRON_INTERVAL_SEC = 3600  # How often to run flaunt in background

app = Flask(__name__)

laboratory.set_power('on')

scheduler = BackgroundScheduler()

# when app stops running
atexit.register(lambda: scheduler.shutdown())


@app.route('/flaunt', methods=['POST'])
def flaunt():
    for color in MID_RAINBOW:
        laboratory.set_color(color, 1000)
        sleep(2)

    return 'flaunted'


scheduler.add_job(func=flaunt, trigger='interval', seconds=CRON_INTERVAL_SEC, coalesce=True,
                  next_run_time=datetime.now(), id='main')
scheduler.start()

if __name__ == "__main__":
    app.run(port=5002)

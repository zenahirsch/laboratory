import atexit
from datetime import datetime, date

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

from colors import MUTED_BLUE, MUTED_ORANGE, DIM_BLUE, DIM_ORANGE
from lights import pikachu

scheduler = BackgroundScheduler()


def blink_light(color):
    pikachu.set_waveform(is_transient=True, color=color, period=2000, cycles=3, duty_cycle=1, waveform=4)

def set_color(color):
    pikachu.set_color(color)

def update_light(current_hour, is_recycling_week=False, is_pickup_day=False, is_day_before_pickup=False):
    print(f"Updating light")

    if is_recycling_week:
        set_color(MUTED_BLUE)
        strobe_color = DIM_BLUE
    else:
        set_color(MUTED_ORANGE)
        strobe_color = DIM_ORANGE

    if is_pickup_day and current_hour < 12:  # blink light in the morning of pickup day
        blink_light(strobe_color)

    if is_day_before_pickup and current_hour > 18:  # blink light in the evening of day before pickup
        blink_light(strobe_color)


def main():
    current_hour = datetime.now().hour
    today = date.today()
    weekday = today.weekday()
    week_num = today.isocalendar().week
    is_recycling_week = week_num % 2 == 0  # even weeks are recycling weeks
    is_pickup_day = weekday == 0  # mondays are pickup days
    is_day_before_pickup = weekday == 6  # sunday is day before pickup day
    print(f"Hour: {current_hour}. Week num: {week_num}. Recycling: {is_recycling_week}. Pickup day: {is_pickup_day}")
    update_light(is_recycling_week=is_recycling_week, is_pickup_day=is_pickup_day,
                 is_day_before_pickup=is_day_before_pickup, current_hour=current_hour)


pikachu.set_power('on')

# Cron runs every five minutes
scheduler.add_job(func=main, trigger='cron', minute='*/5', coalesce=True, next_run_time=datetime.now(),
                  timezone='America/Detroit', id='check_garbage')

scheduler.start()

# when app stops running
atexit.register(lambda: scheduler.shutdown())
atexit.register(lambda: pikachu.set_power('off'))

app = Flask(__name__)


@app.route('/laboratory/garbage', methods=['POST'])
def respond():
    return {
        'message': 'This will do something with the light!'
    }


if __name__ == "__main__":
    app.run(port=5003)

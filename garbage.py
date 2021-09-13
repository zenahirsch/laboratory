import atexit
from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from colors import MUTED_BLUE, MUTED_ORANGE, DIM_BLUE, DIM_ORANGE
from lights import pikachu

scheduler = BackgroundScheduler()


def update_light(is_recycling_week=False, is_pickup_day=False):
    print(f"Updating light")

    if is_recycling_week:
        pikachu.set_color(MUTED_BLUE)
        strobe_color = DIM_BLUE
    else:
        pikachu.set_color(MUTED_ORANGE)
        strobe_color = DIM_ORANGE

    if is_pickup_day:
        # strobe light for 12 hours if it's a pickup day
        pikachu.set_waveform(is_transient=True, color=strobe_color, period=2000, cycles=21600, duty_cycle=1, waveform=4)


def main():
    today = date.today()
    week_num = today.isocalendar().week
    is_recycling_week = week_num % 2 != 0  # odd weeks are recycling weeks
    is_pickup_day = today.weekday() == 0  # mondays are pickup days
    print(f"This is week {week_num}. Recycling: {is_recycling_week}. Pickup day: {is_pickup_day}")
    update_light(is_recycling_week=is_recycling_week, is_pickup_day=is_pickup_day)


pikachu.set_power('on')

scheduler.add_job(func=main, trigger='cron', day_of_week='*', hour=0, minute=0, coalesce=True,
                  next_run_time=datetime.now(), timezone='America/Detroit', id='check_garbage')

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

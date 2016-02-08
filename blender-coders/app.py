import datetime
from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__)

app.config.update(dict(
    PREFERRED_URL_SCHEME='https',
    DEBUG=False
))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/meeting/widget")
def meeting_widget():
    return render_template('widgets/index.html')

@app.route("/meeting-times.json")
def meeting_times():
    DISPLAY_NUM = 1
    meeting_times = []

    # Meeting generation script originally provided by Campbell Barton
    def generate_meetings(
            t_start,
            days=(9, 18, 27),
            hrs=(10, 10, 10),  # hours GMT
            cities=("America/Los_Angeles", "Europe/Amsterdam", "Australia/Sydney"),
            ):
        year = t_start.year
        while True:
            for month in range(t_start.month, 13):
                for day, hr, city in zip(days, hrs, cities):
                    t_test = datetime.datetime(year=t_start.year, month=month,
                        day=day, hour=hr)
                    if t_test >= t_start:
                        yield t_test, city
            t_start = datetime.datetime(year=t_start.year + 1, month=1, day=1)

    # one day less to account for timezone of system
    t = datetime.datetime.now() - datetime.timedelta(days=1)
    t_start = datetime.datetime(year=t.year, month=t.month, day=t.day)

    for i, (t_local, city) in enumerate(generate_meetings(t_start)):
        meeting_times.append(dict(
            local_time="%04d-%02d-%02dT10:00:00" % (t_local.year, t_local.month, t_local.day),
            days_remaining=max(0, (t_local - t_start).days),
            city=city))
        # print("%04d-%02d-%02d, %02d%s %s local time, (days remaining: %02d), (%04d-%02d-%02d, %02d:%02d UTC)" %
        #     (t_local.year, t_local.month, t_local.day, t_local.hour, t_local.strftime("%p"), city,
        #     max(0, (t_local - t_start).days),
        #     t_utc.year, t_utc.month, t_utc.day, t_utc.hour, t_utc.minute,
        #     ))
        if i > DISPLAY_NUM:
            break

    return jsonify(meeting_times=meeting_times)

if __name__ == "__main__":
    app.run(host='0.0.0.0')


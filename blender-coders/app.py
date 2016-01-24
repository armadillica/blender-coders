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

    # Meeting generation script provided by Campbell Barton
    def generate_meetings(
            t_start,
            days=(9, 18, 27),
            hrs=(18, 9, 23),  # hours GMT
            cities=("America/Los_Angeles", "Europe/Amsterdam", "Australia/Sydney"),
            ):

        year = t_start.year
        while True:
            t_start = datetime.datetime(year=year, month=t_start.month,
                day=t_start.day)
            for month in range(1, 13):
                for day, hr, city in zip(days, hrs, cities):
                    t_test = datetime.datetime(year=t_start.year, month=month,
                        day=day, hour=hr)
                    if t_test >= t_start:
                        yield t_test, city
            year += 1


    # one day less to account for timezone of system
    t = datetime.datetime.now() - datetime.timedelta(days=1)
    t_start = datetime.datetime(year=t.year, month=t.month, day=t.day)

    for i, (t, city) in enumerate(generate_meetings(t_start)):
        # print("%04d-%02d-%02d, %02d GMT, (days remaining: %02d), 10am %s local time" %
        #       (t.year, t.month, t.day, t.hour, max(0, (t - t_start).days), city))
        meeting_times.append(dict(
            gmt_time=t.isoformat() + 'Z',
            days_remaining=max(0, (t - t_start).days),
            city=city))
        if i > DISPLAY_NUM:
            break

    return jsonify(meeting_times=meeting_times)

if __name__ == "__main__":
    app.run(host='0.0.0.0')


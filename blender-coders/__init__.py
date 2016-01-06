import datetime
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def meeting_times():
    DISPLAY_NUM = 4
    meeting_times = []

    # Meeting generation script provided by Campbell Barton
    def generate_meetings(
            t_start,
            days=(9, 18, 27),
            hrs=(18, 9, 23),  # hours GMT
            cities=("Los Angeles", "Amsterdam", "Sydney"),
            ):

        year = t_start.year
        while True:
            t_start = datetime.datetime(year=year, month=1, day=1)
            for month in range(1, 13):
                for day, hr, city in zip(days, hrs, cities):
                    t_test = datetime.datetime(year=t_start.year, month=month, day=day, hour=hr)
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
            gmt_time=t,
            days_remaining=max(0, (t - t_start).days),
            city=city))
        if i > DISPLAY_NUM:
            break

    return jsonify(meeting_times=meeting_times)

if __name__ == "__main__":
    app.run(host='0.0.0.0')


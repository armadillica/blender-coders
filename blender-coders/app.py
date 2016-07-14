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
    meeting_times = []

    def get_sunday_and_days_remaining():
        days_remaining = 0
        d = datetime.date.today()
        while d.weekday() != 6:
            days_remaining += 1
            d += datetime.timedelta(1)
        return {
            'city': 'Europe/Amsterdam',
            'days_remaining': days_remaining,
            'local_time': d}


    def get_day_in_following_weeks(d, weeks=2):
        days_remaining = d['days_remaining']
        sunday = d['local_time']
        for i in range(weeks):
            days_remaining += 7
            sunday += datetime.timedelta(7)
            meeting_times.append({
                'city': d['city'],
                'days_remaining': days_remaining,
                'local_time': sunday
                })


    def format_dates(meeting_times):
        for m in meeting_times:
            m['local_time'] = "%04d-%02d-%02dT16:00:00" % (
                m['local_time'].year, m['local_time'].month, m['local_time'].day)


    first_sunday = get_sunday_and_days_remaining()
    meeting_times.append(first_sunday)
    get_day_in_following_weeks(first_sunday)
    format_dates(meeting_times)
    return jsonify(meeting_times=meeting_times)


if __name__ == "__main__":
    app.run(host='0.0.0.0')


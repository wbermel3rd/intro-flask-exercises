from flask import Flask, render_template, url_for
import datetime
import calendar
import pytz


app = Flask(__name__)


@app.route('/')
def index():
    current_time = datetime.datetime.now(pytz.timezone('US/Eastern'))
    ctime = current_time.strftime("%A, %B %d %Y %H:%M:%S")
    return render_template('index.html', ctime=ctime)

if __name__ == "__main__":
    app.run()
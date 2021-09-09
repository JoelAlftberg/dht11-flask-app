from flask import Flask, render_template, request
import psycopg2
import db.sensordb 
import re


app = Flask(__name__)


@app.route("/")
def main():
    current_temperature = db.sensordb.sql_current('celsius')
    average_today = db.sensordb.sql_select_view('celsius_daily_average')
    average_weekly = db.sensordb.sql_select_view('celsius_weekly_average')
    average_monthly = db.sensordb.sql_select_view('celsius_monthly_average')
    return render_template('index.html', temperature_now=current_temperature[0], temperature_today=round(average_today[0], 1), temperature_monthly=round(average_monthly[0], 1), temperature_weekly=round(average_weekly[0], 1))

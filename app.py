from flask import Flask, render_template, request
import psycopg2
import db.sensordb 
import re


app = Flask(__name__)


@app.route("/")
def main():
    current_temperature = db.sensordb.sql_current('celsius')
    return render_template('index.html', temperature=current_temperature[0])

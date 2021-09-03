from flask import Flask
import psycopg2
import db.sensordb


app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>Main page<h1><br><h3>{{ }}</h3>"

# RaspberryPi - Weather station w/ Flask
A visualizer/dashboard for showing temperature and humidity readings from the DHT11 Adafruit Module.
Built using Flask for the front-end and running Python and Postgres in the backend.

## Hardware
- Raspberry Pi Zero 
- DHT11 Adafruit Module

## Dependencies
- Flask
- Adafruit_DHT pip3-module
- Psycopg2 pip3-module

## Setup
The script in db/db_setup.sh installs the postgres database, as of now it does not set up the views that I'm using to generate the daily, weekly and monthly values.
The views can be created like this in psql:
```
CREATE MATERIALIZED VIEW celsius_daily_average AS
SELECT avg(celsius) FROM temperature
WHERE date BETWEEN (SELECT NOW() - interval '1 day') AND NOW()
```
The psql_refresh.sql script is meant to be put in crontab and run on an hourly basis or so.
It can be ran like this for example (every 30 minutes)\
`*/30 * * * * psql -d sensordb -f /opt/dht11-flask-app/psql_refresh.sql`

## TODO
- [X] Add SQL-queries for averages
- [ ] Real-time graphing
- [ ] Quote of the Day
- [X] Systemd service for sensor
- [X] Display celsius values on dashboard

## WIP
- [ ] Service for Flask
- [ ] Handle unexpected shutdown
- [ ] Display humidity values on dashboard
- [ ] HTML/CSS - make it pretty


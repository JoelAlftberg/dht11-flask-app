# RaspberryPi - Weather station w/ Flask
A visualizer/dashboard for showing temperature and humidity readings from the DHT11 Adafruit Module.
Built using Flask for the front-end and running Python and Postgres in the backend.

## Hardware
- Raspberry Pi Zero 
- DHT11 Adafruit Module

## Setup
The script in db/install.sh installs the postgres database, as of now it does not set up the views that I'm using to generate the daily, weekly and monthly values.
The views can be created like this in psql:
```
CREATE MATERIALIZED VIEW celsius_daily_average AS
SELECT avg(celsius) FROM temperature
WHERE date BETWEEN (SELECT NOW() - interval '1 day') AND NOW()
```
The psql_refresh.sh script is meant to be put in crontab and run on an hourly basis or so.

## TODO
- [X] Add SQL-queries for averages
- [ ] Real-time graphing
- [ ] Quote of the Day
- [ ] HTML/CSS - make it pretty

## WIP
- [ ] Services for flask and sensor
- [ ] Handle unexpected shutdown
- [X] Display celsius values on dashboard
- [ ] Display humidity values on dashboard


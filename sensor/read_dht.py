#!/usr/bin/python3
import time
import psycopg2
import Adafruit_DHT

dht_gpio = 4

conn = psycopg2.connect(database="sensordb", user="pi", password="teampurple", host="127.0.0.1", port="5432")

cursor = conn.cursor()

sensor = Adafruit_DHT.DHT11

print("starting sensor...")

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, dht_gpio) 
    

    sql = f'''INSERT INTO temperature (date, celsius, humidity) VALUES ((SELECT NOW()), {temperature}, {humidity});'''
    
    cursor.execute(sql)

    conn.commit()

    if humidity != None and temperature != None:
        pass
    else:
        print('Error, couldn\'t read... waiting 5 seconds')

    time.sleep(5)

import psycopg2
from datetime import datetime

connection = psycopg2.connect(user='pi',password='teampurple', host='127.0.0.1', port='5432', database='sensordb')

cursor = connection.cursor()

def average_7days():

    cursor.execute(f"SELECT avg(celsius) FROM temperature WHERE date BETWEEN (SELECT NOW()  - interval '7 days') AND NOW()")
    result = cursor.fetchone()
    
    return result

print(average_7days())

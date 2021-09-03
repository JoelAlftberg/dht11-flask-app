import psycopg2

connection = psycopg2.connect(database="sensordb", user="pi", password="teampurple", host="127.0.0.1", port="5432")

cursor = connection.cursor()

def sql_average(column, interval):
    
    cursor.execute(f"SELECT avg({column}) FROM temperature WHERE date BETWEEN (SELECT NOW() - interval '{interval}') AND NOW()")
    result = cursor.fetchone()
    print(result)
    return result

def sql_current(column):

    cursor.execute(f"SELECT {column} FROM temperature WHERE date BETWEEN (SELECT NOW() - interval '10 seconds') AND NOW()")
    result = cursor.fetchone()

    return result


### EXAMPLE FUNCTION CALL ###

#sql_average('celsius', '7 days')

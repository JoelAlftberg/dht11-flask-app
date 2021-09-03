def sql_average(column, interval):
    
    cursor.execute(f"SELECT avg({column}) FROM temperature WHERE date BETWEEN (SELECT NOW() - interval '{interval}') AND NOW()")
    result = cursor.fetchone()

    return result

def sql_current(column):

    cursor.execute(f"SELECT {column} FROM temperature WHERE date = NOW()")
    result = cursor.fetchone()

    return result


### EXAMPLE FUNCTION CALL ###

#print(sql_average('celsius', '7 days'))


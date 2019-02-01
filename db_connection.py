import psycopg2
import csv

with open('db_con_params.csv', 'r') as file_in:
    db_file = csv.reader(file_in, delimiter=',')
    con_string = ""
    for param in db_file:
        con_string += param[0] + '=' + param[1] + ' '

con = psycopg2.connect(con_string)
cur = con.cursor()
cur.execute("select version()")
print(cur.fetchall())
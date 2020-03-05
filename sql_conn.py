import mysql.connector
import os
import sys

from mysql.connector import Error, MySQLConnection
from sql_conn_dbconfig import read_db_config

"""
Establishes connection with MySQL server then
runs a SQL command to retrieve requested info
"""

def connector():
    try:
        # call read_db_config() to initiaite a connection with database
        # using provided .ini file
        db_config = read_db_config()
        conn = None
        conn = MySQLConnection(**db_config)
        
        if conn.is_connected():
            try:
                # open file to read necessary SQL commands
                # replace 'sql.txt' with whatever you want to name your file that holds your SQL query 
                f = open(os.path.join(sys.path[0], 'sql.txt'), 'r')
                if f.mode == 'r':
                    sql = f.read()
            except FileNotFoundError as ffe:
                print(ffe)
                sys.exit(1)
            
            # run SQL commands and retrieve requested info
            # in sql.txt, if there are multiple %s, need two 'chip_ID's
            query = sql
            cursor = conn.cursor()
            cursor.execute(query, )
            data = cursor.fetchone()

            # output_vars is the result of your SQL query.
            # dictionary key is your variable name to be used in an external Python program.
            # dictionary value holds the data retrieved by your SQL query in the SELECT statement.
            # data retrieved with the SELECT statement will be a key, value pair in a dictionary.
            output_vars = {
                    'var_1': data[0],
                    'var_2': data[1],
                    'var_3': data[2],
                    'var_4': data[3]
                    }
            return output_vars

        else:
            print('Connection failed')
    except Error as error:
        print(error)
    finally:
        # close MySQL database connection when data is retrieved
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    connector()
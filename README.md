# Python-to-MySQL-Database-Connector

### <u>Purpose</u>
The Connector serves as a plug-and-play utility to connect a Python program to a MySQL database. SQL queries can be executed through the main Python program to retrieve data from the database. The retrieved data can then be saved as Python variables to be used. It provides a way to retrieve data real-time and immeditely implement them using a Python program.

### <u>Getting Started</u>
This program requires a Python 3 environment.

You will also need access to a MySQL database and the driver 'MYSQL Connector'.
The 'MYSQL Connector' driver can be downloaded [here](https://dev.mysql.com/downloads/connector/python/).

Once downloaded, the driver can be installed by running the following commands from your terminal:
```
python -m pip install mysql-connector
```

In the **config.ini** file, you will need to populate the variables with your MySQL database information.

Place your SQL query in the **sql.txt** file. This will be parsed and used to execute your SQL commands. This file can be named anything, but you must also change the file name argument in line 25 in **sql_conn.py**.

### <u>Features</u>
The retrieved data of your SQL query will be stored as a dictionary (line 43 in **sql_conn.py**). In **sql_conn.py** the example dictionary is as follows:
```
output_vars = {
  'var_1': data[0],
  'var_2': data[1],
  'var_3': data[2],
  'var_4': data[3]
}
```
You may name the keys to fit your program's requirements. The values are stored in the order of your SELECT statement in your SQL query and may contain more or less key: value pairs than what is shown above. For instance, if your SELECT statement was as follows:
```
SELECT apple_name, apple_color, apple_size
```
you could structure your dictionary as such:
```
output_vars = {
  'Apple Name': data[0],
  'Apple Color': data[1],
  'Apple Size': data[2]
```
so that the resulting dictionary would be as follows (modified to serve this example):
```
apple_details = {
  'Apple Name': 'Red Delicious',
  'Apple Color': 'Red',
  'Apple Size': 'Medium'
}
```
The resulting dictionary can then be used as a standard Python dictionary:
```
for apple, description in apple_details.items():
     print('{}: {}'.format(apple, description)

> Apple Name: Red Delicious
> Apple Color: Red
> Apple Size: Medium
```

#coding:utf-8

import mysql.connector
from mysql.connector import Error

# 连接mysql
def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print('Connection to MySQL DB successful')
    except Error as e:
        print(f"The error '{e}' occurred.")

    return connection

# 连接
connection = create_connection("localhost", 'root', "12345678")


# 创建数据库
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database create successfully")
    except Error as e:
        print(f"The error '{e}' occurred.")

# 创建
create_database_query = "CREATE DATABASE readers"
create_database(connection, create_database_query)

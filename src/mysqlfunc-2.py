#coding:utf-8

import mysql.connector
from mysql.connector import Error

# 连接mysql
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print('Connection to MySQL DB successful')
    except Error as e:
        print(f"The error '{e}' occurred.")

    return connection

# 连接
connection = create_connection("localhost", 'root', "12345678", 'readers')

# 建表，即：写
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred.")

# 查询函数，即：读
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred.")

# 建表
create_users_table = """
CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT,
    name TEXT NOT NULL,
    age INT,
    gender TEXT,
    PRIMARY KEY (id)
) ENGINE = InnoDB
"""
#execute_query(connection, create_users_table)


# 插入记录，注意：`users`, `name`, `age`, `gender`，不是引号包裹，是键盘左上角的撇号
insert_users = """
INSERT INTO 
`users` (`name`, `age`, `gender`)
VALUES
('zhagnsan',23,'male'),
('lisi',24,'female'),
('wangwu',25,'male');
"""
#execute_query(connection, insert_users)

# 查询
select_users = "SELECT * FROM users"
users = execute_read_query(connection, select_users)
for user in users:
   print(user)
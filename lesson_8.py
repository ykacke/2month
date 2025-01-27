import sqlite3



def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(connection, create_table_sql):
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


def insert_employee(connection, employee):
    sql = '''INSERT INTO employees
    (full_name, salary, hobby, birth_date, is_married)
    VALUES (?, ?, ?, ?, ?) '''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, employee)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_employee(db_name, employee):
    sql = '''UPDATE employees SET salary = ?, is_married = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, employee)
    except sqlite3.Error as e:
        print(e)


def delete_employee(db_name, id):
    sql = '''DELETE FROM employees WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
    except sqlite3.Error as e:
        print(e)


def select_all_employees(db_name):
    sql = '''SELECT * FROM employees'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def select_employees_by_salary(db_name, salary_limit):
    sql = '''SELECT * FROM employees WHERE salary >= ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (salary_limit,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


sql_to_create_employees_table = '''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(200) NOT NULL,
    salary FLOAT(10,2) NOT NULL DEFAULT 0.0,
    hobby TEXT DEFAULT NULL,
    birth_date DATE NOT NULL,
    is_married BOOLEAN DEFAULT FALSE
)
'''


my_connection = create_connection('''8hw.db''')
if my_connection is not None:

    print('Successfully connected to database')
    create_table(my_connection, sql_to_create_employees_table)
#     insert_employee(my_connection,
#                     ('Jibek Manasova', 2400.5, 'Programming', '2000-01-25', False))
#     my_connection.close()
#
# # Открытие соединения и вставка данных
# with sqlite3.connect(database_name) as my_connection:
#     insert_employee(my_connection, ('Jibek Manasova', 2400.5, 'Programming', '2000-01-25', False))
#     insert_employee(my_connection, ('Mark Daniels', 1500.0, 'Football', '1999-01-02', False))
#     insert_employee(my_connection, ('Alex Brilliant', 2300.5, None, '1989-12-31', True))
#     insert_employee(my_connection, ('Diana Julls', 1800.0, 'Programming', '2005-01-22', True))
#     insert_employee(my_connection, ('Michael Corse', 1800.0, 'Football', '2001-09-17', True))
#     insert_employee(my_connection, ('Jack Moris', 2100.2, 'Programming', '2001-07-12', True))
#     insert_employee(my_connection, ('Viola Manilson', 1750.82, None, '1991-03-01', False))
#     insert_employee(my_connection, ('Joanna Moris', 1000.0, 'Football', '2004-04-13', False))
#     insert_employee(my_connection, ('Peter Parker', 2000.0, 'Programming', '2002-11-28', False))
#     insert_employee(my_connection, ('Paula Parkerson', 800.09, None, '2001-11-28', True))
#     insert_employee(my_connection, ('George Newel', 1320.0, 'Programming', '1981-01-24', True))
#     insert_employee(my_connection, ('Miranda Alistoun', 2500.55, 'Football', '1997-12-22', False))
#     insert_employee(my_connection, ('Valeria Hillton', 2000, 'Football', '1977-10-28', True))
#     insert_employee(my_connection, ('Jannet Miler', 2100.9, 'Programming', '1997-02-02', True))
#     insert_employee(my_connection, ('William Tokenson', 1500, None, '1999-12-12', False))
#     insert_employee(my_connection, ('Shanty Morani', 1200.6, None, '1989-08-13', False))
#     insert_employee(my_connection, ('Fiona Giordano', 900.12, 'Football', '1977-01-15', True))
#
# update_employee(database_name, (2500, True, 2))
# delete_employee(database_name, 2)
# select_all_employees(database_name)
# select_employees_by_salary(database_name, 2300)




# import sqlite3
#
# connection = sqlite3.connect('vse.db')
#
# def create_connection(db_name):
#     connection = None
#     try:
#         connection = sqlite3.connect(db_name)
#     except sqlite3.Error as e:
#         print(e)
#     return connection
#
# def create_table(connection, create_table_sql):
#     try:
#         cursor = connection.cursor()
#         cursor.execute(create_table_sql)
#     except sqlite3.Error as e:
#         print(e)
#
# def insert_employee(connection, employee):
#     try:
#         sql = '''
#         INSERT INTO employees (full_name, salary, hobby, birth_date, is_married)
#         VALUES (?, ?, ?, ?, ?)
#         '''
#         cursor = connection.cursor()
#         cursor.execute(sql, employee)
#         connection.commit()
#     except sqlite3.Error as e:
#         print(e)
#
# def update_employee(db_vse, employee):
#     sql = '''UPDATE employees SET salary = ?, is_married = ? WHERE id = ?'''
#     try:
#         with sqlite3.connect(db_vse) as connection:
#             cursor = connection.cursor()
#             cursor.execute(sql, employee)
#     except sqlite3.Error as e:
#         print(e)
#
# def delete_employee(db_vse, id):
#     sql = '''DELETE FROM employees WHERE id = ?'''
#     try:
#         with sqlite3.connect(db_vse) as connection:
#             cursor = connection.cursor()
#             cursor.execute(sql, (id,))
#     except sqlite3.Error as e:
#         print(e)
#
# def select_all_employees(db_vse):
#     sql = '''SELECT * FROM employees'''
#     try:
#         with sqlite3.connect(db_vse) as connection:
#             cursor = connection.cursor()
#             cursor.execute(sql)
#             rows = cursor.fetchall()
#             for row in rows:
#                 print(row)
#     except sqlite3.Error as e:
#         print(e)
#
# def select_employees_by_salary(db_vse, salary_limit):
#     sql = '''SELECT * FROM employees WHERE salary >= ?'''
#     try:
#         with sqlite3.connect(db_vse) as connection:
#             cursor = connection.cursor()
#             cursor.execute(sql, (salary_limit,))
#             rows = cursor.fetchall()
#             for row in rows:
#                 print(row)
#     except sqlite3.Error as e:
#         print(e)
#
# sql_to_create_employees_table = '''
# CREATE TABLE IF NOT EXISTS employees (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     full_name VARCHAR(200) NOT NULL,
#     salary FLOAT(10,2) NOT NULL DEFAULT 0.0,
#     hobby TEXT DEFAULT NULL,
#     birth_date DATE NOT NULL,
#     is_married BOOLEAN DEFAULT FALSE
# )
# '''
#
# database_name = 'vse.db'
#
# my_connection = create_connection(database_name)
# if my_connection is not None:
#     cursor.execute(sql_to_create_employees_table)
#     print('Successfully connected to database')
#     create_table(my_connection, sql_to_create_employees_table)
#     insert_employee(my_connection, ('Jibek Manasova', 2400.5, 'Programming', '2000-01-25', False))
#     my_connection.close()
#
#     my_connection = create_connection(database_name)
#     insert_employee(my_connection, ('Mark Daniels', 1500.0, 'Football', '1999-01-02', False))
#     insert_employee(my_connection, ('Alex Brilliant', 2300.5, None, '1989-12-31', True))
#     insert_employee(my_connection, ('Diana Julls', 1800.0, 'Programming', '2005-01-22', True))
#     insert_employee(my_connection, ('Michael Corse', 1800.0, 'Football', '2001-09-17', True))
#     insert_employee(my_connection, ('Jack Moris', 2100.2, 'Programming', '2001-07-12', True))
#     insert_employee(my_connection, ('Viola Manilson', 1750.82, None, '1991-03-01', False))
#     insert_employee(my_connection, ('Joanna Moris', 1000.0, 'Football', '2004-04-13', False))
#     insert_employee(my_connection, ('Peter Parker', 2000.0, 'Programming', '2002-11-28', False))
#     insert_employee(my_connection, ('Paula Parkerson', 800.09, None, '2001-11-28', True))
#     insert_employee(my_connection, ('George Newel', 1320.0, 'Programming', '1981-01-24', True))
#     insert_employee(my_connection, ('Miranda Alistoun', 2500.55, 'Football', '1997-12-22', False))
#     insert_employee(my_connection, ('Valeria Hillton', 2000, 'Football', '1977-10-28', True))
#     insert_employee(my_connection, ('Jannet Miler', 2100.9, 'Programming', '1997-02-02', True))
#     insert_employee(my_connection, ('William Tokenson', 1500, None, '1999-12-12', False))
#     insert_employee(my_connection, ('Shanty Morani', 1200.6, None, '1989-08-13', False))
#     insert_employee(my_connection, ('Fiona Giordano', 900.12, 'Football', '1977-01-15', True))
#
#     update_employee(database_name, (2500, True, 2))
#     delete_employee(database_name, 2)
#     select_all_employees(database_name)
#     select_employees_by_salary(database_name, 2300)

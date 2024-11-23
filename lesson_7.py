import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print(f'{error} in CREATE_CONNECTION FUNCTION')
    return connection


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print(f'{error} in CREATE_TABLE FUNCTION')

def insert_products(connection, product):
    try:
        sql = '''INSERT INTO products (product_title, price, quantity)
         VALUES (?, ?, ?)'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in INSERT_PRODUCTS FUNCTION')


def update_quantity(connection, product):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in UPDATE_QUANTITY FUNCTION')


def update_price(connection, product):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in UPDATE_PRICE FUNCTION')


def delete_id(connection, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in DELETE_ID FUNCTION')


def select_all(connection):
    try:
        sql = '''SELECT * FROM products'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELECT_ALL FUNCTION')


def select_by_price_quantity(connection, limit):
    try:
        sql = '''SELECT * FROM products WHERE price <= ? AND quantity >= ?'''
        cursor = connection.cursor()
        cursor.execute(sql, limit)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELECT_BY_PRICE_QUANTITY FUNCTION')

def select_by_name(connection):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE '%Ise_cream%' '''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELECT_BY_NAME FUNCTION')


sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

my_connection = create_connection('hw.db')

if my_connection:
    print('Connected succesfully!')
    create_table(my_connection, sql_to_create_products_table)
    insert_products(my_connection, ('Vanilla Ice_cream', 120.0, 10))
    insert_products(my_connection, ('Chocolate Ice_cream', 150.0, 20))
    insert_products(my_connection, ('Strawberry Ice_cream', 130.0, 15))
    insert_products(my_connection, ('Mango Ice_cream', 140.0, 25))
    insert_products(my_connection, ('Pistachio Ice_cream', 160.0, 10))
    insert_products(my_connection, ('Cookie Dough Ice_cream', 170.0, 30))
    insert_products(my_connection, ('Caramel Ice_cream', 155.0, 12))
    insert_products(my_connection, ('Blueberry Ice_cream', 145.0, 18))
    insert_products(my_connection, ('Coffee Ice_cream', 150.0, 22))
    insert_products(my_connection, ('Mint Chocolate Ice_cream', 135.0, 19))
    insert_products(my_connection, ('Coconut Ice_cream', 125.0, 17))
    insert_products(my_connection, ('Lemon Ice_cream', 120.0, 20))
    insert_products(my_connection, ('Raspberry Ice_cream', 140.0, 16))
    insert_products(my_connection, ('Peach Ice_cream', 150.0, 14))
    insert_products(my_connection, ('Banana Ice_cream', 130.0, 21))

    update_quantity(my_connection, (18, 13))
    update_price(my_connection, (89, 7))
    delete_id(my_connection, 4)
    select_all(my_connection)
    select_by_price_quantity(my_connection, (100, 5))
    select_by_name(my_connection)
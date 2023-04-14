import sqlite3

# connection = sqlite3.connect(':memory:')
connection = sqlite3.connect('test.db')

cursor = connection.cursor()
# cursor.execute("""CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text
#     )""")
#

# cursor.execute("""INSERT INTO customers VALUES(
#         'John',
#         'Daw',
#         'john-daw@mail.com'
#     )""")

# many_customers = [
#     ('AAA', 'BBB', 'aaa@bbb.com'),
#     ('CCC', 'DDD', 'ccc@ddd.com'),
#     ('EEE', 'FFF', 'eee@fff.com')
# ]
#
# cursor.executemany("""INSERT INTO customers VALUES(?,?,?)""", many_customers)
#
# connection.commit()

cursor.execute("SELECT * FROM customers")
# cursor.fetchall()
print(cursor.fetchone())
# cursor.fetchmany(2)

connection.close()


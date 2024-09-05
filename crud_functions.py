import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')


def get_all_products():
    cursor.execute('SELECT title, description, price FROM Products', )
    prodacts = cursor.fetchall()
    return prodacts


def get_all_users():
    cursor.execute('SELECT username, email, age, balance FROM Users', )
    users = cursor.fetchall()
    return users


def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   ((f'{username}'), (f'{email}'), (f'{age}'), (f'{1000}')))
    connection.commit()


def is_included(username):
    cursor.execute('SELECT COUNT(username) FROM Users WHERE username = ?', (username,))
    count_users = cursor.fetchone()
    if count_users[0] != 0:
        return True
    return False


if __name__ == '__main__':
    initiate_db()
    add_user('user', '1@2.3', '67')
    print(get_all_products())
    print(get_all_users())
    print(is_included('user'))

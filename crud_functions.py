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

def get_all_products():
    cursor.execute('SELECT title, description, price FROM Products', )
    prodacts = cursor.fetchall()
    return prodacts

if __name__ == '__main__':
    initiate_db()
    print(get_all_products())

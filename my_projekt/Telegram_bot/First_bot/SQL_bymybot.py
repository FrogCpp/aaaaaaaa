import sqlite3

def start():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Picture (
    url TEXT NOT NULL,
    age url
    )
    ''')

def inp(messages):
    sql = 'INSERT INTO Url (url) VALUES (?)'
    connection.executemany(sql, messages)
    print(connection.execute("SELECT * FROM url"))

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()



connection.commit()
connection.close()
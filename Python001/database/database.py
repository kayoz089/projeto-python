import sqlite3

conn = sqlite3.connect("logins.db")
cursor = conn.cursor()

# tabela de usuários
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS logins(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        email TEXT NOT NULL
    )
''')


import sqlite3

# Connect to SQLite database (this will create the file if it doesn't exist)
conn = sqlite3.connect('notepad.db')
c = conn.cursor()

# Create users table
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

# Create notepad table (each user will have one notepad)
c.execute('''
    CREATE TABLE IF NOT EXISTS notepads (
        user_id INTEGER PRIMARY KEY,
        content TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
''')

# Commit and close
conn.commit()
conn.close()

print("Database initialized successfully.")

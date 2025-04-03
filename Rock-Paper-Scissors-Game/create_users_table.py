# import sqlite3

# # Connect to the Users database (it will create 'Users.db' if it doesn't exist)
# conn = sqlite3.connect('Users.db')
# cursor = conn.cursor()

# # Create the USERS table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS USERS (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     firstname TEXT NOT NULL,
#     lastname TEXT NOT NULL,
#     username TEXT UNIQUE NOT NULL,
#     password TEXT NOT NULL,
#     gender TEXT NOT NULL
# )
# """)

# conn.commit()
# conn.close()

# print("✅ Users table created successfully!")

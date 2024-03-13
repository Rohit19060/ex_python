# SQLite
# MySQL
# PostgreSQL
# MongoDB


# sqlite3
# flask_sqlalchemy

import sqlite3

con = sqlite3.connect("data.db")
print("Database opened successfully")

con.execute("DROP TABLE IF EXISTS users")
con.execute(
    "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)"
)
print("Table created successfully")

con.execute(
    "INSERT INTO users (name, email, password) VALUES ('admin', 'admin@gmail.com', 'admin')"
)
con.execute(
    """INSERT INTO users (name, email, password) 
    VALUES ('user1', 'user@gmail.com', 'user')"""
)

data = con.execute("SELECT * FROM users")
for row in data:
    print(row)
    print("ID: ", row[0])
    print("Name: ", row[1])
    print("Email: ", row[2])
    print("Password: ", row[3])
    print("")


con.commit()
print("Records inserted successfully")

# bb_b_ab_cbba_bcbb_

# a) acbac
# b) acbbb
# c) cbbba
# d) abbbc

# a) bbabcabbcbbaabcbbc
# b) bbabcabbcbbabbcbbb
# c) bbcbbabbcbbabbcbba
# d) bbabbabbcbbabbcbbc

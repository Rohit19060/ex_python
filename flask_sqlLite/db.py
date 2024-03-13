import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

# DROP TABLE IF EXISTS users;
conn.execute('DROP TABLE IF EXISTS users')
print("Table dropped successfully")

conn.execute('CREATE TABLE users (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print("Table created successfully")

# INSERT INTO users (name, addr, city, pin) VALUES ('John', 'Highway 21', 'New York', '12345');
conn.execute("INSERT INTO users (name, addr, city, pin) VALUES ('John', 'Highway 21', 'New York', '12345')")
conn.execute("INSERT INTO users (name, addr, city, pin) VALUES ('Mark', 'Highway 22', 'New York', '12345')")
conn.execute("INSERT INTO users (name, addr, city, pin) VALUES ('James', 'Highway 23', 'New York', '12345')")

conn.commit()
print("Records created successfully")

# Print the records
cursor = conn.execute("SELECT name, addr, city, pin FROM users")
for row in cursor:
    print("Name = ", row[0])
    print("Address = ", row[1])
    print("City = ", row[2])
    print("Pin = ", row[3], "\n")
    
conn.close()
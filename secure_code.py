import sqlite3
import hashlib

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Enter Username: ").strip()
password = input("Enter Password: ").strip()

if len(username) > 20:
    print("Invalid Username")
    exit()

hashed_password = hashlib.sha256(password.encode()).hexdigest()

query = "SELECT * FROM users WHERE username=? AND password=?"

cursor.execute(query, (username, hashed_password))

result = cursor.fetchone()

if result:
    print("Login Successful")
else:
    print("Login Failed")

conn.close()
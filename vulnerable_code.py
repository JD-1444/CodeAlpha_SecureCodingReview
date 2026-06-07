import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Enter Username: ")
password = input("Enter Password: ")

query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"

cursor.execute(query)

result = cursor.fetchone()

if result:
    print("Login Successful")
else:
    print("Login Failed")

conn.close()
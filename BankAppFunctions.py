import hashlib
import os
import time

def create_account(cursor, conn):
    os.system("clear")
    print("Enter details for your new account.")
    username = input("Username: ")
    password = input("Password: ")

    # Check if the username already exists
    cursor.execute('SELECT * FROM bank_users WHERE name = ?', (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        print("Username already exists. Please choose a different username.")
        return

    # Hash the password before saving
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    # Save the new account to the database
    cursor.execute('INSERT INTO bank_users (name, password_hash) VALUES (?, ?)', (username, password_hash))
    conn.commit()
    print("Account created successfully!")

def check_account(cursor):
    os.system("clear")
    print("Enter your username and password to log in.")
    username = input("Username: ")
    password = input("Password: ")

    # Hash the entered password to compare with the stored hash
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute('SELECT * FROM bank_users WHERE name = ? AND password_hash = ?', (username, password_hash))
    user = cursor.fetchone()

    if user:
        print("Login successful!")
        time.sleep(3)
        os.system("clear")
    else:
        print("Invalid username or password.")
        time.sleep(3)
        os.system("clear")

def DBList(cursor):
    os.system("clear")
    cursor.execute('SELECT * FROM bank_users')
    all_rows = cursor.fetchall()
    for row in all_rows:
        print(row)
    time.sleep(5)
    os.system("clear")

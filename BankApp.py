import sqlite3
import os
import time
from BankAppFunctions import create_account, check_account, DBList

# Connect to sqlite3
conn = sqlite3.connect("BankAppDB.db")
cursor = conn.cursor()

# Create bank_users table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS bank_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    password_hash TEXT NOT NULL
)
''')
conn.commit()

# Main loop for user interaction
while True:
    time.sleep(0.5)
    print("Hello User, Welcome to the bank!")
    print("1. Create an Account")
    print("2. Log in")
    print("3. Exit")
    print("4. Check if account exists")
    print("5. Print DB")

    choice = input("Select option: ")

    if choice == "1":
        create_account(cursor, conn)
    elif choice == "2":
        check_account(cursor)
    elif choice == "3":
        print("Exiting the application.")
        break
    elif choice == "4":
        check_account(cursor)
    elif choice == "5":
        os.system("clear")
        DBList(cursor)
    else:
        print("Invalid option. Please try again.")

# Clean up and close the database connection
conn.close()

import sqlite3
import hashlib

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


# Function to create a new account
def create_account():
    print("Enter details for your new account.")
    username = input("Username: ")
    password = input("Password: ")

    # Hash the password before saving
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    # Save the new account to the database
    cursor.execute('INSERT INTO bank_users (name, password_hash) VALUES (?, ?)', (username, password_hash))
    conn.commit()
    print("Account created successfully!")


# Function to check if an account exists
def check_account():
    print("Enter your username and password to log in.")
    username = input("Username: ")
    password = input("Password: ")

    # Hash the entered password to compare with the stored hash
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute('SELECT * FROM bank_users WHERE name = ? AND password_hash = ?', (username, password_hash))
    user = cursor.fetchone()

    if user:
        print("Login successful!")
    else:
        print("Invalid username or password.")


# Main loop for user interaction
while True:
    print("Hello User, Welcome to the bank!")
    print("1. Create an Account")
    print("2. Log in")
    print("3. Exit")
    print("4. Check if account exists")

    choice = input("Select option: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        check_account()
    elif choice == "3":
        print("Exiting the application.")
        break
    elif choice == "4":
        check_account()
    else:
        print("Invalid option. Please try again.")


# Class to represent a bank user (not currently in use in the loop)
class BankUser:
    def __init__(self, name, password):
        self.name = name
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()

    def save_to_db(self):
        cursor.execute('INSERT INTO bank_users (name, password_hash) VALUES (?, ?)', (self.name, self.password_hash))
        conn.commit()


# Example user creation (can be removed or modified for testing)
u1 = BankUser("Ariosha", 123)
u1.save_to_db()

# Fetch and display all users (for debugging/testing purposes)
cursor.execute('SELECT * FROM bank_users')
all_rows = cursor.fetchall()
for row in all_rows:
    print(row)

# Clean up and close the database connection 1
conn.close()
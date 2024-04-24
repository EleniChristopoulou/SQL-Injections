import sqlite3

def create_table():
    # Connect to the SQLite database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create the users table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       email TEXT,
                       password TEXT)''')

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

def insert_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    users_data = [
        ('user2@email.com', 'password2'),
        ('user1@email.com', 'password1'),
        ('user3@email.com', 'password3')
    ]
    cursor.executemany("INSERT INTO users (email, password) VALUES (?, ?)", users_data)

    conn.commit()
    conn.close()

def delete_all_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Execute the SQL command to delete all rows from the users table
    cursor.execute("DELETE FROM users")

    conn.commit()
    conn.close()

    print("All data deleted from the users table.")

def display_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    print("ID | Email             | Password")
    print("---------------------------------")

    for row in rows:
        print(f"{row[0]:2} | {row[1]:<18} | {row[2]}")
    conn.close()

def check_credentials(email, password):
    # Connect to the SQLite database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email=? AND password=?",(email,password))
    
    user = cursor.fetchone()

    conn.close()
    return user

def main():
    display_table()
    # Prompt the user for email and password
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check the credentials in the database
    user = check_credentials(email, password)

    if user:
        print("Login successful! Welcome, "+ user[1]+"\n")
    else:
        print("Invalid email or password.\n")

if __name__ == "__main__":
    while True:
        main()

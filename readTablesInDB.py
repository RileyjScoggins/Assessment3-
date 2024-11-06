import sqlite3

def list_tables():
    # Connect to the questions.db database
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    
    # Query to list all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    # Close the database connection
    conn.close()
    
    # Print the names of the tables
    print("Tables in the database:")
    for table in tables:
        print(table[0])

# Run the function to list tables
if __name__ == "__main__":
    list_tables()

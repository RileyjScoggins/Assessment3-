import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Function to create a table if it doesn't already exist
def create_table(table_name):
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_answer TEXT NOT NULL
    )
    ''')

# Dictionary of questions organized by table (class) with multiple-choice options
questions_data = {
    "DS3850": [
        ("What is the correct file extension for Python files?", ".py", ".pyc", ".pyo", ".pyz", "A"),
        ("Which keyword is used to define a function in Python?", "func", "function", "def", "define", "C"),
        ("What data type is used to store a sequence of characters in Python?", "int", "float", "str", "list", "C"),
        ("What symbol is used to start a comment in Python?", "#", "//", "/*", "--", "A"),
        ("How do you print output to the console in Python?", "console.log()", "echo()", "print()", "printf()", "C"),
        ("Which operator is used for exponentiation in Python?", "^", "**", "exp()", "power()", "B"),
        ("What is the output of print(type([]))?", "dict", "list", "tuple", "set", "B"),
        ("What keyword is used to handle exceptions in Python?", "catch", "try-except", "finally", "except-catch", "B"),
        ("What does the 'len' function do in Python?", "Length", "Type", "Size", "Width", "A"),
        ("What is a dictionary in Python?", "Key-value pairs", "List", "Set", "Sequence", "A")
    ],
    "DS3860": [
        ("What does SQL stand for?", "Simple Query Language", "Structured Query Language", "Standard Query Language", "Sequential Query Language", "B"),
        ("Which SQL statement is used to retrieve data?", "FETCH", "GET", "SELECT", "PULL", "C"),
        ("What SQL command is used to delete a table?", "REMOVE", "DELETE", "CLEAR", "DROP", "D"),
        ("What SQL function is used to find the highest value in a column?", "MAX", "HIGH", "TOP", "BEST", "A"),
        ("What is a primary key in a database?", "A non-unique identifier", "A unique identifier for each record", "A data type", "A schema", "B"),
        ("What clause is used in SQL to filter records?", "FILTER", "WHERE", "IF", "HAVING", "B"),
        ("What is a foreign key?", "A key unique to each table", "A reference to a primary key in another table", "A type of index", "A duplicate key", "B"),
        ("Which SQL statement is used to update data?", "MODIFY", "CHANGE", "ALTER", "UPDATE", "D"),
        ("What is a JOIN in SQL?", "Combines rows from two or more tables", "Deletes duplicate rows", "Merges two databases", "Splits a table", "A"),
        ("What is normalization in databases?", "Removing data", "Organizing data to reduce redundancy", "Inserting data", "Exporting data", "B")
    ],
    "DS4210": [
        ("What does IT stand for?", "Information Technology", "Internet Technology", "Intelligent Technology", "Interconnected Technology", "A"),
        ("What is the primary function of an operating system?", "Manages computer resources", "Provides Internet access", "Runs specific applications", "Monitors security", "A"),
        ("What is the purpose of a firewall?", "Control network traffic", "Increase network speed", "Remove malware", "Install updates", "A"),
        ("What does 'URL' stand for?", "Uniform Resource Locator", "Universal Resource Locator", "Unified Resource Locator", "Uniform Remote Locator", "A"),
        ("What is cybersecurity?", "Network optimization", "System repair", "Protection from theft or damage", "Data storage management", "C"),
        ("What is cloud computing?", "Using local storage", "A type of computer", "Storing data over the internet", "Creating a personal network", "C"),
        ("What does Wi-Fi stand for?", "Wide Fidelity", "Wireless Fidelity", "Wireless Frequency", "Wide Frequency", "B"),
        ("What is the role of a database?", "Organizing and storing data", "Providing internet access", "Creating computer applications", "Running scripts", "A"),
        ("What is artificial intelligence?", "Automation of manual tasks", "Simulation of human intelligence", "Creation of social networks", "A type of software", "B"),
        ("What is a network?", "A single computer", "A system of interconnected computers", "An application", "A database", "B")
    ],
    "DS4220": [
        ("What is the main purpose of R?", "Web development", "Statistical analysis", "Graphic design", "Game development", "B"),
        ("What function is used to create a vector in R?", "vector()", "c()", "v()", "make_vector()", "B"),
        ("What is a data frame in R?", "A graphical plot", "A table-like structure for data", "A type of loop", "A statistical function", "B"),
        ("What symbol is used for assignment in R?", "=", "<-", "<=", ":", "B"),
        ("What does the 'ggplot2' package do in R?", "Web scraping", "Data visualization", "Statistical testing", "Data cleaning", "B"),
        ("What is a list in R?", "A collection of different data types", "A string", "A data frame", "A numeric vector", "A"),
        ("How do you install a package in R?", "install.package()", "load.package()", "import.package()", "install.packages()", "D"),
        ("What is the function to read a CSV file in R?", "read.csv()", "load.csv()", "import.csv()", "open.csv()", "A"),
        ("What does the 'summary' function do in R?", "Provides summary statistics", "Removes NA values", "Plots data", "Saves data", "A"),
        ("What is the 'tidyverse' in R?", "A collection of R packages for data science", "A data visualization library", "A text formatting tool", "A data storage method", "A")
    ],
    "PHED1015": [
        ("What does 'asana' mean in yoga?", "Mindfulness", "Postures", "Breathing", "Meditation", "B"),
        ("What is the primary purpose of yoga?", "Physical strength", "Increasing flexibility", "Uniting body and mind", "Losing weight", "C"),
        ("What does 'pranayama' refer to?", "Balance", "Meditation", "Breath control", "Mindfulness", "C"),
        ("Which type of yoga focuses on physical postures?", "Hatha yoga", "Karma yoga", "Raja yoga", "Jnana yoga", "A"),
        ("What is meditation?", "Physical exercise", "Focused mental exercise", "A breathing technique", "A type of posture", "B"),
        ("What does 'namaste' signify?", "Hello", "Goodbye", "I bow to you", "Thank you", "C"),
        ("What is 'savasana'?", "A breathing technique", "A type of yoga", "The corpse pose for relaxation", "A chant", "C"),
        ("What is 'yoga nidra'?", "Deep sleep", "A form of meditation", "A state of conscious relaxation", "A posture", "C"),
        ("What is a common yoga prop?", "Exercise mat", "Yoga mat", "Block", "Belt", "B"),
        ("What does 'chakra' mean?", "Energy centers in the body", "Physical strength", "Mental focus", "Posture", "A")
    ]
}

# Create each table and insert questions
for table, questions in questions_data.items():
    create_table(table)
    for question, option_a, option_b, option_c, option_d, correct_answer in questions:
        cursor.execute(f'''
        INSERT INTO {table} (question, option_a, option_b, option_c, option_d, correct_answer)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (question, option_a, option_b, option_c, option_d, correct_answer))
    conn.commit()

print("All questions have been inserted into their respective tables.")

# Close the connection
conn.close()

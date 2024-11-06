import sqlite3

def fetch_all_questions():
    # Connect to the questions.db database
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    
    # Retrieve all records from the questions table
    cursor.execute("SELECT course_code, question, answer FROM questions")
    rows = cursor.fetchall()
    
    # Close the database connection
    conn.close()
    
    # Display each question with its course code and answer
    for course_code, question, answer in rows:
        print(f"Course Code: {course_code}")
        print(f"Question: {question}")
        print(f"Answer: {answer}")
        print("-" * 50)

# Run the function to fetch and display questions
if __name__ == "__main__":
    fetch_all_questions()


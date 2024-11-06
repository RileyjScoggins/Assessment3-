import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Function to delete a question by its ID
def delete_question(question_id):
    try:
        # Check if the question exists
        cursor.execute('SELECT * FROM DS3850 WHERE id = ?', (question_id,))
        question = cursor.fetchone()

        if not question:
            print("No question found with that ID.")
            return
        
        # Ask for confirmation
        confirm = input(f"Are you sure you want to delete the question: '{question[1]}'? (y/n): ")
        if confirm.lower() == 'y':
            cursor.execute('DELETE FROM DS3850 WHERE id = ?', (question_id,))
            conn.commit()
            print(f"Question ID {question_id} has been deleted.")
        else:
            print("Deletion canceled.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to delete a question from any subject table
def delete_from_subject_table(subject_table, question_id):
    try:
        # Check if the question exists
        cursor.execute(f'SELECT * FROM {subject_table} WHERE id = ?', (question_id,))
        question = cursor.fetchone()

        if not question:
            print(f"No question found with that ID in {subject_table}.")
            return
        
        # Ask for confirmation
        confirm = input(f"Are you sure you want to delete the question: '{question[1]}'? (y/n): ")
        if confirm.lower() == 'y':
            cursor.execute(f'DELETE FROM {subject_table} WHERE id = ?', (question_id,))
            conn.commit()
            print(f"Question ID {question_id} has been deleted from {subject_table}.")
        else:
            print("Deletion canceled.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # List of subjects and their corresponding tables
    subjects = [
        ('DS3850', 'Intro to Python'),
        ('DS3860', 'Database Mgmt'),
        ('DS4210', 'Business Intelligence'),
        ('DS4220', 'Advanced Analytics'),
        ('PHED1015', 'Yoga')
    ]
    
    # Ask the user to choose a subject
    print("Select a subject to delete a question from:")
    for i, (table, name) in enumerate(subjects, 1):
        print(f"{i}. {name}")
    
    try:
        subject_choice = int(input("Enter the number corresponding to the subject: "))
        if subject_choice < 1 or subject_choice > len(subjects):
            print("Invalid selection.")
            return
        
        # Get the selected subject's table name
        selected_subject = subjects[subject_choice - 1][0]

        # Get the question ID to delete
        question_id = int(input(f"Enter the question ID to delete from {selected_subject}: "))

        # Call the delete function for the selected subject table
        delete_from_subject_table(selected_subject, question_id)

    except ValueError:
        print("Please enter a valid number.")
    finally:
        # Close the connection
        conn.close()

if __name__ == "__main__":
    main()

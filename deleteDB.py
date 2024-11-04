# deleteDB.py

def delete_question(file_path='questions_data.txt'):
    question_to_delete = input("Enter the question text you want to delete: ")
    found = False

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file:
            for line in lines:
                category, question_text, answer = line.strip().split(", ")
                if question_text == question_to_delete:
                    found = True
                    print(f"Deleted question: {question_text}")
                else:
                    file.write(line)
        
        if not found:
            print("Question not found.")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")

if __name__ == "__main__":
    delete_question()

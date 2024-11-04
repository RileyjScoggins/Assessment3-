# readDB.py

def read_questions(file_path='questions_data.txt'):
    try:
        with open(file_path, 'r') as file:
            questions = file.readlines()
            if not questions:
                print("No questions found.")
            else:
                for question in questions:
                    category, question_text, answer = question.strip().split(", ")
                    print(f"Category: {category}")
                    print(f"Question: {question_text}")
                    print(f"Answer: {answer}")
                    print("-" * 40)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")

if __name__ == "__main__":
    read_questions()

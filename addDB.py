# addDB.py

def add_question(file_path='questions_data.txt'):
    category = input("Enter the category: ")
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")

    with open(file_path, 'a') as file:
        file.write(f"{category}, {question}, {answer}\n")
        print("Question added successfully.")

if __name__ == "__main__":
    add_question()

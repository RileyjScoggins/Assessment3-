import tkinter as tk
from tkinter import ttk, messagebox

# Updated categories as specified
categories = [
    "DS-3850 (Introduction to Python)", 
    "DS-3860 (Database Management)", 
    "DS-4210 (Intro to Information Technology)", 
    "DS-4220 (Coding Language of R)", 
    "PHED-1015 (Yoga)"
]

# Sample questions for each quiz
quizzes = {
    "DS-3850 (Introduction to Python)": [
        {
            "question": "What is the correct file extension for Python files?",
            "answer": ".py"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "answer": "def"
        },
        {
            "question": "What will be the output of 'print(2 ** 3)'?",
            "answer": "8"
        },
        {
            "question": "Which of the following is a mutable data type?",
            "answer": "list"
        },
        {
            "question": "Which function is used to convert a string to lowercase in Python?",
            "answer": "lower"
        },
        {
            "question": "What is the output of 'len([1, 2, 3])'?",
            "answer": "3"
        },
        {
            "question": "What keyword is used to import modules in Python?",
            "answer": "import"
        },
        {
            "question": "What is the purpose of the 'return' statement in a function?",
            "answer": "return value"
        },
        {
            "question": "Which function is used to read user input in Python?",
            "answer": "input"
        },
        {
            "question": "What symbol is used to denote comments in Python?",
            "answer": "#"
        }
    ],
    "DS-3860 (Database Management)": [
        {
            "question": "What does SQL stand for?",
            "answer": "Structured Query Language"
        },
        {
            "question": "Which SQL statement is used to create a table?",
            "answer": "CREATE TABLE"
        },
        {
            "question": "What is a primary key?",
            "answer": "unique identifier"
        },
        {
            "question": "Which command is used to retrieve data from a database?",
            "answer": "SELECT"
        },
        {
            "question": "What does a foreign key do?",
            "answer": "links tables"
        },
        {
            "question": "What is normalization in database design?",
            "answer": "reducing redundancy"
        },
        {
            "question": "Which SQL command is used to update existing records?",
            "answer": "UPDATE"
        },
        {
            "question": "What is a view in SQL?",
            "answer": "virtual table"
        },
        {
            "question": "Which command is used to delete a table?",
            "answer": "DROP TABLE"
        },
        {
            "question": "What is a join in SQL?",
            "answer": "combining tables"
        }
    ],
    "DS-4210 (Intro to Information Technology)": [
        {
            "question": "What does IT stand for?",
            "answer": "Information Technology"
        },
        {
            "question": "Which of the following is an example of hardware?",
            "answer": "Computer"
        },
        {
            "question": "What is the main function of an operating system?",
            "answer": "manage resources"
        },
        {
            "question": "What is a network?",
            "answer": "interconnected devices"
        },
        {
            "question": "What does cloud computing mean?",
            "answer": "internet access"
        },
        {
            "question": "What does the term 'malware' refer to?",
            "answer": "harmful software"
        },
        {
            "question": "What is the primary purpose of a database?",
            "answer": "store data"
        },
        {
            "question": "Which of the following is a popular operating system?",
            "answer": "Windows"
        },
        {
            "question": "What is a firewall?",
            "answer": "security system"
        },
        {
            "question": "What is an IP address?",
            "answer": "device identifier"
        }
    ],
    "DS-4220 (Coding Language of R)": [
        {
            "question": "What is the primary use of R?",
            "answer": "data analysis"
        },
        {
            "question": "Which function is used to read data into R?",
            "answer": "read.csv"
        },
        {
            "question": "Which of the following is a data structure in R?",
            "answer": "Data Frame"
        },
        {
            "question": "What operator is used for assignment in R?",
            "answer": "<-"
        },
        {
            "question": "Which package is commonly used for data manipulation in R?",
            "answer": "dplyr"
        },
        {
            "question": "Which function generates a plot in R?",
            "answer": "plot"
        },
        {
            "question": "Which function is used to calculate the mean in R?",
            "answer": "mean"
        },
        {
            "question": "How do you create a vector in R?",
            "answer": "c()"
        },
        {
            "question": "What is the purpose of the 'install.packages()' function?",
            "answer": "install packages"
        },
        {
            "question": "Which symbol is used for comments in R?",
            "answer": "#"
        }
    ],
    "PHED-1015 (Yoga)": [
        {
            "question": "What does 'asana' refer to in yoga?",
            "answer": "Postures"
        },
        {
            "question": "Which of the following is a benefit of yoga?",
            "answer": "All of the above"
        },
        {
            "question": "What is the meaning of 'Namaste'?",
            "answer": "I bow to you"
        },
        {
            "question": "Which breathing technique is commonly used in yoga?",
            "answer": "Pranayama"
        },
        {
            "question": "What does 'vinyasa' refer to?",
            "answer": "Flow of movement"
        },
        {
            "question": "In which yoga style is the focus on holding poses for longer durations?",
            "answer": "Hatha"
        },
        {
            "question": "Which of the following is a common yoga pose?",
            "answer": "Downward Dog"
        },
        {
            "question": "What is 'meditation' often used for in yoga practice?",
            "answer": "clear the mind"
        },
        {
            "question": "Which of the following is NOT a type of yoga?",
            "answer": "Aerobics"
        },
        {
            "question": "What is the primary focus of restorative yoga?",
            "answer": "Healing and relaxation"
        }
    ]
}
# Create the main window
class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Application")
        self.geometry("400x200")
        
        self.selected_category = tk.StringVar()
        self.question_index = 0
        self.score = 0
        
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Select a Quiz Category", font=("Arial", 16))
        label.pack(pady=20)
        
        # Dropdown menu for categories
        self.category_dropdown = ttk.Combobox(self, textvariable=self.selected_category, values=categories, state="readonly")
        self.category_dropdown.pack(pady=10)

        # Start quiz button
        start_button = tk.Button(self, text="Start Quiz", command=self.start_quiz)
        start_button.pack(pady=20)

    def start_quiz(self):
        selected = self.selected_category.get()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a category to continue.")
            return
        
        self.question_index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        if self.question_index < len(quizzes[self.selected_category.get()]):
            question_data = quizzes[self.selected_category.get()][self.question_index]
            self.display_question(question_data)
        else:
            self.end_quiz()

    def display_question(self, question_data):
        question_window = tk.Toplevel(self)
        question_window.title("Quiz Question")
        
        question_label = tk.Label(question_window, text=question_data["question"], wraplength=400)
        question_label.pack(pady=10)
        
        self.answer_entry = tk.Entry(question_window)
        self.answer_entry.pack(pady=10)
        
        submit_button = tk.Button(question_window, text="Submit Answer", command=lambda: self.check_answer(question_data["answer"], question_window))
        submit_button.pack(pady=20)

    def check_answer(self, correct_answer, question_window):
        user_answer = self.answer_entry.get().strip()
        if user_answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct!", "Correct! 😊")
            self.score += 1
        else:
            messagebox.showerror("Incorrect", f"Incorrect! 😢 The correct answer was: {correct_answer}")
        
        self.question_index += 1
        question_window.destroy()
        self.show_question()

    def end_quiz(self):
        messagebox.showinfo("Quiz Finished", f"You scored {self.score} out of {len(quizzes[self.selected_category.get()])}!")
        self.quit()

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox

# Categories as shown in the image
categories = ["Business Communication", "Business App Dev", "Accounting", "Finance", "Marketing"]

def open_quiz_window(selected_category):
    if selected_category:
        messagebox.showinfo("Starting Quiz", f"Loading quiz for: {selected_category}")
        category_window.destroy()
        # Code to open the quiz window would go here
    else:
        messagebox.showwarning("Selection Error", "Please select a category to continue.")

# Initialize main window
category_window = tk.Tk()
category_window.title("Quiz - Select Your Category")
category_window.geometry("300x150")

# Label
label = tk.Label(category_window, text="Select your category", font=("Arial", 12))
label.pack(pady=10)

# Dropdown menu for categories
category_var = tk.StringVar()
category_dropdown = ttk.Combobox(category_window, textvariable=category_var, state="readonly")
category_dropdown['values'] = categories
category_dropdown.pack(pady=10)

# Start quiz button
start_button = tk.Button(category_window, text="Start Quiz", command=lambda: open_quiz_window(category_var.get()))
start_button.pack(pady=20)

category_window.mainloop()

#Step 2
import tkinter as tk
from tkinter import messagebox

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer.lower()  # Store the answer in lowercase for easier comparison

    def check_answer(self, user_answer):
        """Return True if user_answer is correct; otherwise, False."""
        return user_answer.lower().strip() == self.answer

# Sample Python questions for the quiz
sample_questions = [
    Question("What keyword is used to define a function in Python?", "def"),
    Question("What data type is used to store true or false values?", "boolean"),
    Question("What operator is used for exponentiation in Python?", "**"),
    Question("What function is used to display output in Python?", "print"),
    Question("What symbol is used to start a comment in Python?", "#"),
    Question("What keyword is used to create a loop that repeats a specific number of times?", "for"),
    Question("What keyword is used to create a loop that continues until a condition is false?", "while"),
    Question("What built-in function is used to get the length of a list?", "len"),
    Question("What method is used to add an item to the end of a list?", "append"),
    Question("What function is used to convert a string to an integer in Python?", "int"),
]

class QuizApp:
    def __init__(self, questions):
        self.questions = questions
        self.current_question_index = 0
        self.score = 0
        self.quiz_window = None

    def start_quiz(self):
        """Initialize the quiz window and display the first question."""
        self.quiz_window = tk.Tk()
        self.quiz_window.title("Quiz Window")
        self.quiz_window.geometry("400x200")

        # Display the first question
        self.display_question()

        self.quiz_window.mainloop()

    def display_question(self):
        """Display the current question and answer entry box."""
        # Clear the window for the new question
        for widget in self.quiz_window.winfo_children():
            widget.destroy()

        current_question = self.questions[self.current_question_index]

        # Display question text
        question_label = tk.Label(self.quiz_window, text=f"Question: {current_question.text}", font=("Arial", 12))
        question_label.pack(pady=10)

        # Entry box for user answer
        self.answer_entry = tk.Entry(self.quiz_window, font=("Arial", 12))
        self.answer_entry.pack(pady=10)

        # Submit button
        submit_button = tk.Button(self.quiz_window, text="Submit Answer", command=self.submit_answer)
        submit_button.pack(pady=20)

    def submit_answer(self):
        """Check the answer and provide feedback to the user."""
        current_question = self.questions[self.current_question_index]
        user_answer = self.answer_entry.get()

        if current_question.check_answer(user_answer):
            messagebox.showinfo("Correct!", "Correct! Well done.")
            self.score += 1
        else:
            messagebox.showinfo("Incorrect", f"Incorrect. The correct answer was: {current_question.answer}")

        # Move to the next question or end the quiz
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        """End the quiz and show the final score."""
        messagebox.showinfo("Quiz Complete", f"You scored {self.score} out of {len(self.questions)}")
        self.quiz_window.destroy()

# Start the quiz with the sample questions
quiz_app = QuizApp(sample_questions)
quiz_app.start_quiz()

import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# Connect to SQLite database
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Global variables to store quiz data
current_question = None
score = 0
question_index = 0
questions = []

# Mapping of class display names to table names
class_mapping = {
    "DS3850 - Intro to Python": "DS3850",
    "DS3860 - Database Mgmt": "DS3860",
    "DS4210 - Business Intelligence": "DS4210",
    "DS4220 - Advanced Analytics": "DS4220",
    "PHED1015 - Yoga": "PHED1015"
}

# Function to load questions for the selected class
def load_questions(table_name):
    global questions
    cursor.execute(f"SELECT question, option_a, option_b, option_c, option_d, correct_answer FROM {table_name} LIMIT 10")
    questions = cursor.fetchall()

# Function to start the quiz
def start_quiz():
    selected_class = class_var.get()
    if selected_class:
        table_name = class_mapping[selected_class]
        load_questions(table_name)
        open_quiz_window(selected_class)
    else:
        messagebox.showwarning("Select Class", "Please select a class to start the quiz.")

# Function to open the quiz window
def open_quiz_window(class_name):
    global score, question_index, current_question

    score = 0
    question_index = 0
    quiz_window = tk.Toplevel(root)
    quiz_window.title(f"Quiz - {class_name}")

    # Display question and answer options
    def display_question():
        global current_question
        if question_index < len(questions):
            current_question = questions[question_index]
            question_label.config(text=current_question[0])
            option_a_check.config(text=current_question[1])
            option_b_check.config(text=current_question[2])
            option_c_check.config(text=current_question[3])
            option_d_check.config(text=current_question[4])
            answer_var.set("")
        else:
            show_results()
            quiz_window.destroy()

    # Check answer and proceed to the next question
    def check_answer():
        global score, question_index
        selected_option = answer_var.get()
        
        # Verify the correct answer and show appropriate message
        if selected_option == current_question[5]:
            score += 1
            result_label.config(text="Correct! 😊", fg="green")
        else:
            result_label.config(text="Incorrect! 😢", fg="red")
        
        question_index += 1
        quiz_window.after(1000, display_question)  # Proceed to the next question after 1 second delay

    # Show final score with customized feedback
    def show_results():
        if score < 7:
            feedback = "You really should study this again. 📘"
        elif 7 <= score < 10:
            feedback = "That was good, but you could do better! 👍"
        else:
            feedback = "You're ready! 😎"
        messagebox.showinfo("Quiz Completed", f"You answered {score} out of 10 questions correctly.\n{feedback}")

    # Quiz window layout
    question_label = tk.Label(quiz_window, text="", wraplength=400, font=("Arial", 14))
    question_label.pack(pady=10)

    answer_var = tk.StringVar()

    option_a_check = tk.Checkbutton(quiz_window, text="", variable=answer_var, onvalue="A", font=("Arial", 12))
    option_a_check.pack(anchor="w", padx=20)

    option_b_check = tk.Checkbutton(quiz_window, text="", variable=answer_var, onvalue="B", font=("Arial", 12))
    option_b_check.pack(anchor="w", padx=20)

    option_c_check = tk.Checkbutton(quiz_window, text="", variable=answer_var, onvalue="C", font=("Arial", 12))
    option_c_check.pack(anchor="w", padx=20)

    option_d_check = tk.Checkbutton(quiz_window, text="", variable=answer_var, onvalue="D", font=("Arial", 12))
    option_d_check.pack(anchor="w", padx=20)

    result_label = tk.Label(quiz_window, text="", font=("Arial", 12))
    result_label.pack(pady=10)

    next_button = tk.Button(quiz_window, text="Next", command=check_answer)
    next_button.pack(pady=10)

    display_question()

# Main window setup
root = tk.Tk()
root.title("Quiz Bowl")
root.geometry("400x200")

# Dropdown menu for class selection
class_var = tk.StringVar()
class_label = tk.Label(root, text="Select a class to start the quiz:", font=("Arial", 12))
class_label.pack(pady=10)

class_dropdown = ttk.Combobox(root, textvariable=class_var, font=("Arial", 12))
class_dropdown['values'] = list(class_mapping.keys())
class_dropdown.pack(pady=10)

# Start quiz button
start_button = tk.Button(root, text="Start Quiz", command=start_quiz, font=("Arial", 12))
start_button.pack(pady=20)

root.mainloop()
conn.close()

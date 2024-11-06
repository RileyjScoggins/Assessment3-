# Quarterly-Assessment-3
Quiz Bowl Project
The Quiz Bowl Project is a quiz application designed to help users test their knowledge across multiple subjects. Built with Python, this project leverages a SQLite database and a Tkinter-based GUI to deliver a user-friendly quiz experience.

Project Overview
This project offers:

Subject-specific quizzes with questions stored in a database for easy management.
Immediate feedback on answers, letting users know if they are correct or incorrect.
A final score at the end, with custom feedback based on performance.
Key Features
Subject Selection: Choose from the following topics:

DS3850 - Intro to Python
DS3860 - Database Management
DS4210 - Business Intelligence
DS4220 - Advanced Analytics
PHED1015 - Yoga
Quiz Interaction:

Users can select a class from a dropdown menu.
Questions are presented one at a time with checkboxes for answer selection.
At the end, users receive a summary of their performance.
Project Structure
bash
Copy code
QuizBowlProject/
│
├── main.py             # Main script with GUI and quiz logic
├── questions.db        # SQLite database with questions for each subject
└── README.md           # Project README
Getting Started
Prerequisites
Python 3.x installed.
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/QuizBowlProject.git
Navigate to the project directory:
bash
Copy code
cd QuizBowlProject
Install dependencies (if listed in requirements.txt):
bash
Copy code
pip install -r requirements.txt
Run the application:
bash
Copy code
python main.py
Database
The included questions.db file is pre-loaded with questions. You can add more by editing the database directly.

Usage
Select a subject from the dropdown menu.
Begin the quiz and answer each question as it appears.
At the end of the quiz, review your final score and feedback.
Future Enhancements
Possible future additions could include more subjects, timed quizzes, and difficulty levels.

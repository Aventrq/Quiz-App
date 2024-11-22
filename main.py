# main.py
import tkinter as tk
from quiz import Quiz
from gui import QuizGUI
from questions import questions

if __name__ == "__main__":
    root = tk.Tk()
    quiz = Quiz(questions)
    app = QuizGUI(root, quiz)
    root.mainloop()

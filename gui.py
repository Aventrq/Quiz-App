import tkinter as tk
from tkinter import ttk, font

class QuizGUI:
    def __init__(self, root, quiz):
        self.root = root
        self.quiz = quiz
        self.current_frame = None

        self.setup_main_window()
        self.show_title_screen()

    def setup_main_window(self):
        self.root.title('Quiz Time!')
        window_width = 600
        window_height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def clear_frame(self):
        if self.current_frame:
            self.current_frame.destroy()  # Destroy the previous frame completely

    def show_title_screen(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(fill="both", expand=True)

        title_font = font.Font(family="Helvetica", size=48, weight="bold")
        title_label = tk.Label(self.current_frame, text="Quiz Time", font=title_font, fg="black", justify='center')
        title_label.pack(pady=20)

        theme_font = font.Font(family="Arial", size=24, weight="bold")
        theme_label = tk.Label(self.current_frame, text="Theme: Chemistry", font=theme_font)
        theme_label.pack(pady=10)

        start_button = ttk.Button(self.current_frame, text="Start Quiz", command=self.start_quiz)
        start_button.pack(pady=20)

    def start_quiz(self):
        self.show_question()

    def show_question(self):
        self.clear_frame()
        question_data = self.quiz.get_current_question()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack(fill="both", expand=True)

        question_label = tk.Label(self.current_frame, text=question_data['question'], font=("Arial", 14), wraplength=500)
        question_label.pack(pady=10)

        for answer in question_data['answers']:
            answer_button = ttk.Button(self.current_frame, text=answer, command=lambda a=answer: self.handle_answer(a))
            answer_button.pack(fill="x", padx=20, pady=5)


    def handle_answer(self, selected_answer):
        """Handles the logic when an answer is selected."""
        # Check if the answer is correct
        is_correct = self.quiz.check_answer(selected_answer)

        # Update the score
        self.quiz.update_score(is_correct)

        # Clear current frame
        self.clear_frame()

        # Create feedback frame
        feedback_frame = tk.Frame(self.root)
        feedback_frame.pack(fill="both", expand=True)

        # Provide feedback
        feedback_text = "Correct!" if is_correct else "Wrong!"
        feedback_color = "green" if is_correct else "red"

        feedback_label = tk.Label(feedback_frame, text=feedback_text, font=("Arial", 16), fg=feedback_color)
        feedback_label.pack(pady=10)

        # Transition to the next question or end screen after 1 second
        feedback_frame.after(1000, lambda: [feedback_frame.destroy(), self.handle_next_question()])

    def handle_next_question(self):
        """Handles transitioning to the next question or end screen."""
        if self.quiz.next_question():
            self.show_question()
        else:
            self.show_end_screen()


    def next_question(self):
        if self.quiz.next_question():
            self.show_question()
        else:
            self.show_end_screen()

    def show_end_screen(self):
        self.clear_frame()  # Clear the previous frame

        # Create a new frame for the end screen
        end_frame = tk.Frame(self.root)
        self.current_frame = end_frame
        end_frame.pack(fill="both", expand=True)

        # Create and pack the "Quiz Completed!" label
        end_label = tk.Label(end_frame, text="Quiz Completed!", font=("Arial", 16), fg="blue")
        end_label.pack(pady=10)

        # Show the score
        score_label = tk.Label(end_frame, text=f"Your Score: {self.quiz.score}", font=("Arial", 14))
        score_label.pack(pady=5)

        # Restart button to restart the quiz
        restart_button = ttk.Button(end_frame, text="Restart", command=self.restart_quiz)
        restart_button.pack(pady=10)


    def restart_quiz(self):
        self.quiz.current_question_index = 0  # Reset to first question
        self.quiz.score = 0  # Reset score
        self.quiz.multiplier = 1  # Reset multiplier
        self.show_title_screen()  # Show the title screen to start the quiz fresh


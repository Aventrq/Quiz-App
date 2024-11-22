class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.multiplier = 1
        self.current_question_index = 0
        self.current_theme = 'Chemistry'

    def get_current_question(self):
        return self.questions[self.current_theme][self.current_question_index]

    def check_answer(self, selected_answer):
        current_question = self.get_current_question()
        return selected_answer == current_question['correct']

    def update_score(self, correct):
        if correct:
            self.score += 10 * self.multiplier
            self.multiplier += 1
        else:
            self.multiplier = 1  # Reset multiplier for wrong answers

    def has_next_question(self):
        return self.current_question_index + 1 < len(self.questions[self.current_theme])

    def next_question(self):
        if self.has_next_question():
            self.current_question_index += 1
            return True
        return False

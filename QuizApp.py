from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class QuizApp(App):
    def build(self):
        self.score = 0
        self.current_question = 0
        self.questions = [
            {"question": "What is the capital of france?", "options": ["Paris", "London", "Berlin"], "answer": "Paris"},
            {"question": "2 + 2 equals?", "options": ["3", "4", "5"], "answer": "4"},
            {"question": "What is the capital of india?", "options": ["Mumbai", "Delhi", "Benguluru"], "answer": "Delhi"},
        ]

        self.layout = BoxLayout(orientation='vertical', padding=10)
        self.question_label = Label(text=self.questions[self.current_question]["question"])
        self.layout.add_widget(self.question_label)

        self.options_buttons = []
        for option in self.questions[self.current_question]["options"]:
            btn = Button(text=option)
            btn.bind(on_press=self.check_answer)
            self.options_buttons.append(btn)
            self.layout.add_widget(btn)

        self.score_label = Label(text=f"Score: {self.score}")
        self.layout.add_widget(self.score_label)

        return self.layout

    def check_answer(self, instance):
        if instance.text == self.questions[self.current_question]["answer"]:
            self.score += 1
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.update_question()
        else:
            self.end_quiz()

    def update_question(self):
        self.question_label.text = self.questions[self.current_question]["question"]
        for i, option in enumerate(self.questions[self.current_question]["options"]):
            self.options_buttons[i].text = option
        self.score_label.text = f"Score: {self.score}"

    def end_quiz(self):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text=f"Quiz Finished! Your Score: {self.score}"))

if __name__ == '__main__':
    QuizApp().run()

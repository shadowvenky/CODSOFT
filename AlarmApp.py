from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from datetime import datetime
import time
import threading

class AlarmApp(App):
    def build(self):
        self.alarm_time = None
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.time_label = Label(text="Current Time: " + time.strftime('%H:%M:%S'), font_size=24)
        layout.add_widget(self.time_label)

        self.alarm_label = Label(text="Set Alarm Time (Hours:Minutes:Seconds):", font_size=18)
        layout.add_widget(self.alarm_label)

        self.alarm_input = TextInput(hint_text="Enter alarm time", multiline=False, font_size=18)
        layout.add_widget(self.alarm_input)

        self.set_alarm_button = Button(text="Set Alarm", size_hint=(1, 0.5), font_size=18)
        self.set_alarm_button.bind(on_press=self.set_alarm)
        layout.add_widget(self.set_alarm_button)

        self.status_label = Label(text="", font_size=18)
        layout.add_widget(self.status_label)

        Clock.schedule_interval(self.update_time, 1)
        return layout

    def update_time(self, dt):
        current_time = time.strftime('%H:%M:%S')
        self.time_label.text = "Current Time: " + current_time

        if self.alarm_time and current_time == self.alarm_time:
            self.status_label.text = "ALARM! Wake up!"
            threading.Thread(target=self.play_alarm_sound).start()
            self.alarm_time = None  # Reset alarm to prevent repeated alerts

    def set_alarm(self, instance):
        self.alarm_time = self.alarm_input.text.strip()
        try:
            datetime.strptime(self.alarm_time, '%H:%M:%S')  # Validate time format
            self.status_label.text = f"Alarm set for {self.alarm_time}"
        except ValueError:
            self.status_label.text = "Invalid time format! Use HH:MM:SS"

    def play_alarm_sound(self):
        # This is a placeholder for playing a sound.
        # Replace with actual sound playing logic if needed.
        import winsound
        for i in range(5):  # Beep 5 times
            winsound.Beep(1000, 500)
            time.sleep(0.5)

if __name__ == '__main__':
    AlarmApp().run()

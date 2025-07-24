from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class DynamicLabelsApp(App):
    status_text = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_button = Button(text=name)
            temp_button.bind(on_press=self.press_entry)
            temp_button.background_color = (1, 0, 0, 1)
            self.root.ids.main.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.text
        instance.background_color = (1, 0, 1, 1)
        self.status_text = f"{name}'s number is {self.names[name]}"
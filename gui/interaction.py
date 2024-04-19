from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class InteractiveApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        label = Label(text="Click the button:")
        button = Button(text="Click Me!")

        button.bind(on_press=self.on_button_click)

        layout.add_widget(label)
        layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        instance.text = "Button Clicked!"

if __name__ == "__main__":
    InteractiveApp().run()
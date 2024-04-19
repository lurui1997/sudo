from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Line


class SudokuApp(App):
    def build(self):
        layout = GridLayout(cols=1)

        sudoku_layout = GridLayout(cols=3, rows=3, spacing=[5, 5])
        for i in range(9):
            subgrid = GridLayout(cols=3, spacing=[3, 3])
            for j in range(9):
                button = Button(text=str(i * 9 + j), background_normal='', background_color=(0.4, 0.4, 0.4, 1), border=[1, 1, 1, 1])  # 设置边框为白色
                button.bind(on_press=self.on_button_click)
                subgrid.add_widget(button)
            sudoku_layout.add_widget(subgrid)
        layout.add_widget(sudoku_layout)

        control_layout = GridLayout(cols=14, size_hint_y=0.2)

        mark_button = Button(text="Mark", background_color=(0.8, 0.8, 0.8, 1))
        mark_button.bind(on_press=lambda x: self.mark())
        control_layout.add_widget(mark_button)

        add_button = Button(text="Add Number", background_color=(0.8, 0.8, 0.8, 1))
        add_button.bind(on_press=lambda x: self.add_number())
        control_layout.add_widget(add_button)

        delete_button = Button(text="Delete Number", background_color=(0.8, 0.8, 0.8, 1))
        delete_button.bind(on_press=lambda x: self.delete_number())
        control_layout.add_widget(delete_button)

        undo_button = Button(text="Undo", background_color=(0.8, 0.8, 0.8, 1))
        undo_button.bind(on_press=lambda x: self.undo())
        control_layout.add_widget(undo_button)

        hint_button = Button(text="Hint", background_color=(0.8, 0.8, 0.8, 1))
        hint_button.bind(on_press=lambda x: self.give_hint())
        control_layout.add_widget(hint_button)

        layout.add_widget(control_layout)

        number_buttons_layout = GridLayout(cols=9, size_hint_y=0.2)
        for i in range(1, 10):
            number_button = Button(text=str(i), background_color=(0.8, 0.8, 0.8, 1))
            number_button.bind(on_press=lambda x, num=i: self.number_pressed(num))
            number_buttons_layout.add_widget(number_button)

        layout.add_widget(number_buttons_layout)

        return layout

    def on_button_click(self, instance):
        print(f"Button {instance.text} clicked")

    def mark(self):
        print("Mark")

    def add_number(self):
        print("Add Number")

    def delete_number(self):
        print("Delete Number")

    def undo(self):
        print("Undo")

    def give_hint(self):
        print("Give Hint")

    def number_pressed(self, num):
        print(f"Number {num} pressed")


if __name__ == '__main__':
    SudokuApp().run()

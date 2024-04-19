from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.metrics import dp
import random

base = 3
side = base * base
nums = random.sample(range(1, base * base + 1), base * base)


def pattern(r, c):
    return (base * (r % base) + r // base + c) % side


rBase = range(base)
rows = [g * base + r for g in random.sample(rBase, len(rBase)) for r in random.sample(rBase, len(rBase))]
cols = [g * base + c for g in random.sample(rBase, len(rBase)) for c in random.sample(rBase, len(rBase))]

board = [[nums[pattern(r, c)] for c in cols] for r in rows]

squares = side * side
empties = squares * 3 // 4
for p in random.sample(range(squares), empties):
    board[p // side][p % side] = 0


class SudokuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.labels = []
        for row in board:
            row_labels = []
            for cell in row:
                label = Label(text=str(cell) if cell != 0 else '.', size_hint=(1, 1))
                row_labels.append(label)
                layout.add_widget(label)
            self.labels.append(row_labels)

        input_row = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.text_input = TextInput(hint_text='Enter value (1-9)')
        self.text_input.size_hint = (0.7, 1)
        input_row.add_widget(self.text_input)

        add_button = Button(text='Add')
        add_button.size_hint = (0.3, 1)
        add_button.bind(on_press=self.add_value)

        input_row.add_widget(add_button)
        layout.add_widget(input_row)

        return layout

    def add_value(self, instance):
        try:
            value = int(self.text_input.text)
            if value in range(1, 10):
                row = random.randint(0, side - 1)
                col = random.randint(0, side - 1)
                board[row][col] = value
                self.labels[row][col].text = str(value)
                self.text_input.text = ''
            else:
                print('Please enter a number between 1 and 9.')
        except ValueError:
            print('Invalid input. Please enter a number.')


if __name__ == '__main__':
    SudokuApp().run()
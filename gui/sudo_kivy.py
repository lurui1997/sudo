import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

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
        self.labels = [Label(text=" ".join(str(cell) if cell != 0 else '.' for cell in row)) for row in board]
        for label in self.labels:
            layout.add_widget(label)
        return layout

if __name__ == '__main__':
    SudokuApp().run()
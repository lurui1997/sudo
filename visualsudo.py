import tkinter as tk
import random


class SudokuGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Game")

        self.board = None
        self.generate_sudoku('medium')

        self.create_board()

        self.difficulty_label = tk.Label(self.master, text="Choose Difficulty:")
        self.difficulty_label.grid(row=9, column=0, columnspan=9)

        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("medium")

        difficulties = {"Easy": "easy", "Medium": "medium", "Hard": "hard"}

        for i, (text, difficulty) in enumerate(difficulties.items()):
            radio_button = tk.Radiobutton(self.master, text=text, variable=self.difficulty_var, value=difficulty,
                                          command=self.change_difficulty)
            radio_button.grid(row=10, column=i)

    def generate_sudoku(self, difficulty):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.solve_sudoku()  # Generate a complete sudoku board
        self.remove_cells(difficulty)  # Remove cells based on difficulty

    def solve_sudoku(self):
        # Backtracking algorithm to solve the sudoku
        self.solve(0, 0)

    def solve(self, row, col):
        if row == 9:  # Finished solving all rows
            return True
        if col == 9:  # Finished solving current row, move to next row
            return self.solve(row + 1, 0)
        if self.board[row][col] != 0:  # Cell already has a number, go to next cell
            return self.solve(row, col + 1)

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.solve(row, col + 1):
                    return True
                self.board[row][col] = 0  # Backtrack

        return False

    def is_valid(self, row, col, num):
        # Check if the number is not repeated in row, column, and 3x3 grid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        return all(num != self.board[row][j] for j in range(9)) and \
            all(num != self.board[i][j] for i in range(start_row, start_row + 3) for j in
                range(start_col, start_col + 3))

    def remove_cells(self, difficulty):
        if difficulty == 'easy':
            num_cells = 40  # Easy difficulty
        elif difficulty == 'medium':
            num_cells = 50  # Medium difficulty
        elif difficulty == 'hard':
            num_cells = 60  # Hard difficulty

        for _ in range(num_cells):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0

    def create_board(self):
        for i in range(9):
            for j in range(9):
                cell_value = self.board[i][j]
                cell_entry = tk.Entry(self.master, width=2, font=('Arial', 16))
                cell_entry.grid(row=i, column=j)
                if cell_value != 0:
                    cell_entry.insert(0, str(cell_value))

    def change_difficulty(self):
        difficulty = self.difficulty_var.get()
        self.generate_sudoku(difficulty)
        self.create_board()


root = tk.Tk()
game = SudokuGame(root)
root.mainloop()

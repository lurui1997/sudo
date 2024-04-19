import random


def generate_sudoku():
    base = 3
    side = base * base

    def pattern(r, c): return (base * (r % base) + r // base + c) % side

    def shuffle(s): return random.sample(s, len(s))

    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]

    nums = shuffle(range(1, base * base + 1))

    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    squares = side * side
    empties = squares * 3 // 4
    for p in random.sample(range(squares), empties):
        board[p // side][p % side] = 0

    return board


def print_board(board):
    for row in board:
        print(" ".join(str(cell) if cell != 0 else '.' for cell in row))


def is_valid_move(board, row, col, num):
    # Check if the number is not repeated in row, column, and 3x3 subgrid
    return all(num != board[row][j] for j in range(9)) and \
        all(num != board[i][col] for i in range(9)) and \
        all(num != board[r][c] for r in range(row - row % 3, row - row % 3 + 3) for c in
            range(col - col % 3, col - col % 3 + 3))


def game_difficulty():
    difficulty = input("Choose difficulty (easy, medium, hard): ")
    if difficulty not in ['easy', 'medium', 'hard']:
        print("Invalid difficulty level. Please choose again.")
        return game_difficulty()
    return difficulty


def play_sudoku():
    difficulty = game_difficulty()
    board = generate_sudoku()

    print("Generated Sudoku Puzzle:")
    print_board(board)

    while True:
        row = int(input("Enter the row (0-8) where you want to place a number: "))
        col = int(input("Enter the column (0-8) where you want to place a number: "))
        num = int(input("Enter the number (1-9) to place: "))

        if is_valid_move(board, row, col, num):
            board[row][col] = num
        else:
            print("Invalid move. Try again.")

        print_board(board)

        if all(all(cell != 0 for cell in row) for row in board):
            print("Congratulations! You have solved the Sudoku puzzle!")
            break


if __name__ == "__main__":
    play_sudoku()

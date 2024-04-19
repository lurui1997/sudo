import random

def print_board(board):
    for row in board:
        print(row)

def is_valid(board, num, row, col):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, num, row, col):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_sudoku(difficulty):
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)

    if difficulty == '入门':
        empty_cells = 30
    elif difficulty == '专业':
        empty_cells = 40
    elif difficulty == '大师':
        empty_cells = 50
    elif difficulty == '巅峰':
        empty_cells = 60
    else:
        print('错误的难度级别')
        return None

    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)

    for i in range(empty_cells):
        row, col = cells[i]
        board[row][col] = 0

    return board

# 生成一个入门级别的数独题目
board = generate_sudoku('入门')
print_board(board)

def print_board(board):
    for row in board:
        print(row)

def is_valid(board, num, row, col):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, num, row, col):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_sudoku(difficulty):
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)

    # 根据难度级别确定要清空的格子数量
    if difficulty == '入门':
        empty_cells = 30
    elif difficulty == '专业':
        empty_cells = 40
    elif difficulty == '大师':
        empty_cells = 50
    elif difficulty == '巅峰':
        empty_cells = 60
    else:
        print('错误的难度级别')
        return None

    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)

    for i in range(empty_cells):
        row, col = cells[i]
        board[row][col] = 0

    return board

# 生成一个大师级别的数独题目
board = generate_sudoku('大师')

while True:
    print_board(board)
    row = int(input("请输入要填入数字的行数(1-9): ")) - 1
    col = int(input("请输入要填入数字的列数(1-9): ")) - 1
    num = int(input("请输入要填入的数字(1-9): "))

    if is_valid(board, num, row, col):
        board[row][col] = num
    else:
        print("填入的数字与已有数字冲突，请重新输入。")

    # 判断是否已经完全填入数字
    if all(all(cell != 0 for cell in row) for row in board):
        print("恭喜，数独题目已完成！")
        break
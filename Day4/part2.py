class BingoBoard:
    
    def __init__(self, input_list):
        self.grid = input_list

    def check_win(self):
        for i in range(5):
            if self.check_col(i) or self.check_row(i):
                return True
        return False

    def sum_unmarked(self):
        return sum([value for value in self.grid if value != 'x'])

    def check_col(self, col):
        for i in range(col, 25, 5):
            if self.grid[i] != 'x':
                return False
        return True

    def check_row(self, row):
        for value in self.grid[row*5:row*5+5]:
            if value != 'x':
                return False
        return True

    def check_number(self, number):
        try:
            self.grid[self.grid.index(number)] = 'x'
        except:
            return


with open('Day4/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]

random_numbers = [int(d) for d in data[0].split(',')]
bingo_boards = []

for d in data[1:]:
    if d == "":
        bingo_boards.append([])
    else:
        tmp_values = [int(v) for v in d.split()]
        bingo_boards[-1].extend(tmp_values)


bingo_boards = [BingoBoard(board) for board in bingo_boards]
winning_board = None
winning_number = None
boards_to_remove = []

for number in random_numbers:
    
    for i, board in enumerate(bingo_boards):
        board.check_number(number)
        if board.check_win():
            if len(bingo_boards) > 1:
                boards_to_remove.append(board)
            else:
                winning_number = number
                winning_board = board
    
    for board in boards_to_remove:
        bingo_boards.remove(board)
    boards_to_remove = []

    if winning_number:
        break


print(winning_board.grid)
print(winning_number)
print(winning_board.sum_unmarked() * winning_number)

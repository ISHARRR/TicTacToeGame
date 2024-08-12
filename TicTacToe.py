class TicTacToe:
    def __init__(self):
        # List comprehension is not my code
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            # List comprehension is not my code
            print(' | '.join([cell if cell != '' else ' ' for cell in row]))
            print('-' * 9)
        print('*' * 9)

    def make_move(self, row, col):
        row -= 1
        col -= 1

        if self.board[row][col] == '':
            print(f"Placing {self.current_player} at position ({row + 1}, {col + 1}).")
            self.board[row][col] = self.current_player
            self.print_board()  # Print the board every move
            self.switch_player()  # Switch player after a valid move
            return True
        else:
            print(f"({row + 1}, {col + 1}) is already in play. Try again.")
            self.print_board()
        return False

    def switch_player(self):
        print(f"Switching player")
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        print(f"It is now player {self.current_player}'s turn.")

    def check_winner(self):
        # if statements used to check for a winner are not entirely my code
        print("Checking for a winner.")
        print("Checking rows.")
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                print(f"{self.board[i][0]} wins on row {i + 1}.")
                return self.board[i][0]

        print("Checking columns.")
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                print(f"{self.board[0][i]} wins on column {i + 1}.")
                return self.board[0][i]

        print("Checking diagonals.")
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            print("Wins on the diagonal - top-left to bottom-right.")
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            print("Wins on the diagonal - top-right to bottom-left.")
            return self.board[0][2]

        print("Checking for a Draw.")
        if all(cell != '' for row in self.board for cell in row):
            return 'Draw'

        print("No winner yet.")
        return None
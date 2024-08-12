from TicTacToe import TicTacToe

if __name__ == "__main__":
    game = TicTacToe()

    while True:
        game.print_board()
        row = int(input("Choose a row (1, 2, or 3): "))
        col = int(input("Choose a column (1, 2, or 3): "))

        if not game.make_move(row, col):
            print("Invalid move. Try again.")
            continue

        winner = game.check_winner()
        if winner:
            game.print_board()
            if winner == 'Tie':
                print("YOU BOTH TIED!")
            else:
                print(f"Player {winner} is the WINNERRRRR!")
            break

        game.switch_player()
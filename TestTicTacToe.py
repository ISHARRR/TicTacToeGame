import unittest
from TicTacToe import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    def tearDown(self):
        # Reset the game between tests
        self.game = TicTacToe()

    def test_initial_state(self):
        self.assertEqual(self.game.board, [['', '', ''], ['', '', ''], ['', '', '']])
        self.assertEqual(self.game.current_player, 'X')

    def test_make_move(self):
        self.assertTrue(self.game.make_move(1, 1))
        self.assertEqual(self.game.board[0][0], 'X')
        self.assertFalse(self.game.make_move(1, 1))

    def test_switch_player(self):
        self.game.make_move(1, 1)
        self.assertEqual(self.game.current_player, 'O')

    def test_row_winner(self):
        self.game.make_move(0, 0)
        self.game.make_move(1, 0)
        self.game.make_move(0, 1)
        self.game.make_move(1, 1)
        self.game.make_move(0, 2)
        self.assertEqual(self.game.check_winner(), 'X')

    def test_column_winner(self):
        self.game.make_move(0, 0)
        self.game.make_move(0, 1)
        self.game.make_move(1, 0)
        self.game.make_move(1, 1)
        self.game.make_move(2, 0)
        self.assertEqual(self.game.check_winner(), 'X')

    def test_diagonal_winner(self):
        self.game.make_move(0, 0)
        self.game.make_move(0, 1)
        self.game.make_move(1, 1)
        self.game.make_move(1, 0)
        self.game.make_move(2, 2)
        self.assertEqual(self.game.check_winner(), 'X')

    def test_tie_game(self):
        self.game.board = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]
        self.assertEqual(self.game.check_winner(), 'Draw')
# TicTacToe AI Move
This is a Python implementation of a TicTacToe game with AI moves. The game is played between a human player and the computer AI, where the human player is represented by 'X' and the computer AI is represented by 'O'.

The AI move is implemented using the minimax algorithm. The algorithm calculates the best move for the AI player by recursively calculating the best score for each possible move. The algorithm assumes that the human player will make the best possible move at every turn, and thus tries to minimize the human player's score while maximizing its own.

The game board is represented as follows:

```
0 | 1 | 2
3 | 4 | 5
6 | 7 | 8
```
The `TicTacToe` class contains the following methods:

- `__init__(self, board=None)`: Initializes the TicTacToe game with a board. If no board is provided, an empty board is created.

- `set_board(self, board)`: Sets the game board to the provided board.

- `get_board(self)`: Returns the current game board.

- `get_empty_cells(self)`: Returns a list of empty cells on the game board.

- `is_draw(self)`: Returns True if the game is a draw, False otherwise.

- `is_over(self)`: Returns True if the game is over, False otherwise.

- `get_winner(self)`: Returns the winner of the game, or None if there is no winner.

- `get_move(self)`: Returns the best move for the AI player.

- `__str__(self)`: Returns a string representation of the game board.

- `player_move(self)`: Allows the human player to make a move.
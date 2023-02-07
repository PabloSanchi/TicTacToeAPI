import copy

def minimax(board, depth, is_maximizing):
    if board.is_over():
        if board.get_winner() == board.ai:
            # print('Gano')
            # print(board)
            return 100
        else:
            return -100
    
    if board.is_draw():
        return 0

    best_score = -1000 if is_maximizing else 1000
    for i in board.get_empty_cells():
        board.board[i] = board.ai if is_maximizing else board.player
        score = minimax(copy.deepcopy(board), depth+1, not is_maximizing)
        board.board[i] = ''
        best_score = max(score, best_score) if is_maximizing else min(score, best_score)

    return best_score


class TicTacToe:
    '''
    'X' player
    'O' minimax
    board representation
    0 | 1 | 2
    3 | 4 | 5
    6 | 7 | 8
    '''
    def __init__(self, board=None):
        self.board = board
        self.ai = 'O'
        self.player = 'X'
    
    def set_board(self, board):
        self.board = board

    def get_board(self):
        return self.board

    def get_empty_cells(self):
        cells = []
        for idx, val in enumerate(self.board):
            if val == '':
                cells.append(idx)

        return cells

    def is_draw(self):
        if '' not in self.board:
            return True
        return False

    def is_over(self):
        
        # check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] and self.board[i] != '':
                return True
        
        # check cols
        for i in range(0, 3):
            if self.board[i] == self.board[i+3] == self.board[i+6] and self.board[i] != '':
                return True

        # check diagonals
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != '':
            return True

        if self.board[2] == self.board[4] == self.board[6] and self.board[2] != '':
            return True

        return False

    def get_winner(self):
        # check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] and self.board[i] != '':
                return self.board[i]
        
        # check cols
        for i in range(0, 3):
            if self.board[i] == self.board[i+3] == self.board[i+6] and self.board[i] != '':
                return self.board[i]

        # check diagonals
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != '':
            return self.board[0]

        if self.board[2] == self.board[4] == self.board[6] and self.board[2] != '':
            return self.board[2]

        return None

    def get_move(self):
        best_score = -1000
        best_move = None

        for i in self.get_empty_cells():
            self.board[i] = self.ai # make the move
            cp = copy.deepcopy(self)
            newSelf = copy.deepcopy(self)
            score = minimax(newSelf, 0, False)
            self.board[i] = '' # remove the move

            if score > best_score:
                best_score = score
                best_move = i

        return best_move

    def __str__(self):
        return f'''
        {self.board[0]} | {self.board[1]} | {self.board[2]}
        {self.board[3]} | {self.board[4]} | {self.board[5]}
        {self.board[6]} | {self.board[7]} | {self.board[8]}
        '''

    def player_move(self):
        print(f'Enter a number between 0 and 8 to make a move: ')
        move = int(input())
        if self.board[move] == '':
            self.board[move] = self.player 

# if __name__ == '__main__':
#     ai = TicTacToe(['', '', 'X', '', '', '', '', '', ''])
    
#     print(ai)
#     print('PLAY TIC TAC TOE')
    
#     while(not ai.is_over()):    
#         ai.player_move()
#         print(ai)
#         if not ai.is_over():
#             ai.board[ai.get_move()] = ai.ai
#         print(ai)
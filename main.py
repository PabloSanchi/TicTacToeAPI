from flask import Flask, request
from flask_cors import CORS
from tictactoe import TicTacToe
import json

# create the Flask app
app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/", methods=['GET'])
def root():
    return {"message": "TicTacToe AI"}

@app.route("/aimove", methods=['POST'])
def aimove(): # request : Request
    board = request.json
    board = board['board']

    tictactoe = TicTacToe(board)

    move = None
    if not tictactoe.is_over() and not tictactoe.is_draw():
        move = tictactoe.get_move()
        tictactoe.board[move] = tictactoe.ai
    
    return {
        "move": move, 
        "board": tictactoe.board,
        "over": tictactoe.is_over(),
        "tie": tictactoe.is_draw(),
        "winner": tictactoe.get_winner()
    }

@app.route("/playermove", methods=['POST'])
def playermove():
    # get the body
    board = request.json
    print(board)

if __name__ == "__main__":
    app.run()
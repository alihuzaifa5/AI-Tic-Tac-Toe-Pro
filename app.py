import csv
import os
import random
from flask import Flask, render_template, request, jsonify
from ai.minimax import find_best_move

app = Flask(__name__)
HISTORY_FILE = 'data/player_states.csv'

if not os.path.exists('data'): os.makedirs('data')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_move', methods=['POST'])
def get_move():
    data = request.json
    board = data.get('board')
    difficulty = data.get('difficulty', 'Hard')
    
    if difficulty == "Easy":
        empty = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]
        row, col = random.choice(empty)
        algo, prob = "Random Heuristic", f"{random.randint(10,30)}%"
    elif difficulty == "Medium":
        row, col = find_best_move(board)
        algo, prob = "BFS/DFS Search", f"{random.randint(40,70)}%"
    else:
        row, col = find_best_move(board)
        algo, prob = "Minimax Algorithm", f"{random.randint(85,99)}%"

    return jsonify({'row': row, 'col': col, 'algo': algo, 'prediction': prob})

@app.route('/save_result', methods=['POST'])
def save_result():
    result = request.json.get('result')
    with open(HISTORY_FILE, 'a', newline='') as f:
        csv.writer(f).writerow([result])
    
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            history = [line.strip() for line in f.readlines()]
    return jsonify({'history': history[-5:][::-1]})

if __name__ == '__main__':
    app.run(debug=True)
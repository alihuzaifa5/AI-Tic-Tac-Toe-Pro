# AI Tic-Tac-Toe Pro

A browser-based Tic-Tac-Toe game powered by Flask and an AI opponent. Play as `X` against the computer as `O`, choose a difficulty level, view the algorithm used for the move, and keep a lightweight match history in CSV format.

## Repository Description

> A Flask-powered AI Tic-Tac-Toe game with Easy, Medium, and Hard difficulty modes, Minimax decision-making, move prediction details, and persistent CSV match history.

## Features

- Interactive 3x3 Tic-Tac-Toe board
- Human player as `X` versus AI as `O`
- Three selectable difficulty modes:
  - **Easy:** chooses a random available move
  - **Medium:** presents the BFS/DFS search mode in the interface
  - **Hard:** uses the Minimax algorithm to choose the best move
- Win, loss, and draw detection
- AI algorithm and prediction percentage displayed after each move
- Persistent match history stored in `data/player_states.csv`
- Player and AI score counters for the current browser session
- Responsive glass-style browser interface

## Built With

- Python
- Flask
- JavaScript
- HTML5
- CSS3
- CSV file storage

## Getting Started

### Prerequisites

- Python 3.10 or newer
- `pip`
- A modern web browser

### Installation

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   cd <your-repository-directory>
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment.

   Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   macOS or Linux:

   ```bash
   source .venv/bin/activate
   ```

4. Install the dependency:

   ```bash
   python -m pip install Flask
   ```

### Run the Application

```bash
python app.py
```

Open the local address shown by Flask, usually:

```text
http://127.0.0.1:5000
```

## How to Play

1. Select `Easy`, `Medium`, or `Hard` from the difficulty menu.
2. Click an empty square to place `X`.
3. Wait for the AI to place `O`.
4. Continue until a player wins or the board is full.
5. Use **Restart Match** to start another round.

Completed games are appended to `data/player_states.csv`. The interface displays the five most recent results in reverse chronological order.

## Project Structure

```text
.
├── app.py                    # Flask routes and game API
├── ai/
│   ├── minimax.py            # Minimax move selection
│   ├── bfs_dfs.py            # Search-based AI helpers
│   └── regression.py         # Win-rate prediction utilities
├── data/
│   └── player_states.csv     # Saved game results
├── static/
│   ├── script.js             # Board interaction and API calls
│   └── style.css             # Shared stylesheet
└── templates/
    └── index.html            # Game interface
```

## API Endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/` | Serves the game interface |
| `POST` | `/get_move` | Returns the AI's selected move and algorithm details |
| `POST` | `/save_result` | Saves a completed result and returns recent history |

Example request to `/get_move`:

```json
{
  "board": [["X", "", ""], ["", "O", ""], ["", "", ""]],
  "difficulty": "Hard"
}
```

## Data and Privacy

Match history is stored locally in a CSV file. No account, external database, or third-party analytics service is required.

## License

This project is available under the license included in the repository.

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import os

# Absolute path to CSV
DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "player_stats.csv")


def predict_win_rate():
    """Predict future win rate using Linear Regression"""
    df = pd.read_csv(DATA_FILE)

    if len(df) < 1:
        return 0.0

    X = df[["games"]]
    y = df["wins"] / df["games"].replace(0, 1)

    model = LinearRegression()
    model.fit(X, y)

    next_game = np.array([[df["games"].iloc[-1] + 1]])
    prediction = model.predict(next_game)

    return round(float(prediction[0]) * 100, 2)


def update_player_stats(result):
    """Update CSV after each game"""
    df = pd.read_csv(DATA_FILE)

    games = df.at[0, "games"] + 1
    wins = df.at[0, "wins"]
    losses = df.at[0, "losses"]
    draws = df.at[0, "draws"]

    if result == "X":
        wins += 1
    elif result == "O":
        losses += 1
    else:
        draws += 1

    df.loc[0] = [games, wins, losses, draws]
    df.to_csv(DATA_FILE, index=False)
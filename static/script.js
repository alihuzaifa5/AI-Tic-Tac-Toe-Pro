let board = [["","",""],["","",""],["","",""]];
let gameActive = true;
let pScore = 0;
let aScore = 0;

async function cellClicked(e) {
    const r = e.target.dataset.row;
    const c = e.target.dataset.col;
    if (board[r][c] !== "" || !gameActive) return;

    // 1. Player Move
    updateCell(r, c, "X");
    
    if (gameActive) {
        document.getElementById('status').innerText = "AI is thinking...";
        const diff = document.getElementById('difficulty-select').value;

        // 2. Fetch AI Move
        const response = await fetch('/get_move', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({board: board, difficulty: diff})
        });
        const data = await response.json();
        
        // 3. Update Technical Info Sidebar
        document.getElementById('algo-display').innerText = data.algo;
        document.getElementById('predict-display').innerText = data.prediction;
        
        // 4. Execute AI Move with a small delay for realism
        setTimeout(() => updateCell(data.row, data.col, "O"), 500);
    }
}

function updateCell(r, c, player) {
    board[r][c] = player;
    const el = document.querySelector(`[data-row="${r}"][data-col="${c}"]`);
    el.innerText = player;
    el.classList.add(player.toLowerCase()); // Triggers the CSS animation
    checkGameStatus();
}

function checkGameStatus() {
    const lines = [
        [[0,0],[0,1],[0,2]], [[1,0],[1,1],[1,2]], [[2,0],[2,1],[2,2]],
        [[0,0],[1,0],[2,0]], [[0,1],[1,1],[2,1]], [[0,2],[1,2],[2,2]],
        [[0,0],[1,1],[2,2]], [[0,2],[1,1],[2,0]]
    ];
    for (let line of lines) {
        const [a, b, c] = line;
        if (board[a[0]][a[1]] && board[a[0]][a[1]] === board[b[0]][b[1]] && board[a[0]][a[1]] === board[c[0]][c[1]]) {
            announceWinner(board[a[0]][a[1]]);
            return;
        }
    }
    if (!board.flat().includes("")) announceWinner("Draw");
}

async function announceWinner(winner) {
    gameActive = false;
    let resultText = winner === "Draw" ? "Draw" : (winner === "X" ? "Player Won" : "AI Won");
    document.getElementById('status').innerText = resultText;

    // Save to CSV History
    const resp = await fetch('/save_result', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ result: resultText })
    });
    const data = await resp.json();
    
    // Update History Box
    document.getElementById('history-list').innerHTML = data.history.map(h => `<div>• ${h}</div>`).join("");
    
    // Update Score Counters
    if(winner === "X") document.getElementById('p-score').innerText = ++pScore;
    if(winner === "O") document.getElementById('a-score').innerText = ++aScore;
}

function resetGame() {
    board = [["","",""],["","",""],["","",""]];
    gameActive = true;
    document.getElementById('status').innerText = "Your Turn (X)";
    document.querySelectorAll('.cell').forEach(c => {
        c.innerText = "";
        c.className = "cell"; // Removes 'x' and 'o' classes to reset animations
    });
}

document.querySelectorAll('.cell').forEach(c => c.addEventListener('click', cellClicked));
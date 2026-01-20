# Memory Drift

Interactive memory game that flashes a sequence of digits for you to repeat. It runs entirely in the browser, with optional Python-powered logic via Pyodide and a JavaScript fallback.

- Adaptive difficulty: sequence length and timer scale with your streak, failures, and speed.
- Four sequence styles: random, primes, fibonacci digits, and mirror patterns.
- Daily/weekly challenges, achievements, and local high-score storage (localStorage).
- Keyboard or on-screen keypad input, with responsive layout that fits desktop and mobile.
- Pyodide-backed Python logic from `sequence_logic.py`, falling back to equivalent JS if unavailable.

## Project structure

- `memory_drift.html` — UI, styling, and game logic (Pyodide init, JS fallback, achievements, challenges, high scores).
- `sequence_logic.py` — Python helpers for sequence generation, per-round config, scoring, and result messaging (run through Pyodide).

## Run locally

Use a simple local server so the page can fetch `sequence_logic.py` and load Pyodide:

```bash
cd /Users/srinivasagudi/Desktop/money/Memory_Drift
python3 -m http.server 8000
# then open http://localhost:8000/memory_drift.html
```

Notes:
- First load pulls Pyodide from the CDN; you need network access for that. If it fails, the game automatically uses the JS logic.
- Opening the HTML directly from the file system may block the fetch for `sequence_logic.py`; the local server avoids that.

## How to play

1) Click **Start Game** and read the brief instructions.  
2) Watch the digits flash in order, then repeat them using the keypad or number keys (0-9) before the timer expires.  
3) Each round grows the sequence; beating the target unlocks achievements and updates the scoreboard.  
4) Try the **Sequence style** chips (Random/Primes/Fibonacci/Mirror) or launch the daily/weekly challenge for preset modifiers.

## Editing the Python logic

`sequence_logic.py` powers Pyodide mode. Key entry points:
- `generate_sequence(length, max_digit, mode)` — creates the next sequence.
- `round_config(level, performance)` — returns `{ "length": int, "time": int }` based on progress.
- `score_for_round(seq_len, performance)` — computes points for a round.
- `get_result_message(success, sequence)` — message shown after each attempt.

Update these to experiment with new modes or tuning; the JS fallback mirrors their behavior.

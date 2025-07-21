# balatro-restarter

This is an automation script for the game *Balatro*. Its purpose is to repeatedly restart a run and open Arcana packs obtained from the skips in Ante 1 until it finds the rare **Soul** card, which grants a legendary joker.

## How It Works

The script uses image recognition to automate gameplay:

1. The script repeatedly presses 'R' to restart the game.
2. It then scans the screen to find an Arcana pack.
3. Once an Arcana pack is located, the script opens it.
4. Checks if the Soul card is in the pack.
5. If it isn't there, the script runs again.
6. If it is found, the script stops and logs that it found the card.

The entire process is triggered by pressing the `X1` side mouse button.

## Requirements

*   **Python:** 3.12
*   **Libraries:** All necessary libraries are listed in the `requirements.txt` file.

## Setup and Usage

1.  **Install Dependencies:**
    ```
    # given packages are compatible with Python 3.12 
    pip install -r requirements.txt
    ```
2.  **Run the Script:**
    ```
    python main.py
    ```
3.  **Start Automation:** Once the script is running, while in game, press the **X1 mouse button** to begin the search. The script will take over mouse and keyboard control to perform the tasks. To stop it, you can close the terminal window or move mouse to one of the corners of your screen.

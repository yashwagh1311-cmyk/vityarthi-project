LogicQuest: Modular Number Guessing System

📋 Project Overview

LogicQuest is a modular Python application designed to demonstrate event-driven programming and state management. Unlike simple scripts, this project uses a separated architecture (Logic vs. UI vs. Data) to ensure scalability and maintainability.

🚀 Key Features

Modular Architecture: Separation of concerns between Game Logic (game_logic.py) and User Interface (ui.py).

Data Persistence: A dedicated ScoreManager class handles file I/O to save high scores.

Robust Error Handling: Input validation prevents crashes on non-numeric or empty inputs.

Configurable Settings: All game constants (Range, Attempts) are managed in config.py.

🛠️ Technologies Used

Language: Python 3.x

GUI Framework: Tkinter

Design Pattern: Model-View-Controller (MVC) inspired structure.

⚙️ Steps to Install & Run

Clone the Repository:

git clone 

Navigate to Directory:

cd LogicQuest


Run the Application:

python main.py


🧪 Instructions for Testing

Range Test: Enter numbers < 1 or > 50. Expected: Error Message.

Type Test: Enter "abc". Expected: Error Message.

Win Test: Guess the number correctly. Expected: High score updates in highscore.txt.

📸 Screenshots

Below is a preview of the game running:

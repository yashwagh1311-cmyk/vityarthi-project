import tkinter as tk
from tkinter import messagebox
from config import *
from game_logic import NumberGame
from statistics import ScoreManager

class GameUI:
    def __init__(self, root):
        self.root = root
        self.game = NumberGame()
        self.root.title(GAME_TITLE)
        self.root.geometry(WINDOW_SIZE)
        self.root.configure(bg=BG_COLOR)
        
        self.setup_widgets()
        self.update_display()

    def setup_widgets(self):
        # Title
        tk.Label(self.root, text="LogicQuest", font=("Helvetica", 30, "bold"), bg=BG_COLOR).pack(pady=20)
        
        # High Score Display
        self.highscore_label = tk.Label(self.root, text=f"High Score: {ScoreManager.get_highscore()}", font=("Arial", 12), bg=BG_COLOR)
        self.highscore_label.pack()

        # Input
        self.entry_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.entry_var, font=("Arial", 30), width=5, justify='center').pack(pady=20)

        # Button
        tk.Button(self.root, text="CHECK GUESS", command=self.process_guess, bg="#4CAF50", fg="white", font=("Arial", 15)).pack(pady=10)

        # Feedback
        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 18), bg="white", width=30, height=2)
        self.feedback_label.pack(pady=20)

        # Stats
        self.attempts_label = tk.Label(self.root, text="", font=("Arial", 14), bg=BG_COLOR)
        self.attempts_label.pack(pady=10)

        # Reset
        tk.Button(self.root, text="Reset Game", command=self.reset_ui, bg="#ddd").pack(side=tk.BOTTOM, pady=20)

    def process_guess(self):
        if self.game.is_game_over:
            messagebox.showinfo("Info", "Please reset the game to play again.")
            return

        result = self.game.check_guess(self.entry_var.get())
        self.feedback_label.config(text=result['message'])
        
        if result['win']:
            # Calculate Score based on attempts left
            score = self.game.attempts_left * 10
            if ScoreManager.save_highscore(score):
                messagebox.showinfo("New Record!", f"New High Score: {score}")
            self.reset_ui()
        
        self.update_display()

    def reset_ui(self):
        self.game.reset_game()
        self.entry_var.set("")
        self.update_display()

    def update_display(self):
        self.highscore_label.config(text=f"High Score: {ScoreManager.get_highscore()}")
        self.attempts_label.config(text=f"Attempts Left: {self.game.attempts_left}")
import tkinter as tk
from ui import GameUI

# This is the entry point of the application
if __name__ == "__main__":
    root = tk.Tk()
    app = GameUI(root)
    root.mainloop()
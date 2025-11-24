import os
from config import SCORE_FILE

class ScoreManager:
    """Handles reading and writing high scores to a file."""
    
    @staticmethod
    def save_highscore(score):
        try:
            current_high = ScoreManager.get_highscore()
            if score > current_high:
                with open(SCORE_FILE, "w") as f:
                    f.write(str(score))
                return True
        except Exception as e:
            print(f"Error saving score: {e}")
        return False

    @staticmethod
    def get_highscore():
        if not os.path.exists(SCORE_FILE):
            return 0
        try:
            with open(SCORE_FILE, "r") as f:
                return int(f.read().strip())
        except:
            return 0
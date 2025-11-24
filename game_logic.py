import random
from config import MIN_NUMBER, MAX_NUMBER, MAX_ATTEMPTS

class NumberGame:
    """Core game logic independent of GUI."""
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        self.attempts_left = MAX_ATTEMPTS
        self.is_game_over = False
        self.status_message = f"Guess between {MIN_NUMBER} and {MAX_NUMBER}"

    def check_guess(self, user_input):
        """
        Validates guess and returns a status dict.
        Returns: {'success': bool, 'message': str, 'win': bool}
        """
        try:
            guess = int(user_input)
        except ValueError:
            return {'success': False, 'message': "Error: Not a number!", 'win': False}

        if not (MIN_NUMBER <= guess <= MAX_NUMBER):
            return {'success': False, 'message': f"Error: Range {MIN_NUMBER}-{MAX_NUMBER}", 'win': False}

        self.attempts_left -= 1

        if guess == self.secret_number:
            self.is_game_over = True
            return {'success': True, 'message': "CORRECT! You Win!", 'win': True}
        
        if self.attempts_left <= 0:
            self.is_game_over = True
            return {'success': True, 'message': f"Game Over! It was {self.secret_number}", 'win': False}

        hint = "Too Low!" if guess < self.secret_number else "Too High!"
        return {'success': True, 'message': hint, 'win': False}
import random

class Wordle:
    def __init__(self, word_list):
        self.word_list = set(word_list)
        self.target_word = random.choice(list(self.word_list))
        self.attempts = 6
        self.history = []
        self.wins = 0
        self.total_attempts = 0
        self.games_played = 0
        self.streak = 0
    
    def validate_word(self, word):
        return word.lower() in self.word_list
    
    def check_guess(self, guess):
        if not self.validate_word(guess):
            return "Invalid word. Must be in dictionary."
        
        feedback = ["Gray"] * len(self.target_word)  # Default feedback is "Gray"
        target_word_letters = list(self.target_word)
        guessed_letters = list(guess)
        
        # First pass: Find exact matches (Green)
        for i in range(len(guess)):
            if guessed_letters[i] == target_word_letters[i]:
                feedback[i] = "Green"
                target_word_letters[i] = None  # Mark as used
                guessed_letters[i] = None  # Mark as processed
        
        # Second pass: Find misplaced letters (Yellow)
        for i in range(len(guessed_letters)):
            if guessed_letters[i] and guessed_letters[i] in target_word_letters:
                feedback[i] = "Yellow"
                target_word_letters[target_word_letters.index(guessed_letters[i])] = None  # Mark as used
        
        # Update game state
        self.history.append((guess, feedback))
        self.attempts -= 1
        self.total_attempts += 1
        
        if guess == self.target_word:
            self.wins += 1
            self.streak += 1
            self.games_played += 1
        elif self.attempts == 0:
            self.streak = 0
            self.games_played += 1
        
        return feedback


    
    def is_game_over(self):
        return self.attempts == 0 or any(guess == self.target_word for guess, _ in self.history)
    
    def get_statistics(self):
        avg_attempts = self.total_attempts / self.games_played if self.games_played else 0
        return {"attempts_left": self.attempts, "wins": self.wins, "streak": self.streak, "average_attempts": avg_attempts}
    
    def play(self):
        print("Welcome to Wordle!")
        while not self.is_game_over():
            guess = input("Enter your 5-letter guess: ").lower()
            feedback = self.check_guess(guess)
            print("Feedback:", feedback)
            
            if guess == self.target_word:
                print("Congratulations! You guessed the word!")
                break
        
        if self.attempts == 0:
            print(f"Game over! The word was: {self.target_word}")

if __name__ == "__main__":
    word_list = ['blend', 'lapse', 'flame', 'chime', 'light', 'grass', 'trick', 'flame', 'whale', 'shove',
 'spire', 'frame', 'grape', 'smile', 'space', 'clash', 'swore', 'crisp', 'spore', 'trace',
 'tramp', 'table', 'chase', 'stoke', 'berry', 'vocal', 'bliss', 'brake', 'plane', 'watch',
 'grasp', 'brick', 'pride', 'apple', 'plume', 'waste', 'grace', 'spend', 'mango', 'plaza',
 'plant', 'march', 'flood', 'cheek', 'bride', 'grasp', 'stone', 'prong', 'swipe', 'sharp']

    game = Wordle(word_list)
    game.play()

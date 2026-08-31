import random
# Import the random module to choose the secret word.

# This list stores the visual board states for each incorrect guess count.
wordlepics = [
  """
  ⬜️⬜️⬜️⬜️⬜️
  ⬜️⬜️⬜️⬜️⬜️
  ⬜️⬜️⬜️⬜️⬜️
  ⬜️⬜️⬜️⬜️⬜️
  ⬜️⬜️⬜️⬜️⬜️
  ⬜️⬜️⬜️⬜️⬜️
  """,
  """
  _ _ _ _ _
  ⬜️⬜️⬜️⬜️⬜️
  ⬜️⬜️⬜️⬜️⬜️
  ⬜️⬜️⬜️⬜️⬜️
  ⬜️⬜️⬜️⬜️⬜️
  ⬜️⬜️⬜️⬜️⬜️
  """,
  """
  _ _ _ _ _
  _ _ _ _ _
  ⬜️⬜️⬜️⬜️⬜️
  ⬜️⬜️⬜️⬜️⬜️
  ⬜️⬜️⬜️⬜️⬜️
  ⬜️⬜️⬜️⬜️⬜️
  """,
  """
  _ _ _ _ _
  _ _ _ _ _
  _ _ _ _ _
  ⬜️⬜️⬜️⬜️⬜️
  ⬜️⬜️⬜️⬜️⬜️
  ⬜️⬜️⬜️⬜️⬜️
  """,
  """
  _ _ _ _ _
  _ _ _ _ _
  _ _ _ _ _
  _ _ _ _ _
  ⬜️⬜️⬜️⬜️⬜️
  ⬜️⬜️⬜️⬜️⬜️
  """,
  """
  _ _ _ _ _
  _ _ _ _ _
  _ _ _ _ _
  _ _ _ _ _
  _ _ _ _ _
  ⬜️⬜️⬜️⬜️⬜️
  """
]

# This class handles choosing and filtering valid words from the dictionary.
class words:
  @staticmethod
  def get_dictionary_words():
    """Return alphabetic words from the system dictionary."""
    # Try to open the system dictionary using UTF-8 text encoding.
    try:
      with open("/usr/share/dict/words", encoding="utf-8") as dictionary:
        # Read each line, remove whitespace, convert it to lowercase, and
        # keep only entries made entirely of alphabetic characters.
        return [word.strip().lower() for word in dictionary
            if word.strip().isalpha()]
    except FileNotFoundError:
      # Use a small built-in list when the system dictionary is unavailable.
      return ["cat", "purring", "chicken", "gravy", "mouse"]
  dictionaryword = []
  @classmethod
  def get_random_word(cls):
    # Pick one word at random from the dictionary list.
    return random.choice(cls.dictionaryword)
  @classmethod
  def five_lettered(cls):
    # Keep drawing until a five-letter word is selected.
    daword = cls.get_random_word()
    while len(daword) != 5:
      daword = cls.get_random_word()
    return daword

# Load the dictionary and choose the secret word for this round.
words.dictionaryword = words.get_dictionary_words()
wordle_word = words.five_lettered()

# This class tracks how many incorrect guesses the player has made.
class incorrect_guesses:
  def __init__(self):
    # Start the counter at zero for a fresh game.
    self.count = 0
  def increment(self):
    """Record one incorrect guess and return the updated count."""
    # Increase the wrong-guess count by one.
    self.count += 1
    return self.count
  def reset(self):
    """Reset the counter for a new game."""
    # Reset the count when starting over.
    self.count = 0
  def __int__(self):
    # Convert the object to an integer for comparisons.
    return self.count
  def __lt__(self, other):
    # Compare the current wrong-guess count to a number.
    return self.count < other

# This function runs the full Wordle game loop.
def wordlegame():
  # Print the welcome message and start the game.
  print('Hello, welcome to wordle!')
  print('Guess the word:')
  # Store previously guessed words and letters for tracking.
  guessed_letters = set()
  guessed_words = []
  guessed_results = []
  incorrect_count = incorrect_guesses()
  max_lives = 6
  correct_word = ['⬜️'] * 5

  def evaluate_guess(guess):
    result = ['⬜️'] * 5
    remaining_letters = {}

    # First pass: mark exact matches and count unmatched letters in the answer.
    for index, letter in enumerate(wordle_word):
      if guess[index] == letter:
        result[index] = letter
      else:
        remaining_letters[letter] = remaining_letters.get(letter, 0) + 1

    # Second pass: mark yellow tiles while accounting for duplicate letters.
    for index, letter in enumerate(guess):
      if result[index] != '⬜️':
        continue
      if remaining_letters.get(letter, 0) > 0:
        result[index] = '🟧'
        remaining_letters[letter] -= 1

    return result

  # Draw the current board with guessed rows and empty slots.
  def render_board():
    rows = []
    for i in range(max_lives):
      if i < len(guessed_words):
        rows.append(' '.join(guessed_results[i]))
      else:
        rows.append(' '.join(['⬜️'] * 5))
    print('\n'.join(rows))

  # Keep asking for guesses until the player wins or runs out of turns.
  while incorrect_count < max_lives:
    render_board()
    print(' '.join(correct_word))
    
    # Display incorrect guessed letters
    incorrect_guessed = []
    if guessed_words:
      for i, word in enumerate(guessed_words):
        for j, letter in enumerate(word):
          if guessed_results[i][j] not in ['🟩', '🟧']:
            incorrect_guessed.append(letter)
      if incorrect_guessed:
        print(f'Incorrect letters: {", ".join(set(incorrect_guessed))}')
    
    # Display remaining letters that could be in the word
    remaining = set('abcdefghijklmnopqrstuvwxyz') - guessed_letters
    # Remove incorrect letters from available letters
    remaining -= set(incorrect_guessed)
    if remaining:
      print(f'Available letters: {", ".join(sorted(remaining))}')

    # Read the player's guess and normalize it.
    guess = input('Guess a word: ').strip().lower()
    if len(guess) != 5 or not guess.isalpha():
      # Reject guesses that are not exactly five letters.
      print('Enter a 5-lettered word.')
      continue
    if guess in guessed_letters:
      # Prevent duplicate guesses from counting twice.
      print('You already entered this word.')
      continue

    # Record the valid guess and check if it matches the secret word.
    guessed_letters.add(guess)
    guessed_words.append(guess)
    guessed_results.append(evaluate_guess(guess))

    if guess == wordle_word:
      # End the game with a win when the secret word is guessed.
      print('You win!')
      print(wordle_word)
      return

    if guess not in wordle_word:
      # Increase the wrong-guess count when the guess is not in the answer.
      incorrect_count.increment()

  # Show the losing message and reveal the secret word.
  print(f'You lose! The word was {wordle_word}.')

# Start the game when the file is run.
wordlegame()
again = int(input('Would you like to play again?\n 1. Yes\n 2. No\n'))
if again == 1:
  wordlegame()
else:
  print('Thank you for playing!')
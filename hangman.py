import random
hangman_pics = [
    """
      +---+
      |   |
          |
          |
          |
          |
    ========== 
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    ========== 
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    ========== 
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    ========== 
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    ========== 
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    ========== 
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========== 
    """
]
#different stages of hangman
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
words = get_dictionary_words()


class incorrect_guesses:
  """Track the number of incorrect guesses made during a game."""

  def __init__(self):
    self.count = 0

  def increment(self):
    """Record one incorrect guess and return the updated count."""
    self.count += 1
    return self.count

  def reset(self):
    """Reset the counter for a new game."""
    self.count = 0

  def __int__(self):
    return self.count

  def __lt__(self, other):
    return self.count < other


def get_random_word():
    return random.choice(words)

def play_hangman(secret_word=None):
  if secret_word is None:
    secret_word = get_random_word()
  guessed_letters = set()
  incorrect_guess_count = incorrect_guesses()
  max_lives = len(hangman_pics) - 1
  print('Welcome to hangman!')
  # The loop reads and updates every game-state variable, while the number
  # of lives is derived from the available drawing stages, not an integer.
  # Continue playing while the player still has lives remaining.
  while incorrect_guess_count < max_lives:
    # Show the drawing that matches the number of incorrect guesses.
    print(hangman_pics[int(incorrect_guess_count)])
    # Reveal guessed letters and show underscores for letters not guessed yet.
    display = ''.join(
      letter if letter in guessed_letters else '_'
      for letter in secret_word
    )
    print(display)
    print('Guessed letters:', ' '.join(sorted(guessed_letters)) or 'None')

    # If no underscores remain, every letter has been guessed correctly.
    if '_' not in display:
      print('You win!')
      return

    # Read one guess, rejecting invalid or previously used guesses.
    guess = input('Guess a letter: ').strip().lower()
    if len(guess) != 1 or not guess.isalpha():
      print('Enter one letter.')
      continue
    if guess in guessed_letters:
      print('You already guessed that letter.')
      continue

    guessed_letters.add(guess)
    # A wrong new guess advances the hangman drawing and uses one life.
    if guess not in secret_word:
      incorrect_guess_count.increment()

  # The loop ends when all lives are used, so the player has lost.
  print(hangman_pics[max_lives])
  print(f'You lose! The word was {secret_word}.')


def difficulty():
  print('You have 4 difficulty options:')
  print('1. Easy')
  print('2. Medium')
  print('3. Hard')
  print('4. Random, most difficult')

  def pick_word(min_length, max_length):
    word_list = [word for word in words if min_length <= len(word) <= max_length]
    if word_list:
      return random.choice(word_list)

    # If no words fit the requested range, choose the shortest available word
    # that is at least as long as the lower bound instead of falling back to
    # an arbitrary long word from the dictionary.
    eligible = [word for word in words if len(word) >= min_length]
    if eligible:
      return min(eligible, key=len)
    return random.choice(words)

  try:
    difficultychoice = int(input('What would you like to choose?'))
  except ValueError:
    print('Error. Try again...')
    return difficulty()

  if difficultychoice == 1:
    return pick_word(1, 5)
  elif difficultychoice == 2:
    return pick_word(6, 8)
  elif difficultychoice == 3:
    return pick_word(9, 11)
  elif difficultychoice == 4:
    return random.choice(words)
  else:
    print('Error. Try again...')
    return difficulty()


play_hangman(difficulty())
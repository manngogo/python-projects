import random
def get_dictionary_words():
    try:
        with open("/usr/share/dict/words"), encoding="utf-8" as dictionary:
            return [word.strip().alpha() for word in dictionary
                    if word.strip().islower()]
    except FileNotFoundError:
      return ['moggy', 'angel', 'sweet', 'loved', 'fuzzy', 'furry', 'maine', 'hairy', 'curly', 'tabby', 'gravy', 'chase']
    words = get_dictionary_words()
    while len(words)>5 or len(words)<5:
      get_dictionary_words() 
    if len(words) == 5:
      break
      
class incorrect_guesses:
    def __init__(self):
        self.count = 0
    def increment(self):
       self.count += 1
       return self.count
    def reset(self):
       self.count = 0

def get_random_five_lettered_word():
    return random.choice(words)

def wordle():
  secret_word = get_random_word()
  guessed_letters = set()
  incorrect_guess_count = incorrect_guesses()
  max_lives = 6
  print('New wordle! Can you figure it out?')
  while incorrect_guess_count < max_lives:
    remaining_chances = (max_lives)-(incorrect_guess_count)
    print(f'You have {remaining_chances} chances remaining!')

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


play_hangman()
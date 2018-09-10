import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
guessed_list = []
new_list = []
guessed_word = []
all_guessed = []
turn = 7

def load_word():
   f = open('words.txt', 'r')
   words_list = f.readlines()
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   
  
   return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
   
    for item in list(secret_word):
      if item in letters_guessed:
        new_list.append(item)
        
      
      elif letters_guessed not in list(secret_word):
        global guessed_list
        guessed_list.append(letters_guessed)
        global turn 
        global all_guessed
        if letters_guessed not in list(all_guessed):
          turn -= 1
        break
    all_guessed = new_list + guessed_list
    return True
  
    

    # FILL IN YOUR CODE HERE...

def get_guessed_word(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # FILL IN YOUR CODE HERE...
    new_list = []
    for item in list(secret_word):
      if item in letters_guessed:
        new_list.append(item)
      else:
        new_list.append("_")
    print(new_list)
    if new_list == list(current_word):
        print("You win!")
        global turn 
        turn = 0 
      





def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    missing = []
    for item in list(current_word):
      if item not in list(letters_guessed):
        missing.append(item)
    print("Missing letters: ", missing)
    print("Secret word: ", list(current_word))
  
def letter(prompt):
  letter = input(prompt)

  while letter.lower() not in letters:
    print("{} is not a valid letter. Please try again".format(letter))
    letter = input(prompt)

  return letter


def spaceman(secret_word):
    '''
    secretWord: string, the secret word to guess.
    Starts up a game of Spaceman in the command line.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to guess one letter per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    # FILL IN YOUR CODE HERE...
    print("The secret word has {} letters".format(len(secret_word)))
    print("Secret word value {}".format(secret_word))
    
    while turn > 0:
      is_word_guessed(current_word, letter("Please enter a letter you have {} tries : ".format(turn)))
      get_guessed_word(list(current_word), new_list)

    get_available_letters(all_guessed)
    print("All Guessed: ", all_guessed)
    
    
      
    
     



#
# secret_word = load_word()
current_word = load_word()
spaceman(current_word)






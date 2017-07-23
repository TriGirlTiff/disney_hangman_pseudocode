import random

dl_words = [
"FRONTIERLAND",
"FANTASYLAND",
"ADVENTURELAND",
"TOMORROWLAND",
"CHURRO",
]
# h_word = random.choice(dl_words)
good_guesses =[]
bad_guesses = []

def greeting():
    """greets player"""
    name = raw_input("What is your name? ")
    name = name.capitalize()
    print "Welcome {}! Let's play Disney hangman!".format(name)



def rules():
    """Prints rules of game"""
    print 
    print "These are the rules of the game. You can miss 4 letters or 2 solve attempts"

def player_options():
    """Player chooses to enter another letter or solve"""
    user_choice = raw_input ("\n\nEnter 1 to enter a letter or 2 to solve the puzzle. ")
    return user_choice


def get_word(dl_words):
    """gets random word from list"""
    h_word = random.choice(dl_words)
    return h_word



def get_spaces(h_word):
    """Shows number of spaces in hangman word"""
    h_word = get_word(dl_words)
    for letters in h_word:
        print "_ ", 

def solve_guess(h_word):
    user_solve = raw_input ("What is the hangman word? ")
    return user_solve



def get_letter():
    """Gets a letter from the user"""
    user_guess = raw_input("\n\nEnter a letter: ")
    user_guess = user_guess.upper()
    return user_guess

def display_word(h_word):
    """adds user chosen letters to blank spaces"""
    for letter in h_word:
        if letter in good_guesses:
            print letter,
        else:
            print "_",


greeting()
rules()
player_options()
h_word = get_word(dl_words)
get_spaces(h_word)




num_bad_guesses = 0
while num_bad_guesses < 4:
    user_guess = get_letter()
    if user_guess in bad_guesses or user_guess in good_guesses:
        bad_guesses.append(user_guess)
        good_guesses.append(user_guess)
        print "You have already guessed {}, guess again".format(user_guess)
    elif user_guess not in h_word:
        bad_guesses.append(user_guess)
        num_bad_guesses += 1
        print "{} isn't in the word, guess again".format(user_guess)
    elif user_guess in h_word:
        good_guesses.append(user_guess)
        print "Good guess!"

    display_word(h_word)



import random

dl_words = [
"frontierland",
"fantasyland",
"adventureland",
"tomorrowland",
"haunted mansion",
]
# h_word = random.choice(dl_words)
good_guesses =[]
bad_guesses = []

def greeting():
    """greets player"""
    name = raw_input("What is your name? ")
    name = name.capitalize()
    print "Welcome {}! Let's play hangman!".format(name)



def rules():
    """Prints rules of game"""
    print 
    print "These are the rules of the game. You can miss 5 letters"


def get_word(dl_words):
    """gets random word from list"""
    h_word = random.choice(dl_words)
    return h_word



def get_spaces(h_word):
    """Shows number of spaces in hangman word"""
    h_word = get_word(dl_words)
    for letters in h_word:
        print "_ ", 



def get_letter():
    """Gets a letter from the user"""
    user_guess = raw_input("\n\nEnter a letter: ")
    user_guess = user_guess.lower()
    return user_guess

def display_word(h_word):
    for letter in h_word:
        if letter in good_guesses:
            print letter,
        else:
            print "_",


greeting()
rules()
h_word = get_word(dl_words)
get_spaces(h_word)




num_bad_guesses = 0
while num_bad_guesses < 5:
    user_guess = get_letter()
    if user_guess in bad_guesses or user_guess in good_guesses:
        bad_guesses.append(user_guess)
        good_guesses.append(user_guess)
        print "You have already chosen that letter, guess again"
    elif user_guess not in h_word:
        bad_guesses.append(user_guess)
        num_bad_guesses += 1
        print "That letter isn't in the word, guess again"
    elif user_guess in h_word:
        good_guesses.append(user_guess)
        print "Good guess!"

    display_word(h_word)



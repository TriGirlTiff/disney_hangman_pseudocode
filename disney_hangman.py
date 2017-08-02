import random

dl_words = [
"FRONTIERLAND",
"FANTASYLAND",
"ADVENTURELAND",
"TOMORROWLAND",
"CHURRO",
"HAUNTED MANSION",
"PARADE",
"FIREWORKS",
"MICKEY",
"MINNIE",
"PLUTO",
"DONALD",
"GOOFY",
"SPACE MOUNTAIN",
"SPLASH MOUNTAIN",
"MATTERHORN"
]
# h_word = random.choice(dl_words)
good_guesses =[]
bad_guesses = []

def greeting():
    """greets player"""
    name = raw_input("What is your name? ")
    name = name.capitalize()
    print
    print "Welcome {}! Let's play Disney hangman!".format(name)
 



def rules():
    """Prints rules of game"""
    print 
    print "These are the rules of the game."
    print "All of the hangman words are things that can be found in Disneyland in Anaheim, California."
    print "You can miss 4 letters or one solve attempt."

def should_guess_word():
    """Player chooses to enter a letter or solve"""
    user_choice = raw_input ("\n\nPress enter to guess a letter or 2 to solve the puzzle. ")
    if user_choice == "2":
        return True
    else:
        return False




def get_word(dl_words):
    """gets random word from list"""
    h_word = random.choice(dl_words)
    return h_word



# def get_spaces(h_word):
#     """Shows number of spaces in hangman word"""
#     h_word = get_word(dl_words)
#     for letters in h_word:
#         print "_ ", 

def solve_guess(h_word):
    """Allows user to guess the hangman word"""
    user_solve = raw_input ("What is the hangman word? ")
    user_solve = user_solve.upper()
    if user_solve == h_word:
        print 
        print "You win! {} was the word!".format(h_word)
    else:
        print
        print "Sorry,{} is not the hangman word".format(user_solve)

def check_win(h_word, good_guesses):
    """Checks to see if all the letters have been guessed"""
    for letter in h_word:
        if letter in good_guesses or letter == " ":
            continue
        else:
            return False
    return True
    

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
        elif letter == " ":
            print letter,
        else:
            print "_",
    print 

greeting()
rules()
# player_options()
h_word = get_word(dl_words)
display_word(h_word)
# get_spaces(h_word)




num_bad_guesses = 0
while num_bad_guesses < 4:
    if should_guess_word():
        solve_guess(h_word)
        break
    
    else:
        user_guess = get_letter()
        if user_guess in bad_guesses or user_guess in good_guesses:
            bad_guesses.append(user_guess)
            good_guesses.append(user_guess)
            print "You have already guessed {}, guess again".format(user_guess)
        
        elif user_guess not in h_word:
            bad_guesses.append(user_guess)
            num_bad_guesses += 1
            print "{} isn't in the word, guess again.".format(user_guess)
        
        elif user_guess in h_word:
            good_guesses.append(user_guess)
            print "Good guess!"
            if check_win(h_word, good_guesses):
                print "You win!"
                break

    display_word(h_word)

    if num_bad_guesses == 4:
        print "You ran out of chances! The hangman word was {}".format(h_word)



import display_utility
import words
import random



def check_word(secret, guess):
    '''
    This function takes in the secret word and the users guess and returns a list of 
    words that are the color of their guess (green in right spot, etc.)
    '''
    clue = ["grey" for _ in range(5)]
    tempguess = list(guess)
    tempsecret = list(secret)

    for idx, letter in enumerate(tempguess):
        if tempsecret[idx] == letter:
            clue[idx] = 'green'

            tempguess[idx] = "#"
            tempsecret[idx] = "%"
    
    for idx, letter in enumerate(tempguess):
        if letter in tempsecret:
            clue[idx] = 'yellow'

            tempsecret[tempsecret.index(letter)] = "%"

    return clue
    

def known_word(clues):
    '''
    This function takes in a history of clues and returns a built up string containing
    all the green letters from all the guesses. Every letter that isn't green is 
    replaced by an underscore
    '''
    known = ["_" for _ in range(5)]
    for entry in clues:
        guess = entry[0]
        clue = entry[1]
        for idx, color in enumerate(clue):
            if color == "green":
                known[idx] = guess[idx]
    return f'{"".join(known)}'


def check_letters(clues, yes_lets):
    '''
    This function uses sets to remove duplicates and adds all the letters from the clues to each of the 
    sets. Since green and yellow letters take priority over grey letters (if you have two letters and one is in the 
    word, you want to mark that one known), the grey letters are the set difference between the grey letters and the
    set of the union of the green and yellow letters. 
    '''
    green_letters = set([])
    yellow_letters = set([])
    grey_letters = set([])

    for clue in clues:
        for idx, letter in enumerate(clue[0]):

            match clue[1][idx]:
                case 'green':
                    green_letters.add(letter)
                case 'yellow':
                    yellow_letters.add(letter)
                case 'grey':
                    grey_letters.add(letter)
    
    yes_letters = sorted( list( green_letters.union(yellow_letters) ) )
    no_letters = sorted( list( grey_letters.difference( green_letters.union(yellow_letters) ) ) )

    if yes_lets:
        return "".join(yes_letters).upper()
    else:
        return "".join(no_letters).upper()

    



def no_letters(clues):
    '''
    This function calls my helper function check_letters with the color grey and returns a string
    '''
    return check_letters(clues, False)


def yes_letters(clues):
    '''
    This function also calls my helper function check_letters and does the same thing as no_letters
    '''
    return check_letters(clues, True)

def write_wordle(clues):
    for clue in clues:
            for idx, letter in enumerate(clue[0]):
                if clue[1][idx] == 'green':
                    display_utility.green(letter)

                elif clue[1][idx] == 'yellow':
                    display_utility.yellow(letter)

                else:
                    display_utility.grey(letter)

            print()


if __name__ == "__main__":
    secret_word = random.choice(words.words).upper()
    clues = []
    for _ in range(6):

        print("Known:", known_word(clues))
        print("Green/Yellow Letters:", yes_letters(clues))
        print("Grey Letters:", no_letters(clues))

        while True:
            guess = input("> ").strip().upper()
            if len(guess) == 5 and (guess.lower() in words.words):
                break
        
        clues.append((guess, check_word(secret_word, guess)))

        write_wordle(clues)
        
        if guess == secret_word:
            break
    
    print("Answer: " + secret_word)
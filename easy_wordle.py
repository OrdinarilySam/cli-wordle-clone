from wordle import (check_word, write_wordle)
import words
import random


def filter_word_list(words, clues):
    '''
    This function takes in a list of words and a list of clues and loops through all the words in the word list
    to see if checking the clues against the words in the word list produce the same clues that were given
    '''
    valid = []
    for word in words:
        check = True
        for clue in clues:
            if check_word(word.upper(), clue[0]) != clue[1]:
                check = False
        if check:
            valid.append(word)
    return valid

if __name__ == "__main__":
    secret_word = random.choice(words.words).upper()
    clues = []
    current_list = words.words

    for _ in range(6):
        while True:
            guess = input("> ").strip().upper()
            if guess.lower() in words.words:
                break
        clues.append((guess, check_word(secret_word, guess)))

        write_wordle(clues)

        current_list = filter_word_list(current_list, clues)
        if len(current_list) > 5:
            selected = random.choices(current_list, k=5)
        else:
            selected = current_list

        print(f"{len(current_list)} words possible:")
        for word in selected:
            print(word)

        if guess == secret_word:
            break

    print("Answer:", secret_word)
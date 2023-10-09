import requests
import random
from rich import print


def main():
    guess_count = 1
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    word = get_random_word()
    guess = get_guess()
    print(word)
    print(guess)
    color_coded = color_code(guess,word)
    print(match_word(guess, color_coded))


#Make letters in guess colored from when they re matched the word
def match_word(guess, color_coded):
    newGuess = ""

    for letter in guess:

        #letter correct placed make it green
        if color_coded[guess.index(letter)] == "c":
            newGuess += f"[green]{letter}[/green]"
        
        #letter mis placed make it yellow
        elif color_coded[guess.index(letter)] == "m":
            newGuess += f"[yellow]{letter}[/yellow]"

        #letter wrong make it black
        else:
            newGuess += f"[black]{letter}[/black]"

    return newGuess


#Match guess to word and make color coded list
def color_code(guess, word):
    color_coded = []

    for letter in guess:
        if letter in word:
            if letter == word[guess.index(letter)]:
                color_coded.append("c")
            else:
                color_coded.append("m")
        else:
            color_coded.append("w")

    return color_coded


#Gets 5 letter words from stanford.edu and make them list.
def get_random_word():
    r = requests.get("https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt")
    wordList = []

    for word in r.text.replace("\n", ",").split(","):
        wordList.append(word.upper())

    wordList.pop()

    return random.choice(wordList)


#TODO
def get_guess():
    guess = input("Guess Word: ").upper()
    
    return guess


#TODO
def display_wordle(guesses):
    for guess in guesses:
        print(guess)


#TODO
def wordle():
    guesses = ["_____", "_____", "_____", "_____", "_____"]
    
    return guesses


#Starts the program
if __name__ == "__main__":
    main()

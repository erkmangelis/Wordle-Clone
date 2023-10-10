import requests
import random
from rich import print


def main():
    guess_count = 1
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    guesses = ["_____", "_____", "_____", "_____", "_____"]
    word = get_random_word()
    status = ""
    color_coded = [["w","w"],["w","w"],["w","w"],["w","w"],["w","w"]]
    
    print(word)
    #Main loop
    while guess_count <= 5:
        #Game UI
        print(f"+-----------[bold blue]Guess {guess_count}[/bold blue]-----------+")
        print("|"+" "*29 + "|")
        display_wordle(guesses)
        print(f"|  {match_letters(letters, color_coded)} |")
        print("+" + "-"*29 + "+")
        guess = get_guess()


        color_coded = color_code(guess,word)
        guesses[guess_count - 1] = match_word(guess, color_coded)
        guess_count += 1
    
        print()

        #If player's guess correct, break loop
        if guess == word:
            status = "win"
            break

    #After game ends, checks the game status if player win or lose
    if status == "win":
        print("+" + "-"*11 +"[bold blue]You Won[/bold blue]"+ "-"*11 +"+")
        print("|"+" "*29 + "|")
        display_wordle(guesses)

    else:
        print("+" + "-"*12 +f"[bold blue]{word}[/bold blue]" + "-"*12 +"+")
        print("|"+" "*29 + "|")
        display_wordle(guesses)


def match_letters(letters, color_coded):
    for pair in color_coded:
        if pair[1] in letters:
            if pair[0] == "c":
                letters[letters.index(pair[1])] = f"[bold green]{pair[1]}[/bold green]"
            elif pair[0] == "m":
                letters[letters.index(pair[1])] = f"[bold yellow]{pair[1]}[/bold yellow]"
            elif pair[0] == "w":
                letters[letters.index(pair[1])] = f"[bold black]{pair[1]}[/bold black]"

    strletters = ""
    for letter in letters:
        strletters += letter
    
    return strletters

#Make letters in guess colored from when they re matched the word
def match_word(guess, color_coded):
    newGuess = ""

    for letter in guess:

        #letter correct placed make it green
        if color_coded[guess.index(letter)][0] == "c":
            newGuess += f"[bold green]{letter}[/bold green]"
        
        #letter mis placed make it yellow
        elif color_coded[guess.index(letter)][0] == "m":
            newGuess += f"[bold yellow]{letter}[/bold yellow]"

        #letter wrong make it black
        else:
            newGuess += f"[bold black]{letter}[/bold black]"

    return newGuess


#Match guess to word and make color coded list
def color_code(guess, word):
    color_coded = []

    for letter in guess:
        if letter in word:
            if letter == word[guess.index(letter)]:
                color_coded.append(["c", letter])
            else:
                color_coded.append(["m", letter])
        else:
            color_coded.append(["w", letter])

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
    guess = input("       Guess Word: ").upper()
    
    return guess


#TODO
def display_wordle(guesses):
    for guess in guesses:
        print("|"+" "*12 + guess + " "*12 + "|")
    
    print("+" + "-"*29 + "+")



#Starts the program
if __name__ == "__main__":
    main()

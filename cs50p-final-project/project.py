import sys
import random
import requests
from rich import print



def main():
    #Guess count | Will increased after every guess
    guess_count = 1

    #List of letters in english alphabet
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
               'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    #Wordle rows in list
    guesses = ["_____", "_____", "_____", "_____", "_____"]

    #This variable determine what will display end game
    status = ""

    #The color code list changes after each guess depending on the letters in the guessed letters
    color_coded = [["w","w"],["w","w"],["w","w"],["w","w"],["w","w"]]

    #Gets guess from user and assign it as word to use functions
    word = get_random_word()
    print(word)


    #Main game loop
    #If guess_count reach bigger than 5 ends loop and game
    while guess_count <= 5:

        #Game UI
        #Displays Guess count, wordle rows, all letters user can use and gets guess from user
        print(f"[bold blue]Guess {guess_count}[/bold blue]")
        display_wordle(guesses)
        print(match_letters(letters, color_coded))

        #Takes guess from users and assign as guess
        guess = get_guess()

        #After taked guess from user
        #create color coded list
        #adds the guessed word to wordle rows
        #increase guess count one
        color_coded = color_code(guess,word)
        guesses[guess_count - 1] = match_word(guess, color_coded)
        guess_count += 1
        #If guess_count reach bigger than 5, main while loop stops and game'll end

        #If player's guess correct, break loop and end the game
        if guess == word:
            status = "win"
            break


    #After game ends, checks the game status if player win or lose
    #If status is win, prints "you won" and wordle rows.
    #If player lose prints the right word and wordle rows.
    if status == "win":
        print("[bold blue]You Won[/bold blue]")
        display_wordle(guesses)

    else:
        print(f"[bold blue]{word}[/bold blue]")
        display_wordle(guesses)


#Make lettter in letters list colored if they match with letter in guessed word
#Takes two argument, first one is letter list and the second one is color code list
#returns colored letters list transformed as string
def match_letters(letters, color_coded):
    for pair in color_coded:
        if pair[1] in letters:
            #color green the letter if it's correct
            if pair[0] == "c":
                letters[letters.index(pair[1])] = f"[bold green]{pair[1]}[/bold green]"
            #color yellow the letter if it's misplaced
            elif pair[0] == "m":
                letters[letters.index(pair[1])] = f"[bold yellow]{pair[1]}[/bold yellow]"
            #color black the letter if it's wrong
            elif pair[0] == "w":
                letters[letters.index(pair[1])] = f"[bold black]{pair[1]}[/bold black]"

    #Transform letter list to string object
    strletters = ""
    for letter in letters:
        strletters += letter

    #returns letters as string object
    return strletters


#Make letters in guess colored from when they re matched the word
#"c" correct -> green | "m" misplaced -> yellow | "w" wrong -> black
def match_word(guess, color_coded):
    new_guess = ""

    for letter in guess:

        #letter correct placed make it green
        if color_coded[guess.index(letter)][0] == "c":
            new_guess += f"[bold green]{letter}[/bold green]"

        #letter mis placed make it yellow
        elif color_coded[guess.index(letter)][0] == "m":
            new_guess += f"[bold yellow]{letter}[/bold yellow]"

        #letter wrong make it black
        else:
            new_guess += f"[bold black]{letter}[/bold black]"

    return new_guess


#Match guess to word and make color coded list
#In the list, first index is color code and second one is letter
#returns ExpList = [["c", "a"], ["c", "b"], ["m", "c"], ["colorCode", "letterInWord"]], ["w", "d"]]
def color_code(guess, word):
    color_coded = []

    for letter in guess:
        if letter in word:
            #c is for correct
            if letter == word[guess.index(letter)]:
                color_coded.append(["c", letter])
            #m is for misplaced
            else:
                color_coded.append(["m", letter])
            #w is for wrong
        else:
            color_coded.append(["w", letter])

    return color_coded


#Gets 5 letter words from stanford.edu and return randomly one of them
def get_random_word():
    r = requests.get("https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt")
    word_list = []

    for word in r.text.replace("\n", ",").split(","):
        word_list.append(word.upper())

    word_list.pop()

    return random.choice(word_list)


#Gets valid guess from user
#Its accept guess if its 5 character and only contains alphabetical character
def get_guess():
    while True:
        try:
            guess = input("Guess Word: ").upper()

            if len(guess) != 5:
                continue

            elif not guess.isalpha():
                continue

            else:
                return guess

        except:
            sys.exit("\nGame Ended from User")


#Prints all rows in wordle
def display_wordle(guesses):
    for guess in guesses:
        print(guess)


#Starts the program
if __name__ == "__main__":
    main()

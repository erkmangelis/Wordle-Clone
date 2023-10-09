import requests
import random


def main():
    word = get_random_word()
    print(word)



#Gets 5 letter words from stanford.edu and make them list.
def get_random_word():
    r = requests.get("https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt")
    wordList = []

    for word in r.text.replace("\n", ",").split(","):
        wordList.append(word)

    wordList.pop()

    return random.choice(wordList)


def get_guess():
    guess = input("Guess Word: ")
    return guess




if __name__ == "__main__":
    main()

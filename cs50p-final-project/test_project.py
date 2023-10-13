from project import match_word, match_letters, color_code


#STATIC VARIABLES FOR TEST TO FUNCTIONS
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
               'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

color_coded = [["c","C"],["c","L"],["w","A"],["m","I"],["w","M"]]

guess = "CLAIM"

word = "CLEAR"


def test_match_word():
    assert match_word(guess, color_coded) == "[bold green]C[/bold green][bold green]L[/bold green][bold black]A[/bold black][bold yellow]I[/bold yellow][bold black]M[/bold black]"

def test_match_letters():
    assert match_letters(letters, color_coded) == "[bold black]A[/bold black]B[bold green]C[/bold green]DEFGH[bold yellow]I[/bold yellow]JK[bold green]L[/bold green][bold black]M[/bold black]NOPQRSTUVWXYZ"

def test_color_code():
    assert color_code(guess, word) == [["c", "C"], ["c", "L"], ["m", "A"], ["w", "I"], ["w", "M"]]

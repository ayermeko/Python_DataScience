import sys

def morse_code(string: str) -> str:
    """
    This function converts a string to Morse code.
    """
    NESTED_MORSE = {    " ": "/ ",
                        "A": ".- ",
                        "B": "-... ",
                        "C": "-.-. ",
                        "D": "-.. ",
                        "E": ". ",
                        "F": "..-. ",
                        "G": "--. ",
                        "H": ".... ",
                        "I": ".. ",
                        "J": ".--- ",
                        "K": "-.- ",
                        "L": ".-.. ",
                        "M": "-- ",
                        "N": "-. ",
                        "O": "--- ",
                        "P": ".--. ",
                        "Q": "--.- ",
                        "R": ".-. ",
                        "S": "... ",
                        "T": "- ",
                        "U": "..- ",
                        "V": "...- ",
                        "W": ".-- ",
                        "X": "-..- ",
                        "Y": "-.-- ",
                        "Z": "--.. ",
                        "0": "----- ",
                        "1": ".---- ",
                        "2": "..--- ",
                        "3": "...-- ",
                        "4": "....- ",
                        "5": "..... ",
                        "6": "-.... ",
                        "7": "--... ",
                        "8": "---.. ",
                        "9": "----. ",
    }
    morse_code_string = ""
    for char in string:
        if char.upper() in NESTED_MORSE:
            morse_code_string += NESTED_MORSE[char.upper()]
    return morse_code_string.strip()
    

def check_for_special_characters(string: str) -> bool:
    """
    This function checks if the string contains special characters.
    """
    for char in string:
        if not char.isalnum() and not char.isspace():
            return True
    return False


def main():
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        assert len(sys.argv) > 1, "no argument is provided"
        if (check_for_special_characters(sys.argv[1])):
            raise AssertionError("the arguments are bad")
        result = morse_code(sys.argv[1])
        print(result)

    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
        return

if __name__ == "__main__":
    main()

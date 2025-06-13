import sys


def main():
    """
    This is program that takes a tring as an argument and
    encodes it into Morse code.
    The program supports shpace and alphanumeric characters.
    An alphnumeric character is represented by dots and dashes,
    Complete morse characters are separated by a space.
    A space character is repeated by a slash (/).
    """
    NESTED_MORSE = {" ": "/ ",
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
                    "9": "----. "
                    }
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        is_valid = all(c.isalnum() or c.isspace()
                       for c in sys.argv[1]) and len(sys.argv[1]) > 0
        assert is_valid, "the arguments are bad"

        morse_result = ""
        for char in sys.argv[1].upper():
            if char in NESTED_MORSE:
                morse_result += NESTED_MORSE[char]
        result = morse_result.rstrip()
        print(result)  # rstrip removes the trailing space

    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
        return


if __name__ == "__main__":
    main()

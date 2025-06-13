import sys


def character_sums(value) -> None:
    """
    This function takes a string and calculates
    the sum of characters of a
    certain type in the string and prints the results.
    :param value: The string to analyze.
    :return: None
    """
    dictionary = {
        "upper_letters": 0,
        "lower_letters": 0,
        "punctuation_marks": 0,
        "spaces": 0,
        "digits": 0
    }
    print(f"The text contains {len(value)} characters:")
    for char in value:
        if char.isupper():
            dictionary["upper_letters"] += 1
        elif char.islower():
            dictionary["lower_letters"] += 1
        elif char.isdigit():
            dictionary["digits"] += 1
        elif char.isspace():
            dictionary["spaces"] += 1
        else:
            dictionary["punctuation_marks"] += 1
    print(f"{dictionary['upper_letters']} upper letters")
    print(f"{dictionary['lower_letters']} lower letters")
    print(f"{dictionary['punctuation_marks']} punctuation marks")
    print(f"{dictionary['spaces']} spaces")
    print(f"{dictionary['digits']} digits")


def main():
    """
    This is a function that a single argument and
    displays the sums of its upper-case chars, lower-case chars,
    punctuation, digits and spaces.

    if there is not argument waits for an argument in a command line.
    """
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 1:
            value = input("What is the text to count?\n")
            character_sums(value)
        else:
            string = sys.argv[1]
            character_sums(string)

    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
        return


if __name__ == "__main__":
    main()

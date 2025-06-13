import sys


def is_integer(value: str) -> bool:
    """
    Checks if the provided value is not a negative integer.
    Chceks if the non-negative integer can be converted to an integer.
    :param value: The value to check.
    :return: True if the value is a non-negative integer, False otherwise.
    :rtype: bool
    """
    try:
        int_value = int(value)
        return int_value >= 0
    except ValueError:
        return False


def valid_string(value: str) -> bool:
    """
    Checks if the provided value stirng has special characters.
    :param value: The value to check.
    :return: True if the value is a string without special
    characters, False otherwise.
    :rtype: bool
    """
    return all(c.isalpha() or c.isspace() for c in value) and len(value) > 0


def main():
    """
    This is the main function that accepts two arguments from the command line:
    1. a string(S)
    2. length greater than N
    The program should output a list of words from S
    that have a length greater than N.
    - Words are separated by spaces only.
    - Strings do not contain special characters.
    If the number of argument is different form 2, or if the type of any
    argument is wrong, the program should print AssertionError.
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert valid_string(sys.argv[1]) and is_integer(sys.argv[2]), \
            "the arguments are bad"

        string = sys.argv[1]
        length = int(sys.argv[2])
        words = string.split()

        filtered_words = [word for word in words
                          if (lambda w: len(w) > length)(word)]
        print(filtered_words)

    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
        return


if __name__ == "__main__":
    main()

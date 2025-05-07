import sys


def isNum(string: str) -> bool:
    """
    This function checks if the string is a number.
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


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
        argument_count = len(sys.argv)
        assert argument_count <= 3, "more than two argument is provided"
        if argument_count < 2 or isNum(sys.argv[1]):
            raise AssertionError("the arguments are bad")
        if check_for_special_characters(sys.argv[1]):
            raise AssertionError("the argument contains special characters")
        splited_words = sys.argv[1].split(" ")
        n = int(sys.argv[2])
        filtered = [word for word in splited_words
                    if (lambda w: len(w) >= n)(word)]
        print(filtered)
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
        return


if __name__ == "__main__":
    main()

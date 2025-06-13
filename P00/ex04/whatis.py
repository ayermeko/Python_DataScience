import sys


def is_number(s):
    """
        This function checks if the input is a digit.
        :param s: The input to check.
        :return: True if the input is a digit, False otherwise.
    """
    try:
        int(s)
        return True
    except ValueError:
        return False


def main():
    """
        This function checks the arguments form the command line and
        prints "I'am even" in case the number is even or "I'am odd" in case the number is odd.
        :AssertionError: If more than one argument is provided.
        :AssertionError: If the argument is not a digit.
    """
    try:
        if len(sys.argv) == 1: return
        assert len(sys.argv) <= 2, "more than one argument is provided"
        assert is_number(sys.argv[1]), "argument is not an integer"
        number = int(sys.argv[1])
        if number % 2 == 0:
            print("I'am even")
        else:
            print("I'am odd")
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
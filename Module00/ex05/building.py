import sys


def print_the_stats(stats: dict) -> None:
    """
    This function prints the stats of the text.
    """
    print(f"{stats['upper']} upper letters")
    print(f"{stats['lower']} lower letters")
    print(f"{stats['punctuation']} punctuation marks")
    print(f"{stats['spaces']} spaces")
    print(f"{stats['digits']} digits")


def count_text_properties(text: str) -> None:
    """
    This function prints properties of the text as uppercase
    letters, lowercase letters
    puntuation marks, spaces, digits.
    """
    stats = {
        'upper': 0,
        'lower': 0,
        'punctuation': 0,
        'spaces': 0,
        'digits': 0
    }
    for char in text:
        if char.isupper():
            stats['upper'] += 1
        elif char.islower():
            stats['lower'] += 1
        elif char.isspace():
            stats['spaces'] += 1
        elif char.isdigit():
            stats['digits'] += 1
        else:
            stats['punctuation'] += 1
    return stats


def main():
    try:
        argument_count = len(sys.argv)
        assert argument_count <= 2, "more than one argument is provided"
        if argument_count == 1:
            print("What is the text to count?")
            text = input()
            total_caracters = len(text)
            print(f"The text contains {total_caracters} characters:")
            stats = count_text_properties(text)
            print_the_stats(stats)
        else:
            text = sys.argv[1]
            total_caracters = len(text)
            print(f"The text contains {total_caracters} characters:")
            stats = count_text_properties(text)
            print_the_stats(stats)

    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
        return


if __name__ == "__main__":
    main()

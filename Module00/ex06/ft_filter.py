import sys


def ft_filter(function, iterable) -> list:
    """Filters elements from an iterable based on a function."""
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        argument_count = len(sys.argv)
        assert argument_count <= 1, "more than no argument is provided"
        print(list(ft_filter(lambda x: x % 2 == 0, numbers)))
        print(list(filter(lambda x: x % 2 == 0, numbers)))
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
        return


if __name__ == "__main__":
    main()

from array2D import slice_me


def main():
    """
    The function is a main to test the slicer.
    """
    family = [[1.80, 78.4],
                [2.15, 102.7],
                [2.10, 98.5],
                [1.88, 75.2]]
    try:
        check_len = len(family[0])
        assert check_len >= 1, "Each sublist must have at least 1 element"

        for i, member in enumerate(family):
            assert isinstance(member, list), f"Entry {i} is not a list"
            assert len(member) == check_len, f"Entry {i} must have at least 1 element"

    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()

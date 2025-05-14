from array2D import slice_me


def main():
    """
    This function handles error cases if the lists are not the same size, are not a list
    """
    family = [[1.80, 78.4],
                [2.15, 102.7],
                [2.10, 98.5],
                [1.88, 75.2]]

    try:
        expected_len = len(family[0])
        assert expected_len >= 1, "Each sublist must have at least 1 element"

        for i, member in enumerate(family):
            assert isinstance(member, list), f"Entry {i} is not a list"
            assert len(member) == expected_len, f"Entry {i} must have at least 1 element"
            
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
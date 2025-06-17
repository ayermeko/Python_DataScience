from give_bmi import give_bmi, apply_limit


def main():
    """
    This function is a main tester to test functions
    from another file, and functions in that file
    have the core logic. It is a good practice to
    have asserts inside of the main tester.
    """
    height = [2]
    weight = [1]
    try:
        assert len(height) == len(weight), \
        "The variables are not the same size."
        assert all(isinstance(h, (int, float)) for h in height), \
        "The height has to be an int or float."
        assert all(isinstance(w, (int, float)) for w in weight), \
        "The weight has to be an int or float."
        assert all(h > 0 for h in height), "Height must be greater than 0."
        assert all(w > 0 for w in weight), "Weight must be greater than 0."

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return


if __name__ == "__main__":
    main()

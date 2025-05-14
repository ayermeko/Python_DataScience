from give_bmi import give_bmi, apply_limit


def main():
    """
    Handle the error cases as negaive numbers, non-float or non-int list
    mismatch of the list sizes...
    """
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]

        assert len(height) == len(weight), "Height and Weight does not match."
        assert all(isinstance(h, (int, float)) for h in height), \
            "Height list contains non-numeric values"
        assert all(isinstance(w, (int, float)) for w in weight), \
            "Height list contains non-numeric values"
        assert all(h > 0 for h in height), "Height must be greater than 0."
        assert all(w > 0 for w in weight), "Weight must be greater than 0."

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()



def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate bmis for the list of height and weight and return it as float or
    possibly int.
    zip() to iterate through more then one variable.
    """
    bmis = []
    for h, w in zip(height, weight):
        bmi = w / (h ** 2)
        bmis.append(bmi)
    return bmis


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Applys a limit for each elem of the list and return the list
    with True or False value if the limit is less then bmi
    """
    if (abs(limit) != limit):
        raise AssertionError("Limit must be non-negaive number.")

    res = [value > limit for value in bmi]
    return res

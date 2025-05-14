

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Cacluate BMI return is it as list of float or possibly list of ints
    zip() mostly used to iterate though pairs elements form two or more iterables together.
    """
    bmis = []
    for w, h in zip(weight, height):
        bmi = w / (h ** 2)
        bmis.append(bmi)
    return bmis

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply limits (True if above the limit), in case limit is non-posivite number throw error.
    """
    if (abs(limit) != limit):
        raise AssertionError("Limit must be non-negaive number.")
    
    result = [value > limit for value in bmi]
    return result
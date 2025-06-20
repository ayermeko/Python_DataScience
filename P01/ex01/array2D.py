

def slice_me(family: list, start: int, end: int) -> list:
    """
    This function slices the 'family' list form the 'start' index to the 'end' index.
    """
    result = family[start:end]
    print(f"My shape is : {len(family), len(family[0])}")
    print(f"My new shape is : {len(result), len(result[0])}")
    return result

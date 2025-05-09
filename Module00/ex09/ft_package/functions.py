def count_in_list(lst, n) -> int:
    """
    Count the number of occurrences of n in lst.
    """
    count = 0
    for i in lst:
        if i == n:
            count += 1
    return count


def check_for_special_characters(string: str) -> bool:
    """
    This function checks if the string contains special characters.
    """
    for char in string:
        if not char.isalnum() and not char.isspace():
            return True
    return False                                                            



def check_for_special_characters(string: str) -> bool:
    """
    This function checks if the string contains special characters.
    """
    for char in string:
        if not char.isalnum() and not char.isspace():
            return True
    return False
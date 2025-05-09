

def count_in_list(lst, n) -> int:
    """
    Count the number of occurrences of n in lst.
    """
    count = 0
    for i in lst:
        if i == n:
            count += 1
    return count

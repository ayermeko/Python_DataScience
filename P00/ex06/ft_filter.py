

def ft_filter(function, iterable):
    """
    Custom implementation of the filter function.
    with using list comprehension. and returning lazy iteratables.
    """
    if function is None:
        return [item for item in iterable if item]

    return [item for item in iterable if function(item)]

# lazy iteratables are used to avoid creating a list in memory
# and to allow for more efficient memory usage, especially with large datasets.
# On-demand evaluation: Values are computed only when needed
# def main():
#     """
#     Main function to demonstrate the original functionality of filtering
#     then creating my own version of the filter function.
#     """
#     # Example list of numbers
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     # Filter out even numbers
#     # even_numbers00 = list(filter(lambda x: x % 2 == 0, numbers))
#     even_numbers01 = ft_filter(lambda x: x % 2 == 0, numbers)
#     # Print the result
#     # print("Even numbers:\t\t\t", even_numbers00)
#     print("Even numbers using ft_filter:\t", even_numbers01)
# if __name__ == "__main__":
#     main()

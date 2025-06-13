ft_list = ["Hello", "tata"]
ft_tuple = ("Hello", "toto")
ft_set = {"Hello", "tutu"}
ft_dict = {"Hello": "titi"}

# list is mutable and ordered collection of elements.
# tuple is immutable and ordered collection of elements.
# set is mutable and unordered collection of unique elements.
# dict mutable and unordered collection of key-value pairs.

# why dict is unordered?
# Because dictionaries in Python are implemented as hash tables, which do not maintain the order of elements.

# Additional information:
#   Alternative solution for tuple modification
#   temp_tuple = list(ft_tuple)
#   temp_tuple[1] = "Czech Republic"
#   ft_tuple = tuple(temp_tuple)

if __name__ == "__main__":
    try:
        # Attempt to modify the list
        ft_list[1] = "World"
        # Attempt to modify the tuple
        ft_tuple = ft_tuple[:1] + ("Czech Republic",)  # Create a new tuple with the modified value
        # Attempt to modify the set
        ft_set.remove("tutu")
        ft_set.add("Prague")
        # Attempt to modify the dictionary
        ft_dict["Hello"] = "42Prague"

    except ValueError:
        print("Value not found in collection.")
    except TypeError:
        print("Cannot modify immutable object.")

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)


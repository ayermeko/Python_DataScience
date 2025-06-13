def NULL_not_found(object: any) -> int:
    """
    This function that prints the object type of all types of "Null"
    and returns 0 if it goes well and 1 in case of error.
    :param object: The object to check.
    :return: 0 if successful, 1 if an error occurs.
    :raises TypeError: If the object is not of a type that can be checked.
    :raises ValueError: If the object is not a recognized "Null" type.
    """
    try:
        object_type = type(object)
        if object is None:
            print(f"Nothing: None {object_type}")
        elif isinstance(object, float) and object != object:  # NaN check
            print(f"Cheese: nan {object_type}")
        elif isinstance(object, bool) and not object:
            print(f"Fake: Flase {object_type}")
        elif isinstance(object, int) and object == 0:
            print(f"Zero: 0 {object_type}")
        elif isinstance(object, str) and object == '':
            print(f"Empty: {object_type}")
        else:
            raise TypeError
    except TypeError as e:
        print("Type not Found")
        return 1
    
    return 0

# You cannot check boolean before the int check because in Python, 
# bool is a subclass of int. This means that all boolean values are also integers:
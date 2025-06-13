def all_thing_is_obj(object: any) -> int:
    """
    Function to check if the object is an instance of a collection type.
    """
    try:
        obj_type = type(object)
        if (isinstance(object, list)):
            print(f"List : {obj_type}")
        elif (isinstance(object, tuple)):
            print(f"Tuple : {obj_type}")
        elif (isinstance(object, set)):
            print(f"Set : {obj_type}")
        elif (isinstance(object, dict)):
            print(f"Dict : {obj_type}")
        elif (isinstance(object, str)):
            print(f"{object} is in the kitchen : {obj_type}")
        else:
            raise TypeError
    except TypeError as e:
        print(f"Type not found")
    return 42
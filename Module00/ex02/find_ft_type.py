def print_type_check(obj: any) -> None:
    try:
        obj_type = type(obj)
        if (isinstance(obj, list)):
            print(f"List : {obj_type}")
        elif (isinstance(obj, tuple)):
            print(f"Tuple : {obj_type}")
        elif (isinstance(obj, set)):
            print(f"Set : {obj_type}")
        elif (isinstance(obj, dict)):
            print(f"Dict : {obj_type}")
        elif (isinstance(obj, str)):
            print(f"{obj} is in the kitchen : {obj_type}")
        else:
            raise TypeError
    except TypeError:
        print("Type not found")

def all_thing_is_obj(object: any) -> int:
    print_type_check(object)
    return 42

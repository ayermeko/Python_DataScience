

def NULL_not_found(object: any) -> int:
    try:
        object_type = type(object)
        if (object is None):
            print(f"Nothing: None {object_type}")
        elif (isinstance(object, float) and object != object):
            print(f"Cheese: nan {object_type}")
        elif (isinstance(object, bool) and object == False):
            print(f"Fake: Flase {object_type}")
        elif (isinstance(object, int) and object == 0):
            print(f"Zero: 0 {object_type}")
        elif (isinstance(object, str) and object == ''):
            print(f"Empty: {object_type}")
        else:
            raise TypeError
    except TypeError:
        print("Type not Found")
    return 1
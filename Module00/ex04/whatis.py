import sys

def isNum(obj: str) -> bool:
    try:
        float(obj)
        return True
    except ValueError:
        return False

def main():
    try:
        if (len(sys.argv) > 2):
            print("AssertionError: more than one argument is provided")
            return 
        elif (len(sys.argv) == 1):
            print("AssertionError: no argument provied")
            return
        elif (not isNum(sys.argv[1])):
            print("AssertionError: argument is not an integer")
            return
        
        if (int(sys.argv[1]) % 2 == 0):
            print("I'm Even")
        else:
            print("I'm Odd")
    except Exception as e:
        print(e)
    

if __name__ == "__main__":
    main()

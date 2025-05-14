from load_image import ft_load
import os


def main():
    """
    This is a main fucntion
    """
    try:
        print(ft_load("landscape.jpg"))
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()

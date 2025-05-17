from load_image import ft_load
from pimp_image import *



def main():
    array = ft_load("animal.jpeg")

    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)


if __name__ == "__main__":
    main()
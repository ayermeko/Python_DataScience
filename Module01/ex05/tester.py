from load_image import ft_load
from pimp_image import ft_blue
from pimp_image import ft_green
from pimp_image import ft_red
from pimp_image import ft_invert
from pimp_image import ft_grey
import numpy as np


def main():
    array = ft_load("landscape.jpg")
    print(f"The sape of image is: {np.shape(array)}")
    print(array)
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)

    print(f"{ft_invert.__doc__}")


if __name__ == "__main__":
    main()

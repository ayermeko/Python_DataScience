from pimp_image import ft_blue
from pimp_image import ft_green
from pimp_image import ft_grey
from pimp_image import ft_invert
from pimp_image import ft_red
from load_image import ft_load


def main():
    """
    The main funciton to test and call the fucntions
    from different files.
    """
    array = ft_load("landscape.jpg")
    try:
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
        # print(ft_invert.__doc__)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")



if __name__ == "__main__":
    main()

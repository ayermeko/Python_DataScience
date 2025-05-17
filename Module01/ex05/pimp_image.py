import numpy as np
import matplotlib.pyplot as plt

def ft_display(array: np.array) -> None:
    """
    Display the image using matplotlib.
    """
    try:
        plt.imshow(array)
        plt.axis('off')
        plt.show()
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")

def ft_invert(array: np.array) -> np.array:
    """
    Invert the colors of the image.
    """
    try:
        inverted_array = 255 - array
        ft_display(inverted_array)
        return inverted_array
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")
        return None

def ft_red(array: np.array) -> np.array:
    """
    Keep only the red channel of the image.
    """
    try:
        red_array = np.zeros_like(array)
        red_array[:, :, 0] = array[:, :, 0]
        ft_display(red_array)
        return red_array
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")
        return None


def ft_green(array: np.array) -> np.array:
    """
    Keep only the green channel of the image.
    """
    try:
        green_array = np.zeros_like(array)
        green_array[:, :, 1] = array[:, :, 1]
        ft_display(green_array)
        return green_array
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")
        return None


def ft_blue(array: np.array) -> np.array:
    """
    Keep only the blue channel of the image.
    """
    try:
        blue_array = np.zeros_like(array)
        blue_array[:, :, 2] = array[:, :, 2]
        ft_display(blue_array)
        return blue_array
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")
        return None


def ft_grey(array: np.array) -> np.array:
    """
    Convert the image to grayscale.
    """
    try:
        
        red_mean = array[:, :, 0] / 3
        green_mean = array[:, :, 1] / 3
        blue_mean = array[:, :, 2] / 3 
        sum_mean = red_mean + green_mean + blue_mean

        plt.imshow(sum_mean, cmap='gray')
        plt.axis('off')
        plt.show()
        return sum_mean
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")
        return None

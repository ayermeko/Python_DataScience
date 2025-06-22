import numpy as np
import matplotlib.pyplot as plt


def ft_display(array: np.array) -> None:
    try:
        plt.imshow(array)
        plt.axis('off')
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    except KeyboardInterrupt as e:
        print(f"{type(e).__name__}: Interrupted!")


def ft_invert(array: np.array) -> np.array:
    """
    Inverts the color of the image received.
    """
    res = 255 - array
    ft_display(res)
    return res


def ft_red(array: np.array) -> np.array:
    """
    Keep only red channels of the image.
    """
    res = np.zeros_like(array)
    res[:, :, 0] = array[:, :, 0]
    ft_display(res)
    return res


def ft_green(array: np.array) -> np.array:
    res = np.zeros_like(array)
    res[:, :, 1] = array[:, :, 1]
    ft_display(res)
    return res


def ft_blue(array: np.array) -> np.array:
    res = np.zeros_like(array)
    res[:, :, 2] = array[:, :, 2]
    ft_display(res)
    return res

def ft_grey(array: np.array) -> np.array:
    pass

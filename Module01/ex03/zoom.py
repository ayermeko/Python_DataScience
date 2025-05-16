from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def zoom(image: np.array) -> np.array:
    """
    Zoom on image by given an numpy array
    """
    try:
        assert isinstance(image, np.ndarray), "Input must be a numpy array"
        assert image.ndim == 3, \
            "Input array must have 3 dimensions (height, width, channels)"
        arrZoomedImage = image[100:500, 450:850, 0:1]
        print("New shape after slicing:", np.shape(arrZoomedImage))
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
        return None
    return arrZoomedImage


def main():
    """
    Call ft_load funciton to get array of image and zoom...
    """
    image_arr = ft_load("animal.jpeg")
    print(image_arr)
    zoomed_image = zoom(image_arr)
    print(zoomed_image)

    plt.imshow(zoomed_image, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()

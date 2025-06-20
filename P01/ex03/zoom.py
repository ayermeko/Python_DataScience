import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt

def zoom(image: np.array):
    """
    Zoom in image by a given numpay array.
    """
    try:
        assert isinstance(image, np.ndarray), "Input must be a numpy array"
        assert image.ndim == 3, "Input must have 3 dimentions"
        zoomed_image = image[100:500, 450:850, 0:1]
        print(f"New shape after slicing: {zoomed_image.shape}")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None
    return zoomed_image

def main():
    """
    This a main function to call a zoom function to see if it works.
    """
    img_array = ft_load("animal.jpeg")
    print(img_array)
    zoomed_img = zoom(img_array)
    print(zoomed_img)
    plt.imshow(zoomed_img, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
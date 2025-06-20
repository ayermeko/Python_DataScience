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
        no_channel = image[100:500, 450:850, 0]
        print(f"New shape after slicing: {zoomed_image.shape} or {no_channel.shape}")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None
    return zoomed_image


def rotate(img: np.array) -> np.array:
    """
    Transpose an image by a given numpy array.
    """
    try:
        arrTraspose = np.copy(img[:, :, 0])

        for y, row in enumerate(img):
            for x, col in enumerate(row):
                arrTraspose[x, y] = img[y, x][0]
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    return arrTraspose

def main():
    """
    This a main function to call a zoom function to see if it works.
    """
    img_array = ft_load("animal.jpeg")
    # print(img_array)
    zoomed_img = zoom(img_array)
    print(zoomed_img)
    rotated_img = rotate(zoomed_img)
    print(f"New shape after Transpose: {np.shape(rotated_img)}")
    print(rotated_img)

    try:
        plt.imshow(rotated_img, cmap='gray')
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
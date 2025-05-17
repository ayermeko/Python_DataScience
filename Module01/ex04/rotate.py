from load_image import ft_load
from load_image import zoom
import numpy as np
import matplotlib.pyplot as plt


def ft_transpose(image: np.array) -> np.array:
    """
    Transpose an image by given an numpy array
    """
    try:
        arrTranposed = np.copy(image[:, :, 0])

        for i, row in enumerate(image):
            for j, pixel in enumerate(row):
                arrTranposed[j][i] = image[i][j]
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None
    return arrTranposed


def main():
    """
    Call ft_load funciton to get array of image and zoom and transpose...
    """
    arrImage = ft_load("animal.jpeg")
    if arrImage is None:
        print("Failed to load image.")
        return
    arrZoomedImage = zoom(arrImage)
    if arrZoomedImage is None:
        print("Failed to zoom image.")
        return
    print(
        f"The shape of the image is: {np.shape(arrZoomedImage)}"
        f"or {np.shape(arrZoomedImage[:, :, 0])}"
    )
    print(arrZoomedImage)
    arrTransposedImage = ft_transpose(arrZoomedImage)
    if arrTransposedImage is None:
        print("Failed to transpose image.")
        return
    print(f"New shape after Transpose: {np.shape(arrTransposedImage)}")
    print(arrTransposedImage)
    plt.imshow(arrTransposedImage, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()

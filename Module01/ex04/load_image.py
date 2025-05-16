from PIL import Image
import os
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Load an image from a file and return it as a numpy array.
    Validates file, loads it...
    """
    try:
        assert os.path.exists(path), f"File does not exist: {path}"
        assert os.path.isfile(path), f"Path is not a file: {path}"
        assert os.access(path, os.R_OK), f"File is not readable: {path}"

        ext = os.path.splitext(path)[1].lower()
        assert ext in ['.jpg', '.jpeg'], f"Unsupported file format '{ext}'."

        img = Image.open(path)
        rgb_img = img.convert("RGB")

        print(f"The shape of image is: {np.shape(rgb_img)}")

        return np.array(rgb_img)
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")
        return None
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")
        return None

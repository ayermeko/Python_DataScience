import os
import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """
    Load an image form a file and return it as a numpy array.
    First validates files, loads it...
    """
    try:
        assert os.path.exists(path), f"file does not exist: {path}"
        assert os.path.isfile(path), f"Path is not a file: {path}"
        assert os.access(path, os.R_OK), f"File is not readable: {path}"

        ext = os.path.splitext(path)[1].lower()
        assert ext in ['.jpg', '.jpeg'], "Unsupported file format."

        img = Image.open(path)
        result = np.array(img)

        print(f"The shape of image is: {result.shape}")
        # rgb_img = img.convert("RGB")
        print(result)

        return result
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

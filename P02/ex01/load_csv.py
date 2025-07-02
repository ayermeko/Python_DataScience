import os
import pandas

def load(path: str) -> pandas.DataFrame:
    try:
        assert isinstance(path, str), "Path is bad."
        assert path.lower().endswith('.csv'), "Path is incorrect."
        assert os.path.isfile(path), \
            "Path is not a file, or it does not exists."
        assert os.access(path, os.R_OK), "File is not readable."
        dataset = pandas.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None

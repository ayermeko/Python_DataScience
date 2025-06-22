import pandas as pd

def load(path: str) -> pd.DataFrame: # -> Dataset: (You have to adapt the type of return according to your library)
    try:
        if not isinstance(path, str):
            raise TypeError(f"Incorrect type for a '{path}'")
        if not path.lower().endswith(".csv"):
            raise ValueError(f"Incorrect file extention")
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimension {dataset.shape}")
        return dataset
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None

# import matplotlib.pyplot as plt
from load_csv import load


def main():
    dataset = load("life_expectancy_years.csv")
    if dataset is None:
        return
    try:
        country = "Kazakhstan"
        if country not in dataset['country'].values:
            raise ValueError("Country is not in a dataset.")
        country_data = dataset[dataset['country'] == country]
        
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return

if __name__ == "__main__":
    main()
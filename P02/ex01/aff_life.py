import matplotlib.pyplot as plt
from load_csv import load


def main():
    dataset = load("life_expectancy_years.csv")
    if dataset is None:
        return
    try:
        country = "Czech Republic"
        if country not in dataset['country'].values:
            raise ValueError("Country is not in a dataset.")
        country_data = dataset[dataset['country'] == country]
        years = [int(year) for year in dataset.columns[1:]
                 if str(year).isdigit()]
        life_expectancy = country_data.iloc[0, 1:].values

        plt.plot(years, life_expectancy, label=country)
        plt.title(f"{country} Life expectancey Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return
    except KeyboardInterrupt as e:
        print(f"{type(e).__name__}: Program interrupted.")
        return


if __name__ == "__main__":
    main()

from load_csv import load
import matplotlib.pyplot as plt
import numpy as np

def ft_display(years: np.ndarray, life_exp: np.ndarray, country: str) -> None:
    """
    This is a function to display life expectancy data.
    """
    try:
        plt.plot(years, life_exp, label=country)
        plt.title(f"{country} Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.legend()
        plt.show()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Display stopped!")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


def main() -> None:
    """
    This function is a main to test a display.
    """
    try:
        datas = load("life_expectancy_years.csv")
        if datas is None:
            raise ValueError("File is empty or returned None.")
        
        country = "Czech Republic"
        if country not in datas['country'].values:
            print(f"{country} not found in the dataset")
            return
        
        country_data = datas[datas['country'] == country]
        years = np.array([int(year) for year in datas.columns[1:] if str(year).isdigit()])
        life_expectancy = np.array(country_data.iloc[0, 1:].values)

        ft_display(years, life_expectancy, country)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return

if __name__ == "__main__":
    main()

from load_csv import load
import matplotlib.pyplot as plt

def main():
    file1 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    file2 = load("life_expectancy_years.csv")
    if file1 is None or file2 is None:
        return
    certain_year = "1900"
    gnp_1900 = file1[certain_year]
    life_expectancy_1900 = file2[certain_year]
    
    try:
        plt.scatter(gnp_1900, life_expectancy_1900)
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life expectancy (Years)")
        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()

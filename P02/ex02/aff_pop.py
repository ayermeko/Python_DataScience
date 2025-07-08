from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def convert(val: str) -> float:
    if val.endswith("M"):
        return float(val[:-1]) * 1_000_000
    if val.endswith("k"):
        return float(val[:-1]) * 1_000
    return float(val)


def init_data(country: str, data: pd.DataFrame) -> list[float]:
    if country not in data["country"].values:
        raise ("No such a country is a Dataset.")
    populcation_row = data[data["country"] == country].iloc[:, 1:]
    return [convert(val) for val in populcation_row.values.flatten()]


def main():
    data = load("population_total.csv")
    if data is None:
        return

    country_names = ["Czech Republic", "Kazakhstan"]
    populcations = {}

    try:
        for country in country_names:
            populcations[country] = init_data(country, data)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return

    years = data.columns[1:].astype(int)

    try:
        for name, pop in populcations.items():
            plt.plot(years, pop, label=name)
        plt.xlim(1800, 2050)
        plt.xticks(range(1800, 2041, 40))
        plt.yticks(
            [i * 1e6 for i in range(20, 61, 20)],
            [f"{i}M" for i in range(20, 61, 20)]
        )

        plt.legend()
        plt.show()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return
    except KeyboardInterrupt:
        print("Interrupted.")
        return


if __name__ == "__main__":
    main()

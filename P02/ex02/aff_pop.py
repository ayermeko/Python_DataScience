from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def convert(population: str) -> float:
    """Convert '5.5M' → 5_500_000, '42k' → 42_000, '1234' → 1234."""
    if population.endswith("M"):
        return float(population[:-1]) * 1e6
    if population.endswith("k"):
        return float(population[:-1]) * 1e3
    return float(population)


def get_population_series(df: pd.DataFrame, country: str) -> list[float]:
    """Return a list of numeric population values for one country."""
    if country not in df["country"].values:
        raise ValueError(f"{country} is not in the dataset.")
    row = df[df["country"] == country].iloc[:, 1:]      # drop the 'country' col
    return [convert(val) for val in row.values.flatten()]


def main() -> None:
    df = load("population_total.csv")
    if df is None:
        return

    country_names = ["Czech Republic", "Kazakhstan"]     # keep order stable
    populations = {}

    # --- gather data ----------------------------------------------------- #
    try:
        for name in country_names:
            populations[name] = get_population_series(df, name)
    except ValueError as err:
        print(err)
        return

    years = df.columns[1:].astype(int)

    # --- plot ------------------------------------------------------------ #
    try:
        for name, pop in populations.items():
            plt.plot(years, pop, label=name)

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.xlim(1800, 2050)
        plt.xticks(range(1800, 2041, 40))

        # Center 40M in the visible range
        plt.yticks([i * 1e6 for i in range(20, 61, 20)],
                [f"{i}M" for i in range(20, 61, 20)])

        plt.legend()
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return
    except KeyboardInterrupt as e:
        print(e)
        return


if __name__ == "__main__":
    main()

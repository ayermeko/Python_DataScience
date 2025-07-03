from load_csv import load
import matplotlib.pyplot as plt
import pandas as ps


def convert(population: str) -> float:
    if population.endswith("M"):
        return float(population[:-1]) * 1e6
    elif population.endswith("k"):
        return float(population[:-1]) * 1e3
    return float(population)


def data_init(data: ps.DataFrame, country: str):
    if country not in data['country'].values:
        raise ValueError("Country is not in the data values.")
    country_data = data[data["country"] == country].iloc[:, 1:]
    population_row = country_data.values.flatten()
    return [convert(val) for val in population_row]

def main():
    data = load("population_total.csv")
    if data is None:
        return
    try:
        countries = {
            "Czech Republic",
            "Kazakhstan"
        }
        try:
            for country in countries:
                data_init(data, country)
        except Exception as e:
            print(e)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    except KeyboardInterrupt as e:
        print(f"Interrupted: {e}")
    
    # ft_display()

if __name__ == "__main__":
    main()
import numpy as np
import matplotlib.pyplot as plt

years = np.arange(1, 11)
lions = np.array([15, 16, 17, 20, 19, 21, 23, 24, 25, 27])
elephants = np.array([50, 52, 54, 53, 55, 56, 57, 59, 60, 62])
zebras = np.array([100, 98, 95, 97, 96, 94, 95, 93, 92, 90])

species_data = {
    'Lions': lions,
    'Elephants': elephants,
    'Zebras': zebras
}

def total_population(data):
    return np.sum(data)

def average_yearly_growth(data):
    yearly_growth = np.diff(data)
    return np.mean(yearly_growth)

def yearly_growth_rate(data):
    growth_rate = np.diff(data) / data[:-1] * 100
    return np.concatenate(([0], growth_rate))

print("Total Population and Average Yearly Growth:")
for species, data in species_data.items():
    total_pop = total_population(data)
    avg_growth = average_yearly_growth(data)
    print(f"{species} - Total Population: {total_pop}, Average Yearly Growth: {avg_growth:.2f}")

print("\nYearly Growth Rates (%):")
for species, data in species_data.items():
    growth_rates = yearly_growth_rate(data)
    print(f"{species} - Yearly Growth Rates: {growth_rates}")

plt.figure(figsize=(10, 6))
for species, data in species_data.items():
    plt.plot(years, data, label=species, marker='o')

plt.xlabel('Year')
plt.ylabel('Population (in thousands)')
plt.title('Population Trends Over 10 Years')
plt.legend()
plt.grid(True)
plt.show()

def species_with_highest_growth(data):
    avg_growth_rates = {species: average_yearly_growth(data[species]) for species in data}
    highest_growth_species = max(avg_growth_rates, key=avg_growth_rates.get)
    return highest_growth_species

highest_growth_species = species_with_highest_growth(species_data)
print(f"\nSpecies with the highest average growth rate: {highest_growth_species}")

end_population = {species: data[-1] for species, data in species_data.items()}

plt.figure(figsize=(10, 6))
plt.bar(end_population.keys(), end_population.values(), color=['blue', 'green', 'orange'])
plt.xlabel('Species')
plt.ylabel('Population at Year 10 (in thousands)')
plt.title('Total Population at the End of 10 Years')
plt.show()




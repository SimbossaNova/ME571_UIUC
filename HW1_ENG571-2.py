# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 17:55:33 2023

@author: jacob
"""

import matplotlib.pyplot as plt

# Data
years = [1950, 1960, 1970, 1980, 1990]
population = [152.3, 180.7, 205.0, 227.7, 249.9]
gdp = [1418.5, 1970.8, 2873.9, 3776.3, 4897.3]
energy = [33.1, 43.8, 66.4, 76.0, 81.3]
co2_emissions = [690.8, 791.9, 1156.5, 1252.5, 1337.3]

# Calculating terms
gdp_per_capita = [g/p for g, p in zip(gdp, population)]
energy_per_gdp = [e/g for e, g in zip(energy, gdp)]
co2_per_energy = [c/e for c, e in zip(co2_emissions, energy)]
calculated_co2_emissions = [p * a * eg * ce for p, a, eg, ce in zip(population, gdp_per_capita, energy_per_gdp, co2_per_energy)]

# Displaying results
for i, year in enumerate(years):
    print(f"For the year {year}:")
    print(f"GDP per capita (A) = ${gdp_per_capita[i]:.2f} billion/person")
    print(f"Energy per GDP = {energy_per_gdp[i]:.5f} (10^15 BTU/$B)")
    print(f"CO₂ emissions per Energy = {co2_per_energy[i]:.2f} (10^6 metric tons/10^15 BTU)")
    print(f"Calculated Total CO₂ emissions = {calculated_co2_emissions[i]:.2f} (10^6 metric tons)")
    print("\n")

calculated_co2_emissions = [p * a * eg * ce for p, a, eg, ce in zip(population, gdp_per_capita, energy_per_gdp, co2_per_energy)]

# Displaying results
for i, year in enumerate(years):
    print(f"For the year {year}:")
    print(f"Calculated CO₂ emissions = {calculated_co2_emissions[i]:.2f} (10^6 metric tons)")
    print("\n")


def display_change(prev, current, term_name):
    change = current / prev
    print(f"{term_name} in {years[i]} / {term_name} in {years[i-1]} = {current:.2f} / {prev:.2f} = {change:.2f} (i.e., a {100*(change-1):.2f} % {'increase' if change > 1 else 'decrease'})")

for i in range(1, len(years)):
    print(f"Changes from {years[i-1]} to {years[i]}:")
    display_change(population[i-1], population[i], "Population")
    display_change(gdp_per_capita[i-1], gdp_per_capita[i], "GDP per Capita")
    display_change(energy_per_gdp[i-1], energy_per_gdp[i], "Energy per GDP")
    display_change(co2_per_energy[i-1], co2_per_energy[i], "CO₂ emissions per Energy")
    display_change(co2_emissions[i-1], co2_emissions[i], "Total CO₂ emissions")
    print("\n")
    
    # Plotting Energy/GDP
plt.figure(figsize=(10, 5))
plt.plot(years, energy_per_gdp, marker='o', color='blue', label='Energy/GDP')
plt.title('Energy per GDP over Decades')
plt.xlabel('Year')
plt.ylabel('Energy/GDP (10^15 BTU/$B)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plotting CO₂ emissions/Energy
plt.figure(figsize=(10, 5))
plt.plot(years, co2_per_energy, marker='o', color='green', label='CO₂ emissions/Energy')
plt.title('CO₂ emissions per Energy over Decades')
plt.xlabel('Year')
plt.ylabel('CO₂ emissions/Energy (10^6 metric tons/10^15 BTU)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
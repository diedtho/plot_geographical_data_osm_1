from pyrosm.data import sources

# Print available source categories
print(sources.available.keys())

# Prints a list of countries in Europe that can be downloaded
print(sources.europe.available)

# Prints a list of all cities that can be downloaded
print(sources.cities.available)


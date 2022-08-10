from pyrosm import get_data

# Download data for the city of Helsinki
#fp = get_data("Helsinki")
#print(fp)

# Download the data into specified directory
fp = get_data("helsinki", directory="./my_data")
print("Data was downloaded to:", fp)
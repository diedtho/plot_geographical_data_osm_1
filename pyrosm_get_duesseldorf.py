from pyrosm import get_data

# Download the data into specified directory
fp = get_data("Duesseldorf", directory="./my_data")
print("Data was downloaded to:", fp)
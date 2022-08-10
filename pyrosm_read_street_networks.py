from pyrosm import OSM
from pyrosm import get_data
import osmnx as ox

# Pyrosm comes with a couple of test datasets
# that can be used straight away without
# downloading anything
fp = "./my_data/Helsinki.osm.pbf"

# Initialize the OSM parser object
osm = OSM(fp)

# Get all driving roads and the nodes
nodes, edges = osm.get_network(nodes=True, network_type="driving")
print(edges.head())

# Create NetworkX graph
G = osm.to_graph(nodes, edges, graph_type="networkx") # 'networkx' uses (too) much memory

# Plot the graph with OSMnx
ox.plot_graph(G)

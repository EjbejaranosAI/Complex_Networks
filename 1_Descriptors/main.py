"""Structural descriptors of complex networks"""
"""Authors: Edison Bejarano - Eric Walzthöny"""

## Import Scripts 
from utils.utils import extract_zip, read_net_files
from utils.utils import extract_data_and_save
from utils.airport_descriptors import AirportDescriptor


## Variable configuration
## Path to the zip file 
ZIP_PATH = './A1-networks.zip'
## extracted directory
OUTPUT = './A1-networks/'

## Extract the zipfile, if the output dir exists it will skip
extract_zip(ZIP_PATH, OUTPUT)

## Reading all the pajek files (.net files)
net_files = read_net_files(OUTPUT, verbosity=False)

##### Part A: Numerical Descriptors of Networks ######
## extract the data and optionally save the CSV
df = extract_data_and_save(net_files, "new_Descriptors", save_csv=True)

##### Part B: Numerical Descriptors of Real Network - AIRPORT ######
## get the airport file from memory 
airport = net_files['real']['airports_UW.net'][0]
airport = AirportDescriptor(airport, []) # not passing an airport list now
## usage 
## airport.degree --> degrees for all the nodes in the network 


### PART C: Histograms and CCDF


"""
networks_graph = []
name_networks = []

name_networks, networks_graph = extract_read_files(path, output)
print(len(networks_graph))
# a) Numerical descriptors of networks
df = compute_descriptors(name_networks,networks_graph)
df.to_csv('./results/Descriptors.csv',index=True)

# Airport real networks
# b) Numerical descriptors of the nodes of the network real/airports_UW.net
df2 = real_networks_airports(name_networks,networks_graph)

# c) Plot the histograms of the degree distributions (PDF, probability distribution function) and the complementary cumulative degree distributions (CCDF) for the following networks:

"""

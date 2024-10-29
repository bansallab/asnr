#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 13:34:31 2024

@author: melissacollier
"""
import pandas as pd
import numpy as np
import os
import glob
import networkx as nx
import community
import fnmatch
import os
import numpy as np
import csv
import zipfile
import math

from tabulate import tabulate


df = pd.read_csv("Network_summary_masterfile.csv")
df['genus_species'] = df['genus'] + " " + df['species']

num_networks = len(df.index)

Taxa = df['class'].unique().tolist()

num_taxa = len(Taxa)

Species = df['genus_species'].unique().tolist()
num_species = len(Species)

taxa_rows = []

for t in Taxa:
    d = df.loc[df['class']== t]
    num = len(d.index)
    species = d['genus_species'].unique().tolist()

    
    row = [t, num, species]
    taxa_rows.append(row)
    
    
taxa_cols = ['Taxanomic Class', "Number of Networks", "Species Represented"]
taxa_rows.insert(0, taxa_cols)
taxa_data = taxa_rows
taxa_table = tabulate(taxa_data, headers="firstrow", tablefmt="pipe")

######  
Interaction = df['interaction_type'].unique().tolist()
Interaction_clean = []

num_interactions = len(Interaction)
Interaction_defs = ["Physical contact occurs between individuals that are not grroming, trophallaxis, or dominance behaviors.",
                    "Mouth to mouth foodsharing behaviors",
                    "Physical contact unique to aggressive dominance interactions such as biting, head butting, fighting, etc.",
                    "No physical contact, individuals are just within a certain distance of eachother as indicated by the study",
                    "Physical contact unique to grooming interactions in primates",
                    "A projection of a bipartite network in which individuals are connected to all locations visted (e.g. feeder sharing networks)",
                    "Connections are based on multiple different types of interactions",
                    "Individuals are connected if they were seen foraging together",
                    "Individuals are connected if seen as part of the same group as defined by the research study",
                    "Individuals are connected sharing the same food source",
                    "Indiivduals are connected if mating involving fluid excahnge occurred (e.g. intromission)",
                    "Individuals are connected if mating that does not involve fluid exhange occurred (e.g. spore transfer)",
                    "Direct interaction between individuals that does not involve physical contact (e.g. sniffing, chasing)",
                    ]    


int_rows = []

n = 0
for i in Interaction:
    i1 = i.replace("_", " ")
    i1 = i1.replace ('NFE', "No Fluid Exchange")
    i1 = i1.replace ('FE', "Fluid Exchange")
    Interaction_clean.append(i1)
    d = df.loc[df['interaction_type']== i]
    num = len(d.index)
     
    row = [i1,Interaction_defs[n], num]
    n = n +1
    int_rows.append(row)
    

int_cols = ['Interaction Type', "General Definition" ,"Number of Networks"]
int_rows.insert(0, int_cols)
int_data = int_rows
int_table = tabulate(int_data, headers="firstrow", tablefmt="pipe")


with open("README.md", "a") as f:
    f.write("Animal Social Network Repository 2.0\n ===============\n\n")
    f.write("Background\n ==========================================\n This network repository is composed of " +str(num_networks) +" networks from " + str(num_species) + " species across " +str(num_taxa) +" taxa, that are publicly available. This repository is novel in that it incorporates different animal networks that vary in sociality levels, including social, solitary and fission fusion. Networks vary in interaction criteria, edge definition, and weighted and unweighted, and in many more network properties as well. However, this repository synthesizes all of these networks in an organized, consistent manner in order to make sure that the networks are user-friendly. It is our hope that the networks in this repository further advance the field of wildlife network theory, yet the networks in this repository are not limited to questions of sociality. Due to its extensive and detailed nature, the networks found in this repository can be used to answer multiple scientific inquiries in varying fields.\n To learn more about the project, please visit our website: https://bansallab.github.io/asnr/ or read the work by Sah et al cited below.\n\n" )
    f.write("Citation\n =================\n To cite the repository, please use:\n Melissa Collier, Pratha Sah, Jose Mendez, Sania Ali, Shweta Bansal. Animal Social Network Repository, Version 2. https://github.com/bansallab/asnr (2021)\n\n To cite the project and data, please use:\n Pratha Sah, José David Mendez, Shweta Bansal. A multi-species respository of social networks. Scientific Data, 6:44 (2019)\n\n")
    f.write("What is included?\n =================\n All networks can be found in the Networks directory. Details, descriptions and metrics for each network are found in Network_summary_masterfile.csv\n Below we summarize the networks across species and interactions.\n\n")
    f.write(taxa_table +"\n\n")
    f.write(int_table +"\n\n")
    f.write("Glossary of qualatative study description terms \n ===================================\n All terms below are found as qualatative columns in the Network_summary_masterfile.csv\n\n")
    f.write("Network ID: Unique identifier of the network in the Networks directory.\n\n")
    f.write("Network Identifiers: Descriptive terms to differentiate multiple networks taken from one study. Could include years, colony names, trap names, etc.\n\n")
    f.write("Taxonomic class: Taxonomic class of the species. Could be " + str(Taxa) + ".\n\n")
    f.write("Population type: Type of animal population recorded. Could be captive, semi-ranging or free-ranging.\n\n")
    f.write("Georgraphical location: Location where the population(s) were recorded.\n\n")
    f.write("Data collection technique: Method of data collection including focal sampling, survey scan, mark recapture, RFID, radio tags, video recording, etc.\n\n")
    f.write("Interaction type: Type of association/interaction recorded between animal pairs to construct the social network.\n\n")
    f.write("Definition of interaction: Criteria of occurence of an association/interaction as defined in the study.\n\n")
    f.write("Edge weight type: Criteria of weighting network edges. Could be based on frequency, duration, intensity of interactions or metrics such as simple ratio index, half weight index etc.\n\n")
    f.write("Total duration of data collection: Total time span over which the social network data was collected.\n\n")
    f.write("Time resolution of data colllection (within a day): Resolution of data collection within a day.\n\n")
    f.write("Time span of data collection (within a day): Total duration of data collection within a day.\n\n")
    f.write("Attributes Available: The node attributes provided in the study. If available, they are included in the graphml files. \n\n")
    f.write("Note: Additional notes on the dataset. \n\n")
    f.write("Glossary of quantative network metrics\n ===================================\n All metrics below are found as columns in the Network_summary_masterfile.csv")
    f.write("Is connected: Binary value to determine if the network is fully connected (TRUE) or is composed of multiple components (FAlSE)\n\n")
    f.write("Num Components: The number of connected components in the network.\n\n")
    f.write("Nodes: The number of individuals in the network.\n\n")
    f.write('Edges: The number of connections in the network. \n\n')
    f.write("Network Density: The proportion of existing edges in the network out of the total number of possible edges. \n\n")	
    f.write("Highest Degree: The highest degree value for a node in the network. \n\n")
    f.write("Average/Standard Deviation Degree: The average number of or standard deviation in contacts for all nodes in the network. \n\n")
    f.write("CV Degree: The coefficient of variation in the network. Equal to the average degree divided by the standard deviation.\n\n")
    f.write("Skewness: A measure of the asymmetry of the network's degree dsitribution. \n\n")
    f.write("Average/Standard Deviation Node Strength: The averagea and standard deviation of the sum of all the edgeweights connected to each node in the network. \n\n")
    f.write("CV Node Strength: The coefficient of variation of edge strength calculated as the average strength divided by the standard deviation. \n\n")
    f.write("Highest Node Strength: The highest strength value in the network. \n\n")
    f.write("Average/Standard Deviation Edge Strength: The mean and standard deviation in edge weight values. \n\n")
    f.write("CV Edge Strength: The coefficient of vairation in edge weight values, calculated as the average edge weight divided by the standard deviation. \n\n")
    f.write("Degree Assortativity: The tendency of contacts to have a similar number of contacts. Higher values mean high dgree individuals form more bonds, lower values mean that high degree individuals form bonds with low degree individuals. \n\n")
    f.write("Average/Standard Devioation Betweenness Centrality (Weighted/Unweighted): The tendency for nodes to occupy a central position in the network. Higher values mean the network has more central or bridge nodes. Values calculated both with and without edge weights. \n\n")
    f.write("Highest Betweenness Centrality (Weighted/Unweighted): The higest betweeness value in the network, both with and without edgeweights. \n\n")
    f.write("Clustering Coefficient (Weighted/Unweighted): The tendancy for a set of three individuals to be connected, or for an individuals contacts to interact with eachother. Calculated both with and without edgeweights. \n\n")
    f.write("Newman's Modularity (Q): The strength of subdividisions or communities within the network. Based on Newman's definition. \n\n")
    f.write("Qmax: The maximum modularity value. \n\n")
    f.write("Qrel: Modularity, (Q) normalized by Qmax. \n\n")
    f.write("Number of Modules: The number of modules or communities in the network.  \n\n")
    f.write("Average Module Size': THe average number of nodes in each mondule or community. \n\n")
    f.write("Cohesion: The tendancy for individuals to interact with their own module. \n\n")
    f.write("Diameter: The longest of all the shortest path lengths for all node pairs in the network. Calculated on the largest connected component. \n\n")
    f.write("Adding data\n ===========\n One of the main goals of this repository is to further enhance the study of animal social networks. If you happen to come across any interesting data on animal networks that has been published and is not yet included in this repository, please contact us. We will do our best to make it consistent with our format and add it to the repository. Requests should be filed to shweta@sbansal.com\n\n")
    f.write("License\n =======\n All datasets in this repository were made publicly available in other data repositories. You will find a link to the original source of the network, additionally to the study in which the data was collected. A great amount of effort was made to determine the license under which the datasets were distributed, and it is our understanding that the datasets are free to redistribute. However, if you own the rights to any dataset that is included in this repository and you object their inclusion, please email shweta@sbansal.com. The data in question will promptly be removed as well as all traces from git revision history.\n\n")
    
    
    
    
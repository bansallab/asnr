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
############################################################################
mydir = "voles_trapsharing_weighted/"
author = "begon" 

dt = pd.read_csv('Network_attributes.csv')
dt_sub = dt[dt['Filename'].str.contains(author)] 
location = dt_sub['Geographical Location'].iloc[0]
taxa = dt_sub['Taxa'].iloc[0]
class1 = dt_sub['Class'].iloc[0]
interaction = dt_sub['Interaction type'].iloc[0]
citn = dt_sub['Citation'].iloc[0]

#####################################################################333
def calculate_avg_wd(G, partition, n_nodes):
	r"""returns average within-module degree"""
	wdlist = []
	for node1 in G.nodes():
		nbrs = G.neighbors(node1)
		mod1 = partition[node1]
		mod_nbrs = [node2 for node2 in nbrs if partition[node2]==mod1]
		wd = len(mod_nbrs)
		wdlist.append(wd) 
		
	return sum(wdlist)/(1.*n_nodes)
	
#######################################
def calculate_Qmax(G, mod_nodes):
	r"""returns maximum modularity possible given the network partition"""
	Lt= sum([G.degree(node) for node in G.nodes()])
	total  =0
	
	for mod in mod_nodes.keys():
		Lk = sum([G.degree(node) for node in mod_nodes[mod]])
		total+= (1.0*Lk/Lt) - (1.0*Lk/Lt)**2 

	return total
######################################################################################
index_col = ['Filename','Taxa', 'Class', 'Interaction type', 'Geographical Location' ,'Nodes', 'Edges', 'Network density','Average degree', 'CV degree','Newman modularity', 'Qmax' ,'Qrel','Group cohesion','Number of modules', 'Diameter']
numeric_cols = ['Network density','Average degree', 'CV degree','Newman modularity', 'Qmax' ,'Qrel','Group cohesion','Number of modules', 'Diameter']
df = pd.DataFrame(columns=index_col)
######################################################################################

for filename in sorted(os.listdir(os.path.abspath('../Networks/'+mydir))):
	if filename.endswith(".graphml"): 
			print filename
			G= nx.read_graphml(os.path.abspath('../Networks/'+mydir+filename))
			G.remove_edges_from(G.selfloop_edges())
			n_nodes = len(G.nodes())
			n_edges = len(G.edges())

			#####
			## if network does not have weights, add a weight of one to all edges
			if len(nx.get_edge_attributes(G,'weight'))==0:
				for (n1,n2) in G.edges(): G[n1][n2]['weight']=1
			####

			####################################################
			#if no edges then return NAs
			if n_edges==0:
				row = [filename, taxa, class1, interaction, location, n_nodes, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
				df_row = pd.DataFrame([row], columns = index_col) 
				df = pd.concat([df, df_row])
				continue
			########################################################
			## remove edges with weight zero
			for (n1, n2) in G.edges():
				if G[n1][n2]['weight']==0: 
					print ("Removing NULL edge!!!"), (n1, n2), len(G.edges()),
					G.remove_edge(n1,n2)
					print len(G.edges())
			

			#########################################################
			is_connect = nx.is_connected(G) 
			num_comp = nx.number_connected_components(G)
			density = round(nx.density(G),3)
			deg_list = [G.degree(node) for node in G.nodes()]
			avg_deg = round(np.mean(deg_list),3)
			std_deg = round(np.std(deg_list),3)
	
			if avg_deg>0:cv_deg = round(float(std_deg)/avg_deg,3)
			else: cv_deg = "NA"
			if std_deg>0:
				first_part = float(n_nodes)/((n_nodes-1)*(n_nodes-2))
				sec_part = sum([(float(deg - avg_deg)/std_deg)**3 for deg in deg_list])
				skew = round(first_part*sec_part,3)
			else: skew="NA"
			wt_deg_list = [G.degree(node, weight="weight") for node in G.nodes()]
			wt_edge_list = [G[n1][n2]['weight'] for (n1,n2) in G.edges()]
			node_stg = round(np.mean(wt_deg_list),3)
			edge_stg = round(np.mean(wt_edge_list),3)
			std_node_stg = round(np.std(wt_deg_list),3)
			std_edge_stg = round(np.std(wt_edge_list),3)
			CV_node_stg = round(float(std_node_stg)/node_stg,3)
			CV_edge_stg = round(float(std_edge_stg)/edge_stg,3)
			high_node_stg = round(max(wt_deg_list),3)
			asrt = round(nx.degree_assortativity_coefficient(G),3)
			#asrt_wt = round(nx.degree_assortativity_coefficient(G, weight="weight"),3)
			betw_list  = nx.betweenness_centrality(G).values()
			betw_wt_list  = nx.betweenness_centrality(G, weight="weight").values()
			avg_betw =  round(np.mean(betw_list) ,3)
			std_betw =  round(np.std(betw_list) ,3)
			betw_wt =  round(np.mean(betw_wt_list) ,3)
			std_betw_wt =  round(np.std(betw_wt_list) ,3)
			highest_betw = max(betw_list)
			highest_betw_wt = max(betw_wt_list)
			clstr = round(nx.average_clustering(G),3)
			clstr_wt = round(nx.average_clustering(G, weight="weight"),3)
			trans = round(nx.transitivity(G),3)
			#avg_jaccard = calculate_avg_jaccard(num, G)
			#for the rest of the computations, network is required to be connected
			if not nx.is_connected(G): G = max(nx.connected_component_subgraphs(G), key=len)
			G1 = nx.Graph()
			G1.add_nodes_from(G.nodes())
			G1.add_edges_from(G.edges())
		
			partition = community.best_partition(G1)
			Q = round(community.modularity(partition, G1),3)
			modules = list(set(partition.values()))
			mod_nodes= {}
			for mod in modules: mod_nodes[mod] = [node for node in G1.nodes() if partition[node]==mod]
			Qmax = round(calculate_Qmax(G1, mod_nodes),3)
			coh = calculate_avg_wd(G1, partition, n_nodes)/(1.*avg_deg)
			diam = nx.diameter(G)
			avg_modsize = float(len(G1.nodes()))/len(modules)
			if Qmax>0:Qrel = round(float(Q)/Qmax,3)
			else: Qrel="NA"	
	
			row = [filename, taxa, class1, interaction, location, n_nodes, n_edges, density, avg_deg, cv_deg, Q, Qmax, Qrel, coh, len(modules), diam ]
			df_row = pd.DataFrame([row], columns = index_col) 
			df = pd.concat([df, df_row])
######################################################################################		
df['Taxa'] = df['Taxa'].str.replace('_', ' ')
df['Taxa'] = "*" + df['Taxa'] +"*"
df['Interaction type'] = df['Interaction type'].str.replace('_', ' ')
for col in numeric_cols: df[col] = pd.to_numeric(df[col], errors='coerce')
df=df.round(decimals=3)
base_filename = 'Readme.md'

# Get column names
cols = df.columns

# Create a new DataFrame with just the markdown
# strings
df2 = pd.DataFrame([['---',]*len(cols)], columns=cols)

#Create a new concatenated DataFrame
print df
df3 = pd.concat([df2, df])

#Save as markdown
df3.to_csv(os.path.abspath('../Networks/'+mydir+base_filename), sep="|", index=False)

with open(os.path.abspath('../Networks/'+mydir+base_filename), 'a') as file1:
    file1.write('**Citation:** '+citn)




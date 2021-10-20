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
#####################################################################333
def calculate_avg_wd(G, partition, n_nodes):
	r"""returns average within-module degree"""
	wdlist = []
	for node1 in list(G.nodes):
		nbrs = G.neighbors(node1)
		mod1 = partition[node1]
		mod_nbrs = [node2 for node2 in nbrs if partition[node2]==mod1]
		wd = len(mod_nbrs)
		wdlist.append(wd) 
		
	return sum(wdlist)/(1.*n_nodes)
	
#######################################
def calculate_Qmax(G, mod_nodes):
	r"""returns maximum modularity possible given the network partition"""
	Lt= sum([G.degree(node) for node in list(G.nodes)])
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


attr_list = ['total nodes', 'total edges', 'network density','average degree', 'degree heterogeneity', 'degree assortativity','average betweenness centrality (unweighted)', 'average betweenness centrality (weighted)', 'average clustering coefficient (unweighted)', 'average clustering coefficient (weighted)' ,'Newman modularity', 'maximum modularity' ,'relative modularity','group cohesion', 'network diameter']



directories = os.listdir(os.path.abspath('../Networks/'))
directories = [name for name in directories if name != '.DS_Store']
for mydir in directories:
	sub_directories = os.listdir(os.path.abspath('../Networks/'+mydir))
	sub_directories = [name for name in sub_directories if name != '.DS_Store']
	for subdir in sub_directories:
		print mydir, subdir
		
		#######################################
		## read qualitative attributes
		dt = pd.read_csv('Network_summary_master_file.csv')
		dt_sub =  dt[dt['dirname'].str.contains(subdir)] 
		location = dt_sub['geographical_location'].iloc[0]
		taxa = dt_sub['taxa'].iloc[0]
		taxa = taxa.replace('_', ' ')
		class1 = dt_sub['class'].iloc[0]
		interaction = dt_sub['interaction_type'].iloc[0]
		interaction = interaction.replace('_', ' ')
		edge_wt_type = dt_sub['edge_wt_type'].iloc[0]
		population_type = dt_sub['population_type'].iloc[0]
		data_record = dt_sub['data_record_technique'].iloc[0]
		total_span = dt_sub['time_span'].iloc[0]
		resolution = dt_sub['resolution'].iloc[0]
		time_span_day = dt_sub['time_span_per_day'].iloc[0]
		citn = dt_sub['Citation'].iloc[0]
		note = dt_sub['note'].iloc[0]
		definition_of_interaction = dt_sub['definition_of_interaction'].iloc[0]
		cit1 = citn.split()
		cit2 = []
		for num in xrange(len(cit1)):
			if  (num> 0 and num%7==0): 
				cit2.append(cit1[num])
				cit2.append('<br>')
			else: cit2.append(cit1[num])

	
		cit2 = ' '.join(cit2)
		
		####################################################
		num_nodes_list = []
		num_edges_list = []
		net_density_list = []
		avg_degree_list = []
		cv_degree_list = []
		modularity_list = []
		qmax_list = []
		qrel_list = []
		cohesion_list = []
		diameter_list = []
		asrt_list = []
		avg_betw_list=[]
		betw_wt_list = []
		clstr_list = []
		clstr_wt_list = []
		
		val_list = [num_nodes_list, num_edges_list, net_density_list, avg_degree_list, cv_degree_list, asrt_list, avg_betw_list, betw_wt_list, clstr_list, clstr_wt_list, modularity_list, qmax_list, qrel_list, cohesion_list, diameter_list]

		########################################3
		for filename in sorted(os.listdir(os.path.abspath('../Networks/'+mydir+'/'+subdir))):	
			if filename.endswith(".graphml"):	
				print ("filename ............"), filename
				G= nx.read_graphml(os.path.abspath('../Networks/'+mydir+'/'+subdir+'/'+ filename))
				G.remove_edges_from(nx.selfloop_edges(G))
				n_nodes = len(list(G.nodes))
				n_edges = len(list(G.edges))
		

				#####
				## if network does not have weights, add a weight of one to all edges
				if len(nx.get_edge_attributes(G,'weight'))==0:
					for (n1,n2) in list(G.edges): G[n1][n2]['weight']=1
				####

				####################################################
				#if no edges then return NAs
				if n_edges==0:continue
				########################################################
				## remove edges with weight zero
				for (n1, n2) in list(G.edges):
					if G[n1][n2]['weight']==0: 
						#print ("Removing NULL edge!!!"), (n1, n2), len(G.edges()),
						G.remove_edge(n1,n2)
						#print len(G.edges())
		
				#########################################################
				num_nodes_list.append(n_nodes)
				num_edges_list.append(n_edges)
				is_connect = nx.is_connected(G) 
				num_comp = nx.number_connected_components(G)
				density = round(nx.density(G),3)
				net_density_list.append(density)
				deg_list = [G.degree(node) for node in list(G.nodes)]
				avg_deg = round(np.mean(deg_list),3)
				avg_degree_list.append(avg_deg)
				std_deg = round(np.std(deg_list),3)

				if avg_deg>0:
					cv_deg = round(float(std_deg)/avg_deg,3)
					cv_degree_list.append(cv_deg)
				else: cv_deg = "NA"
		
				try:
					asrt = round(nx.degree_assortativity_coefficient(G),3)
					asrt_list.append(asrt)
				except: "asrt not calculated"
				#asrt_wt = round(nx.degree_assortativity_coefficient(G, weight="weight"),3)
				betw_list  = nx.betweenness_centrality(G).values()
				betw_wt_list  = nx.betweenness_centrality(G, weight="weight").values()
				avg_betw =  round(np.mean(betw_list) ,3)
				avg_betw_list.append(avg_betw)
				betw_wt =  round(np.mean(betw_wt_list) ,3)
				betw_wt_list.append(avg_betw)
				clstr = round(nx.average_clustering(G),3)
				clstr_list.append(clstr)
				clstr_wt = round(nx.average_clustering(G, weight="weight"),3)
				clstr_wt_list.append(clstr_wt)
		
				#for the rest of the computations, network is required to be connected
				if not nx.is_connected(G): G = max(nx.connected_component_subgraphs(G), key=len)
				G1 = nx.Graph()
				G1.add_nodes_from(G.nodes)
				G1.add_edges_from(G.edges)
				try:
					partition = community.best_partition(G1)
					Q = round(community.modularity(partition, G1),3)
					modularity_list.append(Q)
					modules = list(set(partition.values()))
					mod_nodes= {}
					for mod in modules: mod_nodes[mod] = [node for node in list(G1.nodes) if partition[node]==mod]
					Qmax = round(calculate_Qmax(G1, mod_nodes),3)
					qmax_list.append(Qmax)
					coh = calculate_avg_wd(G1, partition, n_nodes)/(1.*avg_deg)
					cohesion_list.append(coh)
				except: "modularity not calculated"
				
				
				diam = nx.diameter(G)
				avg_modsize = float(len(list(G1.nodes)))/len(modules)
				if Qmax>0:Qrel = round(float(Q)/Qmax,3)
				else: Qrel="NA"	
				qrel_list.append(Qrel)
	
		##################################################
		if len(num_nodes_list)==1: 
			index_col = ['network attribute','value']
			df = pd.DataFrame(columns=index_col)
			for (attr, val) in zip(attr_list, val_list):
				if len(val)==1:
					if type(val[0]) is float :  value = round(val[0],3)
					elif type(val[0]) is int: value = val[0]
					else: value = 'n/a'
					
					
				else: value = 'n/a'					
				row = [attr, value]
				df_row = pd.DataFrame([row], columns = index_col) 
				df = pd.concat([df, df_row])
		if len(num_nodes_list)>1: 
			index_col = ['network attribute','range']
			df = pd.DataFrame(columns=index_col)
			for (attr, val) in zip(attr_list, val_list):
				val = [num for num in val if not isinstance(num, basestring)]
				if len(val)>0:
					min_val = round(float(min(val)),3)
		
					max_val = round(float(max(val)),3)
					value1 = str(min_val)+ ' - '+str(max_val)
				else: value1 = 'n/a'
				row = [attr, str(min_val)+ ' - '+str(max_val)]
				#if attr =="total nodes": print row
				df_row = pd.DataFrame([row], columns = index_col) 
				df = pd.concat([df, df_row])
		
		######################################################################################		
		# Get column names
		cols = df.columns

		dt = pd.DataFrame([ ["**Study description**", "**value**"],  ["Species", "*"+taxa+"*"], ["Taxonomic class", class1], ["Population type", population_type], ["Geographical location", location], [ "Data collection technique", data_record ], [ "Interaction type", interaction], [ "Definition of interaction", definition_of_interaction], ["Edge weight type", edge_wt_type], ["Total duration of data collection", total_span], [ "Time resolution of data collection (within a day)", resolution], ["Time span of data collection (within a day)",time_span_day], ["Note", note]], columns = cols)
		
		
		df=df.round(decimals=3)
		base_filename = 'Readme.md'

		

		# Create a new DataFrame with just the markdown
		# strings
		df2 = pd.DataFrame([['---',]*len(cols)], columns=cols)
		#dt2 = pd.DataFrame([["", ""], ['---',]*len(cols)], columns=cols)

		#Create a new concatenated DataFrame
	
		#df3 = pd.concat([dt2,dt, df2, df])
		df3 = pd.concat([df2, df, dt])
		

		#Save as markdown
		df3.to_csv(os.path.abspath('../Networks/'+mydir+'/'+subdir+'/'+base_filename), sep="|", index=False, header = True)

		with open(os.path.abspath('../Networks/'+mydir+'/'+subdir+'/'+base_filename), 'a') as file1:
		    file1.write('**Citation** | '+cit2)
		
		"""
		with open(os.path.abspath('../Networks/'+mydir+'/'+subdir+'/'+base_filename), 'a') as file1:
		    file1.write('**Species**| ' + taxa +'\n')
		    file1.write('**Taxonomic class**| ' + class1+'\n')				
		    file1.write('**Population type**| '+population_type+'\n')
		    file1.write('**Geographical location**| '+location+'\n')
		    file1.write('**Data collection technique**| '+ data_record+'\n')
	            file1.write('**Edge weight type**| '+edge_wt_type+'\n')		
		    file1.write('**Time span of data collection**| '+time_span+'\n')
		    file1.write('**Time resolution of data collection**| '+resolution+'\n')
		    cit1 = citn.replace(".", ".\n")
		    file1.write('**Citation**| '+cit1)

		"""

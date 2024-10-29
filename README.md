Animal Social Network Repository 2.5
 ===============

Background
 ==========================================
 This network repository is composed of 771 networks from 80 species across 8 taxa, that are publicly available. This repository is novel in that it incorporates different animal networks that vary in sociality levels, including social, solitary and fission fusion. Networks vary in interaction criteria, edge definition, and weighted and unweighted, and in many more network properties as well. However, this repository synthesizes all of these networks in an organized, consistent manner in order to make sure that the networks are user-friendly. It is our hope that the networks in this repository further advance the field of wildlife network theory, yet the networks in this repository are not limited to questions of sociality. Due to its extensive and detailed nature, the networks found in this repository can be used to answer multiple scientific inquiries in varying fields.
 To learn more about the project, please visit our website: https://bansallab.github.io/asnr/ or read the work by Sah et al cited below.

Citation
 =================
 To cite the repository, please use:
 Melissa Collier, Pratha Sah, Jose Mendez, Sania Ali, Shweta Bansal. Animal Social Network Repository, Version 2. https://github.com/bansallab/asnr (2021)

 To cite the project and data, please use:
 Pratha Sah, José David Mendez, Shweta Bansal. A multi-species respository of social networks. Scientific Data, 6:44 (2019)

What is included?
 =================
 All networks can be found in the Networks directory. Details, descriptions and metrics for each network are found in Network_summary_masterfile.csv
 Below we summarize the networks across species and interactions.

| Taxanomic Class   |   Number of Networks | Species Represented                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:------------------|---------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Insecta           |                  287 | ['Camponotus fellah', 'Camponotus pennsylvanicus', 'Bolitotherus cornutus', 'Laupala cerasina ', 'Rhynchophorus ferrugineus ', 'Gryllus campestris ', 'Aquarius remigis ']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Mammalia          |                  336 | ['Elephas maximus', 'Papio cynocephalus', 'Myotis sodalis', 'Bison bison', nan, 'Tursiops truncatus', 'Mirounga angustirostris', 'Crocuta crocuta', 'Macropus giganteus', 'Macaca mulatta', 'Macaca fuscata', 'Trichosurus cunninghami', 'Macaca radiata', 'Macaca tonkeana', 'Pan paniscus', 'Pan troglodytes', 'Papio papio', 'Saguinus fuscicollis', 'Saguinus mystax', 'Trachypithecus johnii', 'Ateles geoffroyi', 'Alouatta guariba', 'Brachyteles arachnoides', 'Sapajus apella', 'Cercopithecus campbelli', 'Colobus guereza', 'Erythrocebus patas', 'Macaca arctoides', 'Macaca assamensis', 'Procyon lotor', 'Ovis canadensis', 'Ateles hybridus', 'Desmodus rotundus', 'Microtus agrestis', 'Equus grevyi', 'Canis familiaris ', 'Mandrillus sphinx', 'Macaca fascicularis', 'Saimiri oerstedii', 'Alouatta caraya ', 'Cryptoprocta ferox ', 'Lemur catta ', 'Dipodomys spectabilis ', 'Ursus americanus', 'Mus musculus', 'Sousa sahulensis', 'Macaca fuscata fuscata', 'Orcinus orca', 'Zalophus californianus', 'Mus musculus domesticus', 'Otospermophilus beecheyi', 'Macaca sylvanus'] |
| Aves              |                   73 | ['Hirundo rustica', 'Branta leucopsis', 'Gallus domesticus', 'Haemorhous mexicanus', 'Zonotrichia atricapilla', 'Acanthiza spp.', 'Philetairus socius', 'mixed species', 'Gallinago media', 'Gallus gallus', 'Molothrus ater', 'Myiopsitta monachus']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Actinopterygii    |                   16 | ['Poecilia reticulata', 'Gasterosteus aculeatus']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Reptilia          |                   55 | ['Tiliqua rugosa', 'Gopherus agassizii', 'Agkistrodon contortrix ']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Arachnid          |                    1 | [' Serracutisoma proximum']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Cephalapoda       |                    1 | ['Sepia apama ']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Amphibia          |                    2 | ['Dendrobates pumilio ', 'Epidalea calamita']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

| Interaction Type                | General Definition                                                                                                            |   Number of Networks |
|:--------------------------------|:------------------------------------------------------------------------------------------------------------------------------|---------------------:|
| physical contact                | Physical contact occurs between individuals that are not grroming, trophallaxis, or dominance behaviors.                      |                  252 |
| trophallaxis                    | Mouth to mouth foodsharing behaviors                                                                                          |                   16 |
| dominance                       | Physical contact unique to aggressive dominance interactions such as biting, head butting, fighting, etc.                     |                   23 |
| spatial proximity               | No physical contact, individuals are just within a certain distance of eachother as indicated by the study                    |                  115 |
| grooming                        | Physical contact unique to grooming interactions in primates                                                                  |                   62 |
| social projection bipartite     | A projection of a bipartite network in which individuals are connected to all locations visted (e.g. feeder sharing networks) |                  218 |
| overall mix                     | Connections are based on multiple different types of interactions                                                             |                    3 |
| foraging                        | Individuals are connected if they were seen foraging together                                                                 |                    2 |
| group membership                | Individuals are connected if seen as part of the same group as defined by the research study                                  |                   16 |
| Food sharing                    | Individuals are connected sharing the same food source                                                                        |                    1 |
| Fluid Exchange mating           | Indiivduals are connected if mating involving fluid excahnge occurred (e.g. intromission)                                     |                   58 |
| No Fluid Exchange mating        | Individuals are connected if mating that does not involve fluid exhange occurred (e.g. spore transfer)                        |                    3 |
| non physical social interaction | Direct interaction between individuals that does not involve physical contact (e.g. sniffing, chasing)                        |                    2 |

Glossary of qualatative study description terms 
 ===================================
 All terms below are found as qualatative columns in the Network_summary_masterfile.csv

Network ID: Unique identifier of the network in the Networks directory.

Network Identifiers: Descriptive terms to differentiate multiple networks taken from one study. Could include years, colony names, trap names, etc.

Taxonomic class: Taxonomic class of the species. Could be ['Insecta', 'Mammalia', 'Aves', 'Actinopterygii', 'Reptilia', 'Arachnid', 'Cephalapoda', 'Amphibia'].

Population type: Type of animal population recorded. Could be captive, semi-ranging or free-ranging.

Georgraphical location: Location where the population(s) were recorded.

Data collection technique: Method of data collection including focal sampling, survey scan, mark recapture, RFID, radio tags, video recording, etc.

Interaction type: Type of association/interaction recorded between animal pairs to construct the social network.

Definition of interaction: Criteria of occurence of an association/interaction as defined in the study.

Edge weight type: Criteria of weighting network edges. Could be based on frequency, duration, intensity of interactions or metrics such as simple ratio index, half weight index etc.

Total duration of data collection: Total time span over which the social network data was collected.

Time resolution of data colllection (within a day): Resolution of data collection within a day.

Time span of data collection (within a day): Total duration of data collection within a day.

Attributes Available: The node attributes provided in the study. If available, they are included in the graphml files. 

Note: Additional notes on the dataset. 

Glossary of quantative network metrics
 ===================================
 All metrics below are found as columns in the Network_summary_masterfile.csvIs connected: Binary value to determine if the network is fully connected (TRUE) or is composed of multiple components (FAlSE)

Num Components: The number of connected components in the network.

Nodes: The number of individuals in the network.

Edges: The number of connections in the network. 

Network Density: The proportion of existing edges in the network out of the total number of possible edges. 

Highest Degree: The highest degree value for a node in the network. 

Average/Standard Deviation Degree: The average number of or standard deviation in contacts for all nodes in the network. 

CV Degree: The coefficient of variation in the network. Equal to the average degree divided by the standard deviation.

Skewness: A measure of the asymmetry of the network's degree dsitribution. 

Average/Standard Deviation Node Strength: The averagea and standard deviation of the sum of all the edgeweights connected to each node in the network. 

CV Node Strength: The coefficient of variation of edge strength calculated as the average strength divided by the standard deviation. 

Highest Node Strength: The highest strength value in the network. 

Average/Standard Deviation Edge Strength: The mean and standard deviation in edge weight values. 

CV Edge Strength: The coefficient of vairation in edge weight values, calculated as the average edge weight divided by the standard deviation. 

Degree Assortativity: The tendency of contacts to have a similar number of contacts. Higher values mean high dgree individuals form more bonds, lower values mean that high degree individuals form bonds with low degree individuals. 

Average/Standard Devioation Betweenness Centrality (Weighted/Unweighted): The tendency for nodes to occupy a central position in the network. Higher values mean the network has more central or bridge nodes. Values calculated both with and without edge weights. 

Highest Betweenness Centrality (Weighted/Unweighted): The higest betweeness value in the network, both with and without edgeweights. 

Clustering Coefficient (Weighted/Unweighted): The tendancy for a set of three individuals to be connected, or for an individuals contacts to interact with eachother. Calculated both with and without edgeweights. 

Newman's Modularity (Q): The strength of subdividisions or communities within the network. Based on Newman's definition. 

Qmax: The maximum modularity value. 

Qrel: Modularity, (Q) normalized by Qmax. 

Number of Modules: The number of modules or communities in the network.  

Average Module Size': THe average number of nodes in each mondule or community. 

Cohesion: The tendancy for individuals to interact with their own module. 

Diameter: The longest of all the shortest path lengths for all node pairs in the network. Calculated on the largest connected component. 

Adding data
 ===========
 One of the main goals of this repository is to further enhance the study of animal social networks. If you happen to come across any interesting data on animal networks that has been published and is not yet included in this repository, please contact us. We will do our best to make it consistent with our format and add it to the repository. Requests should be filed to shweta@sbansal.com

License
 =======
 All datasets in this repository were made publicly available in other data repositories. You will find a link to the original source of the network, additionally to the study in which the data was collected. A great amount of effort was made to determine the license under which the datasets were distributed, and it is our understanding that the datasets are free to redistribute. However, if you own the rights to any dataset that is included in this repository and you object their inclusion, please email shweta@sbansal.com. The data in question will promptly be removed as well as all traces from git revision history.


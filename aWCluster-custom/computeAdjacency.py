import numpy as np
from scipy.spatial.distance import cdist, pdist, squareform

# Considers the embedding elements as different dimensions in euclidean plane and applies the distance formula
def dim_euclid_Adjacency(clinicalembed, molecularembed, pathologyembed, wsiembed):
    concatembed = np.concatenate([clinicalembed, pathologyembed, wsiembed, molecularembed], axis=1)
    adj_matrix = cdist(concatembed, concatembed, metric='euclidean')
    mean = np.mean(adj_matrix)
    stddev = np.std(adj_matrix)
    bin_adj_matrix = (adj_matrix >= (mean+stddev)).astype(int)
    return bin_adj_matrix # Returns shape of (x, x) where x is the number of patients, each having 3120 embedding elements

# Finds the sum of all concatenated embedding elements of each patient and applies the distance formula (we only have one dimension in this case)
def sum_euclid_Adjacency(clinicalembed, molecularembed, pathologyembed, wsiembed):
    concatembed = np.concatenate([clinicalembed, pathologyembed, wsiembed, molecularembed], axis=1)
    sumc_concatembed = np.sum(concatembed, axis=1)
    adj_matrix = squareform(pdist(sumc_concatembed.reshape(-1, 1), metric='euclidean'))
    mean = np.mean(adj_matrix)
    stddev = np.std(adj_matrix)
    bin_adj_matrix = (adj_matrix>= (mean+stddev)).astype(int)
    return bin_adj_matrix # Returns shape of (x, x) where x is the number of patients, each having 3120 embedding elements
# Functions above, if applied on transpose of 'cancatembed' result in adjacencies of shape (3120, 3120) 

# Considering each patient a different dimension for every column of an embedding element. (Embeddings of different modalities are combined by use of integrative measure)
def invt_dim_euclid_Adjacency(invt):
    adj_matrix = cdist(invt.T, invt.T, metric='euclidean')
    mean = np.mean(adj_matrix)
    stddev = np.std(adj_matrix)
    bin_adj_matrix = (adj_matrix >= (mean+15*stddev)).astype(int) # the thresholding can be changed as per cpu requirement
    return bin_adj_matrix # Returns shape of (1024, 1024)

# Finds the sum of all patient's embedding elements from each column and applies the distance formula (we only have one dimension in this case i.e summed embedding elements)
def invt_sum_euclid_Adjacency(invt):
    sum_invt = np.sum(invt, axis=0)
    adj_matrix = squareform(pdist(sum_invt.reshape(-1, 1), metric='euclidean'))
    mean = np.mean(adj_matrix)
    stddev = np.std(adj_matrix)
    bin_adj_matrix = (adj_matrix>= (mean+stddev)).astype(int)
    return bin_adj_matrix # Returns shape of (1024, 1024)

# Considering each patient/ embedding element a different dimension for every column/ row of an embedding element. (Embeddings of different modalities are combined by summing their )
def noc_dim_euclid_Adjacency(clinicalembed, molecularembed, pathologyembed, wsiembed, flag=1):
    sum_embed = np.sum(clinicalembed, pathologyembed, wsiembed, molecularembed) # --> Results in (x, 1024)
    if flag==0:
        adj_matrix = cdist(sum_embed, sum_embed, metric='euclidean')
    else:
        adj_matrix = cdist(sum_embed.T, sum_embed.T, metric='euclidean')
    mean = np.mean(adj_matrix)
    stddev = np.std(adj_matrix)
    bin_adj_matrix = (adj_matrix >= (mean+stddev)).astype(int)
    return bin_adj_matrix # Returns shape of (x, x) where x is no. of pat if flag ==1 else: (1024, 1024)

# Combines modalities by summing the embedding elements. Finds the sum of all patient's embedding elements from each column and applies the distance formula (we only have one dimension in this case i.e summed embedding elements)
def noc_sum_euclid_Adjacency(clinicalembed, molecularembed, pathologyembed, wsiembed, flag=1):
    sum_embed = np.sum(clinicalembed, pathologyembed, wsiembed, molecularembed) # --> Results in (x, 1024)
    if flag ==0:
        sum_pat = np.sum(sum_embed, axis=1)
    else:
        sum_pat = np.sum(sum_embed, axis=0)
    adj_matrix = squareform(pdist(sum_pat.reshape(-1, 1), metric='euclidean'))
    mean = np.mean(adj_matrix)
    stddev = np.std(adj_matrix)
    bin_adj_matrix = (adj_matrix>= (mean+stddev)).astype(int)
    return bin_adj_matrix # Returns shape of (x, x) if flag =0, else: (1024, 1024)

# Add another method of combining different modalities by finding distances between each embedding element of each modality.
# e.g a =[[7, 6, 9], [7, 2, 1], [9, 4, 2]] --> modality 1
# e.g b =[[5, 3, 6], [2, 4, 2], [7, 4, 3]] --> modality 2 
# e.g c =[[9, 2, 3], [2, 3, 1], [1, 6, 4]] --> modality 3
# Then result [0, 0] = sqrt(sq(7-5)+sq(7-9)+sq(5-9))
# Subsequently, result [n, m] = sqrt(sq(a[n, m]-b[n, m])+ sq(a[n, m]-c[n, m])+ sq(b[n, m]-c[n, m]))
# Result is of shape (3, 3) in the example above but follows the shape of modality
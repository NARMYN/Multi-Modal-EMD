import numpy as np
import time
from invariant import invariant_4
from EMD_convexOpt import EMD_convexOpt
from computeAdjacency import dim_euclid_Adjacency, invt_dim_euclid_Adjacency
import pandas as pd
from pathlib import Path

# User input for the subtype of cancer
subtype = input('Enter the Cancer Subtype that you would like to work with...(choose from ESCA, BLCA, CESC, LUSC, HNSC)\n')

# Start timing
start_time = time.time()

# Load the data files for each modality
clinicaldf = pd.read_parquet(f'{subtype}/Data/filtered_{subtype}_clinical_embeddings.parquet')
moleculardf = pd.read_parquet(f'{subtype}/Data/filtered_{subtype}_molecular_embeddings.parquet')
pathologydf = pd.read_parquet(f'{subtype}/Data/filtered_{subtype}_pathology_embeddings.parquet')
wsidf = pd.read_parquet(f'{subtype}/Data/filtered_{subtype}_wsi_embeddings1.parquet')

# Extract and Preprocess the embeddings from data files
clinicalembed= np.array(clinicaldf['Embeddings'].tolist())
molecularembed0 = np.array(moleculardf['Embeddings'].tolist())
pathologyembed= np.array(pathologydf['Embeddings'].tolist())
wsiembed= np.array(wsidf['Embeddings'].tolist())

# Padding zeros at the end of molecular embeddings
pad_length = 1024 - molecularembed0.shape[1]
molecularembed = np.pad(molecularembed0, ((0, 0), (0, pad_length)), mode='constant', constant_values=0)

# Calculate Adjacency for invariant
Adj1 = dim_euclid_Adjacency(clinicalembed, pathologyembed, wsiembed, molecularembed)

# Calculate the invariants
invt = invariant_4(Adj1, clinicaldf['Patient'], clinicalembed, pathologyembed, wsiembed, molecularembed)
Node_weights = invt

# Calculate Adjacency for EMD
Adj2 = invt_dim_euclid_Adjacency(invt)
# print(sum(Adj2.reshape(-1, 1)))

# Calculate the distance matrix using the custom function
distanceM = EMD_convexOpt(Adj2, Node_weights.T)

# End timing
end_time = time.time()

print(f"Elapsed time: {end_time - start_time} seconds")

# Optionally save the distance matrix to a .csv file
mydf = pd.DataFrame(distanceM)
path = Path(f'{subtype}/Distance_Matrix')
path.mkdir(parents=True, exist_ok=True)
mydf.to_csv(f'{subtype}/Distance_Matrix/trial4.csv', header=False)

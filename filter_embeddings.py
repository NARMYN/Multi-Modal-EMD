import pandas as pd

# Read the parquet files into DataFrames
# Clinical = (504, 1024)
# Molecular = (491, 1024)
# Pathology = (504, 1024)
# WSI = (503, 1024)
clinicaldf = pd.read_parquet('BLCA_clinical_embeddings.parquet')
moleculardf = pd.read_parquet('BLCA_molecular_embeddings.parquet')
pathologydf = pd.read_parquet('BLCA_pathology_embeddings.parquet')
wsidf = pd.read_parquet('best_attention_batchpadding_pooled_features_2.parquet')
# wsidf = pd.read_parquet('BLCA_wsifortest_embeddings.parquet')

# Identify common patients across all three DataFrames
common_patients = set(clinicaldf['Patient']).intersection(moleculardf['Patient']).intersection(pathologydf['Patient']).intersection(wsidf['PatientID'])
feature_columns = [f'feature_{i}' for i in range(1024)]
wsidf['Embeddings'] = wsidf[feature_columns].values.tolist()
# Filter each DataFrame to keep only the common patients
filtered_clinicaldf = clinicaldf[clinicaldf['Patient'].isin(common_patients)]
filtered_moleculardf = moleculardf[moleculardf['Patient'].isin(common_patients)]
filtered_pathologydf = pathologydf[pathologydf['Patient'].isin(common_patients)]
filtered_wsidf = wsidf[wsidf['PatientID'].isin(common_patients)]
# filtered_wsidf = wsidf[wsidf['Patient'].isin(common_patients)]

# Save the filtered DataFrames back to Parquet files
filtered_clinicaldf.to_parquet("filtered_BLCA_clinical_embeddings.parquet")
filtered_moleculardf.to_parquet("filtered_BLCA_molecular_embeddings.parquet")
filtered_pathologydf.to_parquet("filtered_BLCA_pathology_embeddings.parquet")
filtered_wsidf.to_parquet('filtered_BLCA_wsi_embeddings2.parquet', index=False)
# filtered_wsidf.to_parquet("filtered_BLCA_wsifortest_embeddings.parquet")
print("files are saved...")
# # Optionally, print the filtered DataFrames
# print(filtered_df1)
# print(filtered_df2)
# print(filtered_df3)

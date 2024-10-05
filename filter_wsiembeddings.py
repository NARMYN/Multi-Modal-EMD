import pandas as pd

clinicaldf = pd.read_parquet('CESC_clinical_embeddings.parquet')
moleculardf = pd.read_parquet('CESC_molecular_embeddings.parquet')
pathologydf = pd.read_parquet('CESC_pathology_embeddings.parquet')
wsidf = pd.read_parquet('best_attention_batchpadding_pooled_features.parquet')

# Identify common patients across all three DataFrames
common_patients = set(clinicaldf['Patient']).intersection(moleculardf['Patient']).intersection(pathologydf['Patient']).intersection(wsidf['PatientID'])

# Step 2: Combine the feature columns into a list (embedding)
feature_columns = [f'feature_{i}' for i in range(1024)]
wsidf['Embeddings'] = wsidf[feature_columns].values.tolist()
filtered_wsidf = wsidf[wsidf['PatientID'].isin(common_patients)]

# Step 3: Create the new DataFrame with 'patient-id' and 'embeddings'

# Step 4: Save the new DataFrame as a Parquet file
filtered_wsidf.to_parquet('filtered_CESC_wsi_embeddings1.parquet', index=False)

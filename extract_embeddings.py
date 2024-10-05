from datasets import load_dataset
import pandas as pd
import os
from torch.utils.data import Dataset
import numpy as np
clinical_dataset = load_dataset("Lab-Rasool/TCGA", "clinical", split="train")
#wsi_dataset = load_dataset("Lab-Rasool/TCGA", "wsi", split="train")
embeddings1 =[]
embeddings2 =[]
embeddings3 =[]
embeddings4 =[]
embeddings5 =[]

for index, item in enumerate(clinical_dataset):
    #print(index, item)
    if (item['project_id']=='TCGA-HNSC'):
        embeddings1.append(np.frombuffer(item.get("embedding"), dtype=np.float32))
    elif (item['project_id']=='TCGA-LUSC'):
        embeddings2.append(np.frombuffer(item.get("embedding"), dtype=np.float32))
    elif (item['project_id']=='TCGA-BLCA'):
        embeddings3.append(np.frombuffer(item.get("embedding"), dtype=np.float32))
    elif (item['project_id']=='TCGA-CESC'):
        embeddings4.append(np.frombuffer(item.get("embedding"), dtype=np.float32))
    elif (item['project_id']=='TCGA-ESCA'):
        embeddings5.append(np.frombuffer(item.get("embedding"), dtype=np.float32))


# Save embeddings to file
np.savetxt("HNSC_clinical_embeddings.csv", embeddings1)
print(f"Saved embeddings to HNSC_clinical_embeddings.csv")
np.savetxt("LUSC_clinical_embeddings.csv", embeddings2)
print(f"Saved embeddings to LUSC_clinical_embeddings.csv")
np.savetxt("BLCA_clinical_embeddings.csv", embeddings3)
print(f"Saved embeddings to BLCA_clinical_embeddings.csv")
np.savetxt("CESC_clinical_embeddings.csv", embeddings4)
print(f"Saved embeddings to CESC_clinical_embeddings.csv")
np.savetxt("ESCA_clinical_embeddings.csv", embeddings5)
print(f"Saved embeddings to ESCA_clinical_embeddings.csv")


'''dataset = load_dataset("Lab-Rasool/TCGA", 'clinical')
print(dataset)
for ds_name, ds in dataset.items():
    print(f"Dataset: {ds_name}")
    # Extract the embeddings assuming each item is a dictionary with an 'embeddings' key
    embeddings1 = [item['embedding'] for item in ds if (item['project_id']=='TCGA-HNSC')]
    embeddings2 = [item['embedding'] for item in ds if (item['project_id']=='TCGA-LUSC')]
    embeddings3 = [item['embedding'] for item in ds if (item['project_id']=='TCGA-BLCA')]
    embeddings4 = [item['embedding'] for item in ds if (item['project_id']=='TCGA-CESC')]
    embeddings5 = [item['embedding'] for item in ds if (item['project_id']=='TCGA-ESCA')]
    
    # Convert list of embeddings to DataFrame
    df_embeddings1 = pd.DataFrame(embeddings1)
    df_embeddings2 = pd.DataFrame(embeddings2)
    df_embeddings3 = pd.DataFrame(embeddings3)
    df_embeddings4 = pd.DataFrame(embeddings4)
    df_embeddings5 = pd.DataFrame(embeddings5)
    
    # Save embeddings to file
    df_embeddings1.to_csv(f"{ds_name}_HNSC_clinical_embeddings.csv", index=False)
    print(f"Saved embeddings for {ds_name} to {ds_name}_HNSC_clinical_embeddings.csv")
    df_embeddings2.to_csv(f"{ds_name}_LUSC_clinical_embeddings.csv", index=False)
    print(f"Saved embeddings for {ds_name} to {ds_name}_LUSC_clinical_embeddings.csv")
    df_embeddings3.to_csv(f"{ds_name}_BLCA_clinical_embeddings.csv", index=False)
    print(f"Saved embeddings for {ds_name} to {ds_name}_BLCA_clinical_embeddings.csv")
    df_embeddings4.to_csv(f"{ds_name}_CESC_clinical_embeddings.csv", index=False)
    print(f"Saved embeddings for {ds_name} to {ds_name}_CESC_clinical_embeddings.csv")
    df_embeddings5.to_csv(f"{ds_name}_ESCA_clinical_embeddings.csv", index=False)
    print(f"Saved embeddings for {ds_name} to {ds_name}_ESCA_clinical_embeddings.csv")

dataset = load_dataset("Lab-Rasool/TCGA", 'molecular')
print(dataset)

for ds_name, ds in dataset.items():
    print(f"Dataset: {ds_name}")
    # Extract the embeddings assuming each iten is a dictionary with an embeddings key
    embeddings = [item['Embeddings'] for item in ds]
    df_embeddings = pd.DataFrame(embeddings)
    df_embeddings.to_csv(f"{ds_name}_molecular_embeddings.csv", index=False)
    print(f"Saved embeddings for {ds_name} to {ds_name}_molecular_embeddings.csv")'''

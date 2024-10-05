# Earth Mover's Distance on Multi-Modal Data

This repository contains implementation of wasserstein distance on embeddings based multi-modal data of cancer subtypes 

## Introduction

**This research work implements the integrative approach suggested in the paper '[aWCluster: A Novel Integrative Network-Based Clustering of Multiomics for Subtype Analysis of Cancer Data](https://dl.acm.org/doi/10.1109/TCBB.2020.3039511)' for multi-omics on the multi-modal data of four different modalities and five cancer subtypes**

### Cancer Subtypes

| Cancer Subtype    | No. of common Samples/ PatientIDs (x)   |
|------|-----|
| ESCA | 184 |
| CESC | 294 |
| BLCA | 406 |
| LUSC | 490 |
| HNSC | 520 |

### Modalities

The embeddings are extracted from the [custom dataset](https://huggingface.co/datasets/Lab-Rasool/TCGA) of Moffitt Cancer Centre
| Modality    | Embedding Length   |
|------|-----|
| Clinical Data | 1024 |
| Pathology Reports | 1024 |
| Whole Slide Images | 1024 |
| Molecular Data | 48 |

## Methodology

- The subtype-specific embeddings are first **extracted** from the provided dataset using the `get_embeddings.py` file. The WSI embeddings are taken from `best_attention_batchpadding_pooled_features.parquet` or `best_attention_batchpadding_pooled_features_2.parquet` that is a result of `ABMIL`
- The embeddings of each modality are then filtered, to only include the embeddings of patients that are common in all modalities, by using the `filter_embeddings.py` file
- The extracted and filtered results are saved in _.parquet_ file format in the `{Sub-type}/Data` directory i.e in the Data folder inside the folder of each cancer subtype
- The Adjacencies are calculated for the embedding-element specific or patient-specific graphs, where nodes are either patients/samples or embedding elements, respectively. All possible methods for adjacency calculations are placed in `aWCluster-Custom/computeAdjacency.py` file
- The patient-specific invariant is calculated in `invariant.py` file for the specified subtype of cancer by the use of Markov Chains based Integrative Measure technique mentioned in the AWCluster paper (2.1) to merge the modalities for all patients of each cancer subtype and generate node weights
- The Earth Mover's Distance is calculated by using the integrative measures and adjacencies computed above, and the `main_EarthMoversDistance.py` file

### Dimensionality Specifications

| Item  `<Destination>`  | Resulting Dimensions for `<Destination>` |
|------|-----|
| Adjacency `invariant`| (x, x) |
| Adjacency `EMD_convexOpt`| (1024, 1024) |
| Invariant `EMD_convexOpt`| (x, 1024) | 
| Embeddings `invariant` | (x, 1024) |
| Embeddings `computeAdjacency` | (x, 1024) |

Hence, each modality is required to have 1024 embedding elements for each patient. To adhere to this requirement, the molecular embeddings are padded with zeros at the end in `line 29` of `main_EarthMoversDistance.py` file to change its shape from `(x, 48)` to `(x, 1024)`

### Adjacency Methods







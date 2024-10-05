# Multi-Modal-EMD

This repository contains implementation of wasserstein distance on embeddings based multi-modal data of cancer subtypes 

## Introduction

**This research work implements the integrative approach suggested in the paper '[aWCluster: A Novel Integrative Network-Based Clustering of Multiomics for Subtype Analysis of Cancer Data](https://dl.acm.org/doi/10.1109/TCBB.2020.3039511)' for multi-omics on the multi-modal data of four different modalities and five cancer subtypes**

### Cancer Subtypes

| Cancer Subtype    | No. of Samples/ Patients (x)   |
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



import numpy as np

def invariant_4(Adj, PATIENT_s, CLINICAL_s, PATHOLOGY_s, WSI_s, MOLECULAR_s):
    # PATHOLOGY_s = 1 - PATHOLOGY_s
    n = CLINICAL_s.shape[1]
    m = len(PATIENT_s)
    invt3 = np.zeros_like(CLINICAL_s)
    Adj2 = Adj + np.eye(m)

    for i in range(n):
        C_sum = np.sum(CLINICAL_s[:, i, np.newaxis] * Adj, axis=0)
        W_sum = np.sum(WSI_s[:, i, np.newaxis] * Adj, axis=0)
        P_sum = np.sum(PATHOLOGY_s[:, i, np.newaxis] * Adj, axis=0)
        M_sum = np.sum(MOLECULAR_s[:, i, np.newaxis] * Adj, axis=0)

        P_W_M_sum = np.sum(PATHOLOGY_s[:, i, np.newaxis] * WSI_s[:, i, np.newaxis] * MOLECULAR_s[:, i, np.newaxis] * Adj2, axis=0)
        n_Adj2 = np.sum(Adj2, axis=0)
        eps = P_W_M_sum / n_Adj2

        W_cli = CLINICAL_s[:, i] * C_sum
        W_pat = PATHOLOGY_s[:, i] * P_sum
        W_wsi = WSI_s[:, i] * W_sum
        W_mol = MOLECULAR_s[:, i] * M_sum

        invt3[:, i] = eps * W_cli * (W_pat + W_wsi + W_mol)

    return invt3
#290 genes/sample, 100 samples
# print(invariant_3(Adj, gene_s, CLINICAL_s, PATHOLOGY_s, WSI_s))
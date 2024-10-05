import numpy as np
from joblib import Parallel, delayed
from ComputeGraphProb import ComputeGraphProb
from dist_Convex import dist_Convex

def EMD_convexOpt(Adj, Node_weights):
    Node_Prob = ComputeGraphProb(Adj, Node_weights)
    l = Node_weights.shape[1]
    n = len(Adj)
    m = np.sum(Adj) // 2

    D = np.zeros((n, m))
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if Adj[i, j]:
                D[i, count] = 1
                D[j, count] = -1
                count += 1

    Distance_Matrix = np.zeros((l, l))

    def calculate_distance(i):
        distance_matrix_row = np.zeros(l)
        for j in range(i + 1, l):
            rho0 = Node_Prob[:, i]
            rho1 = Node_Prob[:, j]
            drho = rho0 - rho1
            drho -= np.mean(drho)
            distance_matrix_row[j] = dist_Convex(drho, D, m)
        return i, distance_matrix_row

    results = Parallel(n_jobs=-1)(delayed(calculate_distance)(i) for i in range(l - 1))

    for i, row in results:
        Distance_Matrix[i, :] = row

    distanceM = Distance_Matrix + Distance_Matrix.T
    return distanceM

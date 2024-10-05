import numpy as np

def ComputeGraphProb(Adj, Node_weights):
    l = Node_weights.shape[1]  # Number of columns in Node_weights
    n = Adj.shape[0]           # Number of rows in Adj (assuming it's square)
    
    I = np.ones((l, 1))        # Column vector of ones with length l
    
    S = np.sum(Node_weights, axis=0)  # Sum across columns of Node_weights
    S_copy = np.tile(S, (n, 1))       # Repeat S n times along rows to create S_copy
    
    # Node_Prob = Node_weights / S_copy # Element-wise division to get Node_Prob

    # To avoid division by zero, use np.where to replace zero values in S_copy
    Node_Prob = np.divide(Node_weights, S_copy, where=S_copy != 0, out=np.zeros_like(Node_weights))  # Safe division replacing the results of zero division by zero
    
    return Node_Prob
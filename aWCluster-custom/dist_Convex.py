import cvxpy as cp
import numpy as np

def dist_Convex(drho, D, m):
    # Define the variable
    u = cp.Variable(m)

    # Define the objective
    objective = cp.Minimize(cp.norm1(u))

    # Define the constraints
    constraints = [drho + D @ u == 0]

    # Form and solve the problem
    prob = cp.Problem(objective, constraints)
    prob.solve(solver=cp.SCS, verbose=False)  # Using SCS solver as an alternative

    # Return the optimal value
    distanceM = prob.value
    return distanceM

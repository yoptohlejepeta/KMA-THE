from pulp import *


matice = [
    [4, 2, 3],
    [3, 5, 4],
    [2, 1, 4]
]

def druhy_hrac(matice):
    prob = LpProblem("Uloha2", LpMaximize)
    
    variables = []
    for i in range(len(matice)):
        variables.append(LpVariable("x" + str(i), 0, 1, LpInteger))
    
    prob += lpSum([variables[i] for i in range(len(matice))])
    print(lpSum([variables[i] for i in range(len(matice))]))
    
    for i in range(len(matice)):
        prob += lpSum([variables[j] * matice[j][i] for j in range(len(matice))]) <= 1
        
    prob.solve()
    return [value(x) for x in variables]

print(druhy_hrac(matice))
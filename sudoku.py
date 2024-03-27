from pulp import *

problem = LpProblem("sudoku", LpMinimize)
#Objective function
problem += 0

values = range(1, 10)
rows = range(1, 10)
columns = range(1, 10)

data = [['5', '3', '_','_', '7', '_','_', '_', '_'],
        ['6', '_', '_','1', '9', '5','_', '_', '_'],
        ['_', '9', '8','_', '_', '_','_', '6', '_'],
        ['8', '_', '_','_', '6', '_','_', '_', '3'],
        ['4', '_', '_','8', '_', '3','_', '_', '1'],
        ['7', '_', '_','_', '2', '_','_', '_', '6'],
        ['_', '6', '_','_', '_', '_','2', '8', '_'],
        ['_', '_', '_','4', '1', '9','_', '_', '5'],
        ['_', '_', '_','_', '8', '_','_', '7', '9']]

variables = LpVariable.dicts("Choice", (values, rows, columns), cat="Binary")

# Creating 3x3 boxes
boxes = [[(3*i + k + 1, 3*j + l + 1) for k in range(3) for l in range(3)] for i in range(3) for j in range(3)]

# one value per slot
for r in rows:
    for c in columns:
        problem += lpSum([variables[v][r][c] for v in values]) == 1

# row, column, box constraints
for v in values:
    for r in rows:
        problem += lpSum([variables[v][r][c] for c in columns]) == 1
    for c in columns:
        problem += lpSum([variables[v][r][c] for r in rows]) == 1
    for b in boxes:
        problem += lpSum([variables[v][r][c] for (r, c) in b]) == 1

#setting predefined values
set_values = []
for i in data:
    for j in i:
        if j != '_':
            set_values.append([int(j),data.index(i) + 1,i.index(j) + 1])

for i in set_values:
    problem += variables[i[0]][i[1]][i[2]] == 1

result = problem.solve()

solved_variables = []

for r in rows:
    for c in columns:
        for v in values:
            if value(variables[v][r][c]) == 1:
                solved_variables.append(v)

solved_field = [[] for i in range(9)]

for i in solved_field:
    solved_field[solved_field.index(i)] = solved_variables[0 + 9*solved_field.index(i): 9 + 9*solved_field.index(i)]

for i in solved_field:
    print(i)
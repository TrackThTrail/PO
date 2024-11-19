from pulp import LpProblem, LpVariable, LpMinimize, lpSum

b = [10, 8, 12, 15, 9, 11, 14, 16, 13, 18, 20, 22, 19, 21, 17, 15, 13, 12, 11, 10, 8, 7, 6, 5]  # demanda horária
c = 5
n = 24

problem = LpProblem("Frota_de_Onibus", LpMinimize)

x = [LpVariable(f"x_{i}", lowBound=0, cat="Integer") for i in range(n)]

s = [LpVariable(f"s_{i}", lowBound=0, cat="Integer") for i in range(n)]

problem += lpSum([c * (s[i] - b[i]) for i in range(n)]), "Custo_Adicional_Total"

for i in range(n):
    problem += s[i] == lpSum([x[(i - k) % n] for k in range(6)]), f"Calculo_Onibus_Hora_{i}"
    problem += s[i] >= b[i], f"Demanda_Minima_Hora_{i}"

problem.solve()

print("Status da solução:", problem.status)
for i in range(n):
    print(f"Hora {i + 1}: x_{i} = {x[i].varValue}, s_{i} = {s[i].varValue}")

print("Custo adicional total:", problem.objective.value())

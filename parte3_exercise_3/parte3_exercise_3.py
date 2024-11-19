from pulp import LpMaximize, LpProblem, LpVariable

# Criação do problema
problem = LpProblem("Refinaria", LpMaximize)

# Variáveis de decisão
x1 = LpVariable("Gasolina", lowBound=0, cat="Continuous")  # Quantidade de gasolina bruta
x2 = LpVariable("Gas_Oleo", lowBound=0, cat="Continuous")  # Quantidade de gás e óleo

# Função objetivo
problem += 10 * x1 + 7 * x2, "Lucro_Total"

# Restrições
problem += x1 <= 400000, "Restricao_Reforming"
problem += x2 <= 450000, "Restricao_Cracking"
problem += 600 * x1 + 500 * x2 <= 300000, "Restricao_Destilacao"  # Multiplicado por 300.000 (m.m.c. de 500 e 600)
problem += 500 * x1 + 700 * x2 <= 350000, "Restricao_Dessulfuracao"  # Multiplicado por 350.000 (m.m.c. de 700 e 500)

# Resolução do problema
problem.solve()

# Resultados
print("Status:", problem.status)
print("Solução Ótima:")
print(f"Gasolina (x1): {x1.varValue}")
print(f"Gas/Oleo (x2): {x2.varValue}")
print(f"Lucro Total: {problem.objective.value()}")

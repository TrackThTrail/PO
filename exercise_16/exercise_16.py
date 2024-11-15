from pulp import LpProblem, LpMaximize, LpVariable, LpStatus, value

# Criação do problema de otimização
prob = LpProblem("Maximizar_Lucro_Produção", LpMaximize)

# Variáveis de decisão: número de camisas e blusas a serem produzidas
x_1 = LpVariable("Camisas", lowBound=0, cat="Integer")
x_2 = LpVariable("Blusas", lowBound=0, cat="Integer")

# Função objetivo: maximizar o lucro
prob += 8 * x_1 + 12 * x_2  # Lucro total

# Restrições
prob += 20 * x_1 + 60 * x_2 <= 2400  # Restrição de corte
prob += 70 * x_1 + 60 * x_2 <= 84000  # Restrição de costura
prob += 12 * x_1 + 4 * x_2 <= 12000  # Restrição de embalagem

# Resolução do problema
prob.solve()

# Resultados
print(f"Status: {LpStatus[prob.status]}")
print(f"Camisas a serem produzidas (x_1): {value(x_1)} unidades")
print(f"Blusas a serem produzidas (x_2): {value(x_2)} unidades")
print(f"Lucro Total: ${value(prob.objective)}")

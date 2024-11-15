from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpStatus, value

# Criação do problema de otimização
prob = LpProblem("Maximizar_Lucro_Chapas_Barras", LpMaximize)

# Variáveis de decisão
x = LpVariable("Chapas", lowBound=0, cat="Integer")
y = LpVariable("Barras", lowBound=0, cat="Integer")

# Função objetivo: maximizar o lucro
prob += 40 * x + 35 * y

# Restrições
prob += 600 * x + 800 * y <= 480000  # Capacidade proporcional
prob += x <= 550  # Demanda máxima de chapas
prob += y <= 580  # Demanda máxima de barras

# Resolver o problema
prob.solve()

# Resultados
print(f"Status: {LpStatus[prob.status]}")
print(f"Chapas produzidas por dia: {value(x)}")
print(f"Barras produzidas por dia: {value(y)}")
print(f"Lucro Total: ${value(prob.objective)}")

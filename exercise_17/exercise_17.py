from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpStatus, value

# Criação do problema de otimização
prob = LpProblem("Maximizar_Lucro_Moveis", LpMaximize)

# Variáveis de decisão
x = LpVariable("Cadeiras", lowBound=0, cat="Integer")
y = LpVariable("Mesas", lowBound=0, cat="Integer")

# Função objetivo: maximizar o lucro
prob += 50 * x + 100 * y

# Restrições
# Departamento de Serraria
prob += x <= 200  # Máximo de cadeiras na serraria
prob += y <= 80   # Máximo de mesas na serraria

# Departamento de Montagem
prob += x <= 120  # Máximo de cadeiras na montagem
prob += y <= 60   # Máximo de mesas na montagem

# Departamento de Pintura (restrição ajustada)
prob += 110 * x + 150 * y <= 16500  # Capacidade combinada de pintura

# Resolver o problema
prob.solve()

# Resultados
print(f"Status: {LpStatus[prob.status]}")
print(f"Cadeiras produzidas por dia: {value(x)}")
print(f"Mesas produzidas por dia: {value(y)}")
print(f"Lucro Total: ${value(prob.objective)}")

from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpStatus, value

# Cria o problema
prob = LpProblem("Maximize_Profit", LpMaximize)

# Variáveis de decisão
x = LpVariable("Liga de Baixa", lowBound=0, cat="Integer")  # Cadeiras >= 0
y = LpVariable("Liga de Alta", lowBound=0, cat="Integer")


# Função objetivo: maximizar o lucro (40*x1 + 50*x2)
prob += 3000 * x + 5000 * y

# Restrições
prob += x * 0.5 + y * 0.2 <= 16
prob += x * 0.25 + y * 0.3 <= 11
prob += x * 0.25 + y * 0.5 <= 15
# Resolve o problema
prob.solve()

# Resultados
print(f"Status: {LpStatus[prob.status]}")
print(f"Liga de Baixa = {value(x)}")
print(f"Liga de Alta = {value(y)}")
print(f"Lucro Total: ${value(prob.objective)}")

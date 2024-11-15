from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpStatus, value

# Criação do problema de otimização
prob = LpProblem("Maximizar_Retorno_Investimento", LpMaximize)

# Variáveis de decisão: valores investidos em A e B
x_A = LpVariable("Investimento_A", lowBound=0, cat="Continuous")
x_B = LpVariable("Investimento_B", lowBound=0, cat="Continuous")

# Função objetivo: maximizar o retorno
prob += 0.05 * x_A + 0.08 * x_B  # Retorno total dos investimentos

# Restrições
prob += x_A + x_B == 5000  # O total de investimento deve ser 5000
prob += x_A >= 1250  # No mínimo 25% em A
prob += x_B <= 2500  # No máximo 50% em B
prob += x_A >= 0.5 * x_B  # A deve ser no mínimo metade de B

# Resolução do problema
prob.solve()

# Resultados
print(f"Status: {LpStatus[prob.status]}")
print(f"Investimento A: ${value(x_A):.2f}")
print(f"Investimento B: ${value(x_B):.2f}")
print(f"Retorno Total: ${value(prob.objective):.2f}")

from pulp import LpProblem, LpMaximize, LpVariable, LpStatus, value

# Criação do problema de otimização
prob = LpProblem("Maximizar_Lucro_Produção", LpMaximize)

# Variáveis de decisão: quantidade de A e B a ser produzida
x_A = LpVariable("Produto_A", lowBound=30, upBound=150, cat="Continuous")
x_B = LpVariable("Produto_B", lowBound=40, upBound=200, cat="Continuous")

# Função objetivo: maximizar o lucro
prob += 8 * x_A + 10 * x_B  # Lucro total da produção de A e B

# Restrições
prob += 0.5 * x_A + 0.5 * x_B <= 150  # Restrição de matéria-prima I
prob += 0.6 * x_A + 0.4 * x_B <= 145  # Restrição de matéria-prima II

# Resolução do problema
prob.solve()

# Resultados
print(f"Status: {LpStatus[prob.status]}")
print(f"Produto A (unidades): {value(x_A):.2f}")
print(f"Produto B (unidades): {value(x_B):.2f}")
print(f"Lucro Total: ${value(prob.objective):.2f}")

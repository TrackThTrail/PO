from pulp import LpProblem, LpMaximize, LpVariable, LpStatus, value

# Criação do problema de otimização
prob = LpProblem("Maximizar_Lucro_Armazém", LpMaximize)

# Variáveis de decisão: quantidade de Grano e Wheatie a ser colocada na prateleira
x_G = LpVariable("Grano", lowBound=0, upBound=200, cat="Continuous")
x_W = LpVariable("Wheatie", lowBound=0, upBound=120, cat="Continuous")

# Função objetivo: maximizar o lucro
prob += 1 * x_G + 1.35 * x_W  # Lucro total da venda de Grano e Wheatie

# Restrições
prob += 0.2 * x_G + 0.4 * x_W <= 60  # Restrição de espaço de prateleira
prob += x_G <= 200  # Restrição de demanda máxima para Grano
prob += x_W <= 120  # Restrição de demanda máxima para Wheatie

# Restrição de alocação de espaço para Wheatie ser 35% maior que para Grano
prob += x_W == 0.675 * x_G  # Proporção do espaço destinado ao Wheatie

# Resolução do problema
prob.solve()

# Resultados
print(f"Status: {LpStatus[prob.status]}")
print(f"Caixas de Grano: {value(x_G):.2f}")
print(f"Caixas de Wheatie: {value(x_W):.2f}")
print(f"Lucro Total: ${value(prob.objective):.2f}")

from pulp import LpProblem, LpMaximize, LpVariable, LpStatus, value

# Criação do problema de otimização
prob = LpProblem("Maximizar_Lucro_Chapeus", LpMaximize)

# Variáveis de decisão: número de chapéus do tipo 1 e tipo 2
x_1 = LpVariable("Chapeus_Tipo_1", lowBound=0, cat="Continuous")
x_2 = LpVariable("Chapeus_Tipo_2", lowBound=0, cat="Continuous")

# Função objetivo: maximizar o lucro
prob += 8 * x_1 + 5 * x_2  # 8 * x_1 é o lucro do tipo 1 e 5 * x_2 é o lucro do tipo 2

# Restrições
prob += 2 * x_1 + x_2 <= 400  # Restrição de tempo de trabalho total
prob += x_1 <= 150  # Limite do mercado para o tipo 1
prob += x_2 <= 200  # Limite do mercado para o tipo 2

# Resolução do problema
prob.solve()

# Resultados
print(f"Status: {LpStatus[prob.status]}")
print(f"Chapéus do Tipo 1 (x_1): {value(x_1):.2f} unidades")
print(f"Chapéus do Tipo 2 (x_2): {value(x_2):.2f} unidades")
print(f"Lucro Total: {value(prob.objective):.2f} dólares")

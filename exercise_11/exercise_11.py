from pulp import LpProblem, LpMaximize, LpVariable, LpStatus, value

# Criação do problema de otimização
prob = LpProblem("Maximizar_Prazer", LpMaximize)

# Variáveis de decisão: número de horas de estudo e diversão
x_S = LpVariable("Estudo", lowBound=0, cat="Continuous")
x_D = LpVariable("Diversao", lowBound=0, cat="Continuous")

# Função objetivo: maximizar o prazer
prob += 2 * x_D + x_S  # 2 * x_D é o prazer de se divertir e x_S é o prazer de estudar

# Restrições
prob += x_S + x_D <= 10  # O tempo total não pode ultrapassar 10 horas
prob += x_D <= 4  # O tempo de diversão não pode ultrapassar 4 horas
prob += x_S >= x_D  # O tempo de estudo deve ser pelo menos o mesmo que o de diversão

# Resolução do problema
prob.solve()

# Resultados
print(f"Status: {LpStatus[prob.status]}")
print(f"Tempo de Estudo (x_S): {value(x_S):.2f} horas")
print(f"Tempo de Diversão (x_D): {value(x_D):.2f} horas")
print(f"Prazer Total: {value(prob.objective):.2f}")

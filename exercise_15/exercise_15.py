from pulp import LpProblem, LpMaximize, LpVariable, LpStatus, value

# Criação do problema de otimização
prob = LpProblem("Maximizar_Alcance_Campanha", LpMaximize)

# Variáveis de decisão: número de comerciais de rádio e anúncios de TV
x_1 = LpVariable("Comerciais_Radio", lowBound=1, cat="Integer")
x_2 = LpVariable("Anuncios_TV", lowBound=1, cat="Integer")

# Função objetivo: maximizar o alcance
prob += 7000 + 2000 * x_1 + 3000 * x_2  # Alcance total

# Restrições
prob += 300 * x_1 + 2000 * x_2 <= 20000  # Restrição de orçamento total
prob += 300 * x_1 <= 16000  # Limite de verba para rádio
prob += 2000 * x_2 <= 16000  # Limite de verba para TV

# Resolução do problema
prob.solve()

# Resultados
print(f"Status: {LpStatus[prob.status]}")
print(f"Comerciais de Rádio (x_1): {value(x_1)} unidades")
print(f"Anúncios de TV (x_2): {value(x_2)} unidades")
print(f"Alcance Total: {value(prob.objective)} pessoas")

import pulp

# Criação do problema de otimização
prob = pulp.LpProblem("Minimizar_Ociosidade", pulp.LpMinimize)

# Variáveis de decisão
x1 = pulp.LpVariable("x1", lowBound=0, cat="Continuous")  # Número de unidades do modelo HiFi-1
x2 = pulp.LpVariable("x2", lowBound=0, cat="Continuous")  # Número de unidades do modelo HiFi-2

# Função objetivo: Minimizar as horas ociosas nas estações de trabalho
prob += (480 - (6 * x1 + 4 * x2)) * 0.10 + (480 - (5 * x1 + 5 * x2)) * 0.14 + (480 - (4 * x1 + 6 * x2)) * 0.12, "Ociosidade Total"

# Restrições de tempo por estação
prob += 6 * x1 + 4 * x2 <= 432, "Restrição Estação 1"
prob += 5 * x1 + 5 * x2 <= 412.8, "Restrição Estação 2"
prob += 4 * x1 + 6 * x2 <= 422.4, "Restrição Estação 3"

# Restrições de não-negatividade (já garantidas com as variáveis de decisão)
# x1 >= 0
# x2 >= 0

# Resolver o problema
prob.solve()

# Exibir resultados
print("Status:", pulp.LpStatus[prob.status])
print("Número de unidades do modelo HiFi-1 (x1):", pulp.value(x1))
print("Número de unidades do modelo HiFi-2 (x2):", pulp.value(x2))
print("Horas Ociosas Totais:", pulp.value(prob.objective))

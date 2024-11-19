from pulp import LpMaximize, LpProblem, LpVariable

# Criação do problema
problem = LpProblem("Pedido_de_Socorro", LpMaximize)

# Variáveis de decisão
x1 = LpVariable("Caixas_Alimento", lowBound=0, cat="Integer")  # Quantidade de caixas de alimentos
x2 = LpVariable("Caixas_Agua", lowBound=0, cat="Integer")      # Quantidade de caixas de água
x3 = LpVariable("Caixas_Municao", lowBound=0, cat="Integer")   # Quantidade de caixas de munição
x4 = LpVariable("Caixas_Remedios", lowBound=0, cat="Integer")  # Quantidade de caixas de remédios

# Função objetivo
problem += 1 * x1 + 2 * x2 + 4 * x3 + 4 * x4, "Importancia_Total"

# Restrições
problem += x1 + x2 + x3 + x4 <= 7, "Restricao_Capacidade_Helicoptero"
problem += x1 >= 6, "Restricao_Alimentos"
problem += x2 >= 4, "Restricao_Agua"
problem += x3 >= 2, "Restricao_Municao"
problem += x4 >= 2, "Restricao_Remedios"

# Resolução do problema
problem.solve()

# Resultados
print("Status:", problem.status)
print("Solução Ótima:")
print(f"Caixas de Alimentos (x1): {x1.varValue}")
print(f"Caixas de Água (x2): {x2.varValue}")
print(f"Caixas de Munição (x3): {x3.varValue}")
print(f"Caixas de Remédios (x4): {x4.varValue}")
print(f"Importância Total: {problem.objective.value()}")

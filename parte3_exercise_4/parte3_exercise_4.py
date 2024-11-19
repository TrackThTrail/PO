from pulp import LpMaximize, LpProblem, LpVariable

# Criação do problema
problem = LpProblem("Refinaria", LpMaximize)

# Variáveis de decisão
x1 = LpVariable("Pinus", lowBound=0, cat="Continuous")  # Quantidade de Pinus
x2 = LpVariable("Carvalho", lowBound=0, cat="Continuous")  # Quantidade de Carvalho
x3 = LpVariable("Nogueira", lowBound=0, cat="Continuous")  # Quantidade de Nogueira
x4 = LpVariable("Araucaria", lowBound=0, cat="Continuous")  # Quantidade de Araucária

# Renda por cidade
renda_cidade_1 = x1 * 16 + x2 * 12 + x3 * 20 + x4 * 18
renda_cidade_2 = x1 * 14 + x2 * 13 + x3 * 24 + x4 * 20
renda_cidade_3 = x1 * 17 + x2 * 10 + x3 * 28 + x4 * 20
renda_cidade_4 = x1 * 12 + x2 * 11 + x3 * 18 + x4 * 17

# Função objetivo: maximizar o lucro total
problem += renda_cidade_1 + renda_cidade_2 + renda_cidade_3 + renda_cidade_4, "Lucro_Total"

# Restrições de área disponível por cidade
problem += x1 * 17 + x2 * 14 + x3 * 10 + x4 * 9 <= 1500, "Restricao_Cidade_1"
problem += x1 * 15 + x2 * 16 + x3 * 12 + x4 * 11 <= 1700, "Restricao_Cidade_2"
problem += x1 * 13 + x2 * 12 + x3 * 14 + x4 * 8 <= 900, "Restricao_Cidade_3"
problem += x1 * 10 + x2 * 11 + x3 * 8 + x4 * 6 <= 600, "Restricao_Cidade_4"

# Restrições de produção mínima por espécie
problem += x1 >= 225, "Producao_Minima_Pinus"
problem += x2 >= 9, "Producao_Minima_Carvalho"
problem += x3 >= 4.8, "Producao_Minima_Nogueira"
problem += x4 >= 3.5, "Producao_Minima_Araucaria"

# Resolução do problema
problem.solve()

# Resultados
print("Status:", problem.status)
print("Solução Ótima:")
print(f"Pinus (x1): {x1.varValue}")
print(f"Carvalho (x2): {x2.varValue}")
print(f"Nogueira (x3): {x3.varValue}")
print(f"Araucaria (x4): {x4.varValue}")
print(f"Lucro Total: {problem.objective.value()}")

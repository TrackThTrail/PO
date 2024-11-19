from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable

# Criação dos problemas
work = LpProblem("Mao_de_obra", LpMinimize)
problem = LpProblem("Hospital", LpMaximize)
leitos = LpProblem("Leitos", LpMaximize)
space = LpProblem("Space", LpMinimize)

# Variáveis de decisão
x1 = LpVariable("1Leito", lowBound=0, cat="Continuous")
x2 = LpVariable("2Leito", lowBound=0, cat="Continuous")
x3 = LpVariable("3Leito", lowBound=0, cat="Continuous")

# Função objetivo: minimizar mao de obra
work += x1 * 1 + x2 * 0.8 + x3 * 0.8, "Mao_de_obra_Total"
work += x1 + x2 + x3 <= 70, "Restricao_Quartos"
work += x1 * 1 + x2 * 2 + x3 * 3 >= 120, "Restricao_Leitos"
work += x1 <= 0.3 * (x1 + x2 + x3), "Restricao_1Leito_Max"
work += x1 >= 0.15 * (x1 + x2 + x3), "Restricao_1Leito_Min"

# Função objetivo: maximizar arrecadacao global
problem += x1 + (1 / 2) * x2 + (1 / 3) * x3, "Arrecadacao_Global"
problem += x1 + x2 + x3 <= 70, "Restricao_Quartos"
problem += x1 * 1 + x2 * 2 + x3 * 3 >= 120, "Restricao_Leitos"
problem += x1 <= 0.3 * (x1 + x2 + x3), "Restricao_1Leito_Max"
problem += x1 >= 0.15 * (x1 + x2 + x3), "Restricao_1Leito_Min"

# Função objetivo: maximizar numero de leitos
leitos += x1 * 1 + x2 * 2 + x3 * 3, "Numero_Leitos"
leitos += x1 + x2 + x3 <= 70, "Restricao_Quartos"
leitos += x1 * 1 + x2 * 2 + x3 * 3 >= 120, "Restricao_Leitos"
leitos += x1 <= 0.3 * (x1 + x2 + x3), "Restricao_1Leito_Max"
leitos += x1 >= 0.15 * (x1 + x2 + x3), "Restricao_1Leito_Min"

# Função objetivo: minimizar espaco ocupado
space += x1 * 10 + x2 * 14 + x3 * 17, "Espaco_Total"
space += x1 + x2 + x3 <= 70, "Restricao_Quartos"
space += x1 * 1 + x2 * 2 + x3 * 3 >= 120, "Restricao_Leitos"
space += x1 <= 0.3 * (x1 + x2 + x3), "Restricao_1Leito_Max"
space += x1 >= 0.15 * (x1 + x2 + x3), "Restricao_1Leito_Min"

# Resolução dos problemas
work.solve()
problem.solve()
leitos.solve()
space.solve()

# Exibição dos resultados
def print_results(problem_name, problem):
    print(f"Resultados do problema: {problem_name}")
    print(f"Status: {problem.status}")
    print("Solução:")
    for var in problem.variables():
        print(f"{var.name}: {var.varValue}")
    print(f"Função objetivo ({problem_name}): {problem.objective.value()}\n")

# Resultados de cada problema
print_results("Mao de Obra", work)
print_results("Arrecadacao Global", problem)
print_results("Numero de Leitos", leitos)
print_results("Espaco Ocupado", space)

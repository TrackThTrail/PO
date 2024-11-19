from pulp import LpMaximize, LpProblem, LpVariable

# Criar o modelo de otimização
model = LpProblem(name="maximizar-lucro", sense=LpMaximize)

# Variáveis de decisão
x1 = LpVariable(name="lotes_calcas", lowBound=0, cat="Continuous")  # Lotes de calças
x2 = LpVariable(name="lotes_camisas", lowBound=0, cat="Continuous")  # Lotes de camisas

# Função objetivo
model += 500 * x1 + 800 * x2, "Lucro_Total"

# Restrições
model += 10 * x1 + 20 * x2 <= 50, "Mao_Obra_Nao_Especializada"
model += 10 * x2 <= 30, "Mao_Obra_Especializada"
model += 20 * x1 + 10 * x2 <= 80, "Capacidade_Maquina_1"
model += 30 * x1 + 35 * x2 <= 130, "Capacidade_Maquina_2"
model += 12 * x1 + 8 * x2 <= 120, "Materia_Prima_A"
model += 10 * x1 + 15 * x2 <= 100, "Materia_Prima_B"

# Resolver o problema
status = model.solve()

# Resultados
print(f"Status da solução: {model.status}")
print(f"Lucro máximo: R$ {model.objective.value():,.2f}")
print(f"Lotes de calças a produzir: {x1.value():,.2f}")
print(f"Lotes de camisas a produzir: {x2.value():,.2f}")

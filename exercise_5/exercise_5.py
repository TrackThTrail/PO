from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpStatus, value

# Criação do problema de otimização
prob = LpProblem("Maximizar_Lucro_Produtos", LpMaximize)

# Variáveis de decisão
x = LpVariable("Produto_A", lowBound=0, cat="Integer")
y = LpVariable("Produto_B", lowBound=0, cat="Integer")

# Função objetivo: maximizar o lucro
prob += 20 * x + 50 * y

# Restrições
prob += x >= 4 * y  # Volume mínimo de vendas de A
prob += x <= 100    # Limite máximo de vendas de A
prob += 2 * x + 4 * y <= 240  # Disponibilidade de matéria-prima

# Resolver o problema
prob.solve()

# Resultados
print(f"Status: {LpStatus[prob.status]}")
print(f"Unidades do Produto A: {value(x)}")
print(f"Unidades do Produto B: {value(y)}")
print(f"Lucro Total: ${value(prob.objective)}")

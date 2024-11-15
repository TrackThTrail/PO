from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpStatus, value

# Criação do problema de otimização
prob = LpProblem("Maximizar_Lucro_Gasolina", LpMaximize)

# Variáveis de decisão para a quantidade de gasolina produzida
g_sa = LpVariable("Gasolina_SuperAzul", lowBound=0, cat="Continuous")
g_a = LpVariable("Gasolina_Azul", lowBound=0, cat="Continuous")
g_am = LpVariable("Gasolina_Amarela", lowBound=0, cat="Continuous")

# Variáveis de fração dos tipos de petróleo em cada gasolina
p1_sa = LpVariable("Petroleo1_SuperAzul", lowBound=0)
p2_sa = LpVariable("Petroleo2_SuperAzul", lowBound=0)
p3_sa = LpVariable("Petroleo3_SuperAzul", lowBound=0)

p1_a = LpVariable("Petroleo1_Azul", lowBound=0)
p2_a = LpVariable("Petroleo2_Azul", lowBound=0)

p1_am = LpVariable("Petroleo1_Amarela", lowBound=0)

# Função objetivo: maximizar o lucro (receita - custo)
prob += (
    35 * g_sa + 28 * g_a + 22 * g_am  # Receita
    - (19 * (p1_sa + p1_a + p1_am) + 24 * (p2_sa + p2_a) + 20 * p3_sa)  # Custos de petróleo
)

# Restrições de disponibilidade máxima de cada tipo de petróleo
prob += p1_sa + p1_a + p1_am <= 3500  # Limite para o petróleo 1
prob += p2_sa + p2_a <= 2200  # Limite para o petróleo 2
prob += p3_sa <= 4200  # Limite para o petróleo 3

# Restrições de composição para cada gasolina
# SuperAzul
prob += p1_sa <= 0.3 * g_sa
prob += p2_sa >= 0.4 * g_sa
prob += p3_sa <= 0.5 * g_sa

# Azul
prob += p1_a <= 0.3 * g_a
prob += p2_a >= 0.1 * g_a

# Amarela
prob += p1_am <= 0.7 * g_am

# Resolução do problema
prob.solve()

# Resultados
print(f"Status: {LpStatus[prob.status]}")
print(f"Gasolina SuperAzul: {value(g_sa)} barris")
print(f"Gasolina Azul: {value(g_a)} barris")
print(f"Gasolina Amarela: {value(g_am)} barris")
print(f"Lucro Total: ${value(prob.objective)}")

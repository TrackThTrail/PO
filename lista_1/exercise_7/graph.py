import numpy as np
import matplotlib.pyplot as plt

# Definindo o intervalo de valores para x_A e x_B
x_A_values = np.linspace(0, 5000, 400)

# Restrição 1: x_A + x_B = 5000
# x_B = 5000 - x_A
x_B1_values = 5000 - x_A_values

# Restrição 2: x_A >= 1250
# Essa restrição é uma linha vertical em x_A = 1250
x_A2 = 1250

# Restrição 3: x_B <= 2500
# Essa restrição é uma linha horizontal em x_B = 2500
x_B3 = 2500

# Restrição 4: x_A >= 0.5 * x_B
# x_A >= 0.5 * x_B -> x_A >= 0.5 * x_B
x_B4_values = 2 * x_A_values  # Rearranjando a equação para x_B = 2 * x_A

# Plotando as restrições
plt.figure(figsize=(8, 8))

# Gráfico da restrição x_A + x_B = 5000
plt.plot(x_A_values, x_B1_values, label=r'$x_A + x_B = 5000$', color='blue')

# Gráfico da restrição x_A >= 1250
plt.axvline(x_A2, color='green', linestyle='--', label=r'$x_A \geq 1250$')

# Gráfico da restrição x_B <= 2500
plt.axhline(x_B3, color='red', linestyle='--', label=r'$x_B \leq 2500$')

# Gráfico da restrição x_A >= 0.5 * x_B
plt.plot(x_A_values, x_B4_values, label=r'$x_A \geq 0.5 \times x_B$', color='orange')

# Definindo limites do gráfico
plt.xlim(0, 5000)
plt.ylim(0, 5000)

# Adicionando rótulos e título
plt.xlabel(r'$x_A$', fontsize=12)
plt.ylabel(r'$x_B$', fontsize=12)
plt.title('Região Viável para o Problema de Investimento', fontsize=14)

# Adicionando a legenda
plt.legend()

# Exibindo o gráfico
plt.grid(True)
plt.show()

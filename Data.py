import numpy as np
import matplotlib.pyplot as plt

diametro = np.loadtxt('citrus.csv',delimiter=',',skiprows=1, usecols=np.arange(1, 2))
peso = np.loadtxt('citrus.csv',delimiter=',',skiprows=1, usecols=np.arange(2, 3))
diametro_laranja = diametro[:5000]
peso_laranja = peso[:5000]
diametro_toranja = diametro[5000:]
peso_toranja = peso[5000:]

plt.scatter(diametro_laranja, peso_laranja, color="orange", label="Laranja")
plt.scatter(diametro_toranja, peso_toranja, color="red", label="Toranja")

plt.title("Laranja e Toranja")
plt.xlabel("Diâmetro (cm)")
plt.ylabel("Peso (g)")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
from Lectura_Validación import df_pokemon
import seaborn as sns
import matplotlib.pyplot as plt

'''
--- Ejercicio 4 ---
4. Visualización de datos
-------------------------
- Haz un histograma de los valores de ataque.
- Realiza un gráfico de dispersión entre ataque y velocidad.
- Haz un boxplot de los PS por tipo principal (Tipo 1).
- Grafica la distribución de la defensa usando un diagrama de violín.
'''

# Histograma de ataque
sns.histplot(df_pokemon["Ataque"])
plt.title("Histograma de ataque")
plt.xlabel("Ataque")
plt.ylabel("Cantidad de Pokemon")
plt.show()

# Gráfico de dispersión: Ataque vs Velocidad
sns.scatterplot(x="Ataque", y="Velocidad", data=df_pokemon, hue="Tipo 1")
plt.title("Dispersión: Ataque vs Velocidad")
plt.show()

# Boxplot de PS por Tipo 1
sns.boxplot(x="Tipo 1", y="PS", data=df_pokemon)
plt.title("Boxplot de PS por Tipo 1")
plt.show()

# Diagrama de violín de Defensa por Tipo 1
sns.violinplot(x="Tipo 1", y="Defensa", data=df_pokemon)
plt.title("Distribución de la Defensa por Tipo 1")
plt.show()
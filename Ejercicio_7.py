from Lectura_Validación import df_pokemon
import seaborn as sns
import matplotlib.pyplot as plt

'''
--- Ejercicio 7 ---
7. Análisis exploratorio (EDA)
------------------------------
- ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa? Justifica
con estadísticas.
- ¿Hay correlación entre ataque y velocidad? Calcula el coeficiente de correlación.
- ¿Qué tan dispersos están los PS dentro de cada tipo? (compara la desviación
estándar de PS por tipo)
- Identifica posibles outliers en los valores de ataque y PS usando boxplots.
'''

ataque_defensa = df_pokemon.groupby("Tipo 1")[["Ataque", "Defensa"]]
ataque_defensa = ataque_defensa.mean()
ataque_defensa = ataque_defensa.reset_index()
ataque_defensa_melt = ataque_defensa.melt(id_vars="Tipo 1", value_vars=["Ataque", "Defensa"], var_name="Atributos", value_name="Valor")
sns.barplot(data=ataque_defensa_melt, x="Tipo 1", y="Valor", hue="Atributos")
plt.title("Ataque y defensa promedio por tipo")
plt.show()
print("1) Como podemos ver en la imagen anterior, los Pokemon tipo Lucha son los que tienden a tener un mayor Ataque, siguiéndoles los del tipo dragón.")
print("Mientras que en defensa, son los Pokemon tipo Roca los que más destacan, seguidos de los tipo Tierra.")

correlacion = df_pokemon["Ataque"].corr(df_pokemon["Velocidad"])
print("\n2) El coeficiente de correlación entre ataque y velocidad es de: ", round(correlacion, 2))
print("El coeficiente de correlación es muy débil, es decir, no hay mucha relación lineal entre ambos atributos.")
print("El coeficente de correlación es positivo, por lo que las variables tienden a moverse en la misma dirección.")

dispersion_ps = df_pokemon.groupby("Tipo 1")["PS"].std()
dispersion_ps = dispersion_ps.sort_values(ascending=True).reset_index()
dispersion_ps.columns = ["Tipo 1", "Desviación PS"]
print("\n3) La desviación estándar de PS por cada tipo de Pokemon es:\n", round(dispersion_ps, 2))
print("Como observamos en la tabla anterior, el tipo de Pokemon Bicho es el que menos dispersión tiene, lo que quiere decir que sus PS son más homogéneos.")

sns.boxplot(x=df_pokemon["Ataque"], color="red")
plt.title("Boxplot de ataque (detección de outliers)")
plt.show()
sns.boxplot(x=df_pokemon["PS"], color="blue")
plt.title("Boxplot de PS (detección de outliers)")
plt.show()
print("\n4) Como podemos ver en los gráficos, el boxplot de ataque no muestra outliers, en cambio el boxplot de PS si muestra a tres outliers, los cuales son:")
Q1 = df_pokemon["PS"].quantile(0.25)
Q3 = df_pokemon["PS"].quantile(0.75)
IQR = Q3 - Q1
outliers_ps = df_pokemon[(df_pokemon["PS"] < Q1 - 1.5*IQR) | (df_pokemon["PS"] > Q3 + 1.5*IQR)].reset_index()
print(outliers_ps[["Nombre", "PS"]])
print("Esto significa que estos tres Pokemon podrían incidir negativamente al hacer mediciones de los datos al tener valores muy altos, sesgando las mediciones y llevando a errores.")
from Lectura_Validación import df_pokemon

'''
--- Ejercicio 6 ---
6. Agrupamiento y análisis por grupo
-------------------------------------
- Calcula el promedio, la mediana y la desviación estándar de ataque por cada tipo
principal (Tipo 1).
- ¿Qué tipo tiene el mayor promedio de velocidad?
- Para cada tipo principal, ¿cuál es el Pokémon con mayor y menor PS?
'''

ataque_tipo = df_pokemon.groupby("Tipo 1")["Ataque"]
ataque_tipo = ataque_tipo.agg(["mean", "median", "std"])
print("El promedio, la mediana y la desviación estándar de ataque por cada tipo principal es:\n", round(ataque_tipo, 2))

velocidad_tipo = df_pokemon.groupby("Tipo 1")["Velocidad"]
velocidad_tipo = velocidad_tipo.mean()
tipo_mas_rapido = velocidad_tipo.idxmax()
puntaje_max = velocidad_tipo.max()
print("\nEl tipo que tiene mayor promedio de velocidad es: ", tipo_mas_rapido, ", con un puntaje de: ", round(puntaje_max, 2))

ps_max = df_pokemon.loc[df_pokemon.groupby("Tipo 1")["PS"].idxmax(), ["Tipo 1", "Nombre", "PS"]].reset_index(drop=True)
ps_min = df_pokemon.loc[df_pokemon.groupby("Tipo 1")["PS"].idxmin(), ["Tipo 1", "Nombre", "PS"]].reset_index(drop=True)
print("\nPokemon con mayor PS por tipo:\n", ps_max)
print("\nPokemon con menor PS por tipo:\n", ps_min)
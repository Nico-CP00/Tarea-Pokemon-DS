from Lectura_Validación import df_pokemon

'''
--- Ejercicio 5 ---
5. Manipulación de datos
------------------------
- Crea una nueva columna llamada "Poder Total" que sea la suma de ataque, defensa,
velocidad y PS.
- Ordena el DataFrame por "Poder Total" de mayor a menor.
'''

df_pokemon["Poder Total"] = df_pokemon["Ataque"] + df_pokemon["Defensa"] + df_pokemon["Velocidad"] + df_pokemon["PS"]

df_ordenado = df_pokemon.sort_values(by="Poder Total", ascending=False).reset_index()

print("Lista de Pokemon por Poder Total ordenado de mayor a menor\n", df_ordenado)
print("Top 10 de mejores Pokemon\n", df_ordenado[["Nombre", "Poder Total"]].head(10))
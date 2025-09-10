from Lectura_Validación import df_pokemon

'''
--- Ejercicio 2 ---
2. Filtrado y selección
-----------------------
- Filtra todos los Pokémon de tipo "Fuego".
- Selecciona solo las columnas Nombre, Tipo 1, Ataque y Velocidad.
'''

fuego = df_pokemon[(df_pokemon["Tipo 1"] == "Fuego")]
tipo_fuego = fuego[["Nombre", "Tipo 1", "Ataque", "Velocidad"]]
print(tipo_fuego)
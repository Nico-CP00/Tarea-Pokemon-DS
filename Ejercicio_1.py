from Lectura_Archivo import df_pokemon

# ---Ejercicio 2---

fuego = df_pokemon[(df_pokemon["Tipo 1"] == "Fuego") | (df_pokemon["Tipo 2"] == "Fuego")]
tipo_fuego = fuego[["Nombre", "Tipo 1", "Tipo 2", "Ataque", "Defensa", "Velocidad", "PS"]]
print(tipo_fuego)
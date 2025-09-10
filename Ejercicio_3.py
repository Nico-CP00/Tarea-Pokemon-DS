from Lectura_Validación import df_pokemon

'''
--- Ejercicio 3 ---
3. Estadística descriptiva básica
---------------------------------
- Calcula el promedio, la mediana y la moda del ataque de todos los Pokémon.
- ¿Cuál es el Pokémon con mayor defensa? ¿Y el de menor velocidad?
- ¿Cuántos Pokémon tienen dos tipos?
- Calcula el rango y la desviación estándar de los PS (Puntos de Salud).
'''

promedio_ataque = round(df_pokemon["Ataque"].mean(), 2)
mediana_ataque = df_pokemon["Ataque"].median()
moda_ataque = df_pokemon["Ataque"].mode()
# Convertimos las modas en una lista para que se vea mejor
moda_ataque_lista = moda_ataque.tolist()

mayor_def = df_pokemon.loc[df_pokemon["Defensa"].idxmax()]
menor_vel = df_pokemon.loc[df_pokemon["Velocidad"].idxmin()]
nombre_mayor_def = mayor_def["Nombre"]
nombre_menor_vel = menor_vel["Nombre"]
dato_mayor_def = mayor_def["Defensa"]
dato_menor_vel = menor_vel["Velocidad"]

dos_tipos = df_pokemon["Tipo 2"].notna().sum()

rango_ps = df_pokemon["PS"].max() - df_pokemon["PS"].min()
desviacion_ps = round(df_pokemon["PS"].std(), 2)

print("Promedio de ataque de los Pokemon: ", promedio_ataque)
print("Mediana de ataque de los Pokemon: ", mediana_ataque)
print("Moda(s) de ataque de los Pokemon: ", moda_ataque_lista)
print("El Pokemon con mayor defensa es: ", nombre_mayor_def, ", con una defensa de: ", dato_mayor_def)
print("El Pokemon con menor velocidad es: ", nombre_menor_vel, ", con una velocidad de: ", dato_menor_vel)
print("La cantidad de Pokemon con dos tipos es de: ", dos_tipos)
print("El rango de los PS de los Pokemon es de: ", rango_ps)
print("La desviación estándar de los PS de los Pokemon es de: ", desviacion_ps)
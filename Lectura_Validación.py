import pandas as pd

# ---Ejercicio 1---
df_pokemon = pd.read_csv("pokemon_primera_gen.csv")

# Usamos un csv de Internet para comparar los datos de los Pokemon y verificar que estén correctos
df_pokemon_verificacion = pd.read_csv("FirstGenPokemon.csv")
df_pokemon_verificacion = df_pokemon_verificacion[[" Name", " Type1", " Type2", " HP", " Attack", " Defense", " Speed"]]
df_pokemon_verificacion = df_pokemon_verificacion.rename(columns={" Name": "Nombre", " Type1": "Tipo 1", " Type2": "Tipo 2",
" Speed": "Velocidad", " Attack": "Ataque", " Defense": "Defensa", " HP": "PS"})
df_pokemon_verificacion = df_pokemon_verificacion[["Nombre", "Tipo 1", "Tipo 2", "Ataque", "Defensa", "Velocidad", "PS"]]

#Traducimos los tipos
traduccion_tipos = {
    "grass": "Planta",
    "fire": "Fuego",
    "water": "Agua",
    "electric": "Eléctrico",
    "psychic": "Psiquico",
    "ice": "Hielo",
    "dragon": "Dragón",
    "dark": "Siniestro",
    "fairy": "Hada",
    "normal": "Normal",
    "fighting": "Lucha",
    "flying": "Volador",
    "poison": "Veneno",
    "ground": "Tierra",
    "rock": "Roca",
    "bug": "Bicho",
    "ghost": "Fantasma",
    "steel": "Acero"
}
df_pokemon_verificacion["Tipo 1"] = df_pokemon_verificacion["Tipo 1"].replace(traduccion_tipos)
df_pokemon_verificacion["Tipo 2"] = df_pokemon_verificacion["Tipo 2"].replace(traduccion_tipos)

# Aquí podemos comparar ambos DF y ver las diferencias entre ambos csv
# Usamos el if para que solo se ejecute si compilamos este archivo
if __name__ == "__main__":
    diferencias = df_pokemon.compare(df_pokemon_verificacion)
    print(diferencias)

# Aquí excluimos la variable "Nombre", ya que están mejor en el csv original y actualizamos el csv original
columnas_actualizar = ["Tipo 1", "Tipo 2", "Ataque", "Defensa", "Velocidad", "PS"]
df_pokemon[columnas_actualizar] = df_pokemon_verificacion[columnas_actualizar]


"""
Ejercicios de Análisis de Datos con Pokémon (Primera Generación)
===============================================================
Archivo de datos: pokemon_primera_gen.csv
---
1. Lectura de datos
-------------------
- Carga el archivo pokemon_primera_gen.csv en un DataFrame de Pandas.
2. Filtrado y selección
-----------------------
- Filtra todos los Pokémon de tipo "Fuego".
- Selecciona solo las columnas Nombre, Tipo 1, Ataque y Velocidad.
3. Estadística descriptiva básica
---------------------------------
- Calcula el promedio, la mediana y la moda del ataque de todos los Pokémon.
- ¿Cuál es el Pokémon con mayor defensa? ¿Y el de menor velocidad?
- ¿Cuántos Pokémon tienen dos tipos?
- Calcula el rango y la desviación estándar de los PS (Puntos de Salud).
4. Visualización de datos
-------------------------
- Haz un histograma de los valores de ataque.
- Realiza un gráfico de dispersión entre ataque y velocidad.
- Haz un boxplot de los PS por tipo principal (Tipo 1).
- Grafica la distribución de la defensa usando un diagrama de violín.
5. Manipulación de datos
------------------------
- Crea una nueva columna llamada "Poder Total" que sea la suma de ataque, defensa,
velocidad y PS.
- Ordena el DataFrame por "Poder Total" de mayor a menor.
6. Agrupamiento y análisis por grupo
-------------------------------------
- Calcula el promedio, la mediana y la desviación estándar de ataque por cada tipo
principal (Tipo 1).
- ¿Qué tipo tiene el mayor promedio de velocidad?
- Para cada tipo principal, ¿cuál es el Pokémon con mayor y menor PS?
7. Análisis exploratorio (EDA)
------------------------------
- ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa? Justifica
con estadísticas.
- ¿Hay correlación entre ataque y velocidad? Calcula el coeficiente de correlación.
- ¿Qué tan dispersos están los PS dentro de cada tipo? (compara la desviación
estándar de PS por tipo)
- Identifica posibles outliers en los valores de ataque y PS usando boxplots.
8. Ejercicios de interpretación
-------------------------------
- Interpreta los resultados de los gráficos y estadísticas: ¿qué conclusiones
puedes sacar sobre los Pokémon de la primera generación?
- ¿Qué tipo de Pokémon sería "más balanceado" según las estadísticas? ¿Y el más
especializado?
---
Recuerda usar las funciones de Pandas como mean(), median(), mode(), std(),
describe(), groupby(), así como las funciones de visualización de Matplotlib y
Seaborn vistas en la Semana 3.
"""
from Lectura_Validación import df_pokemon

'''
--- Ejercicio 8 ---
8. Ejercicios de interpretación
-------------------------------
- Interpreta los resultados de los gráficos y estadísticas: ¿qué conclusiones
puedes sacar sobre los Pokémon de la primera generación?
- ¿Qué tipo de Pokémon sería "más balanceado" según las estadísticas? ¿Y el más
especializado?
'''

print("1) Como conclusiones importantes con los datos obtenidos podemos destacar que: en mayoría, los Pokemon están muy balanceados en general,")
print("ya que no hay ningún tipo que tenga un desempeño demasiado superior a los demás, si bien hay ciertos tipos con algunos atributos más altos")
print("en promedio, son muy equilibrados en general. También podemos identificar a algunos outliers, pero son muy pocos, en los datos estudiados")
print("sólo identificamos a 3 de los 151. Se puede destacar también que hay sólo 62 Pokemon de dos tipos de los 151, siendo un poco más de un tercio")
print("del total, siendo estos muy codiciados por su combinación de tipos. Hay sólo 3 Pokemon con un poder total superior a 400, los cuales son Mewtwo,")
print("Dragonite y Mew, los siguen de cerca Cloyster y Rhydon con 395, luego se observa una gran caída en el poder total de los siguientes, de 15 puntos.")
print("Se puede destacar también que hay sólo 2 Pokemon de tipo Hielo como tipo principal, subiendo a 5 si sumamos los que tienen el tipo Hielo como")
print("tipo 2, siendo muy escasos en comparación con los demás. Por último, podemos destacar que el atributo ataque de todos los Pokemon es muy parecido,")
print("variando solo en algunos tipos de Pokemon pero siendo muy constante en los otros.\n")

print("2) Del ejercicio 7 podemos obtener datos que nos ayuden a determinar esto, podríamos empezar con los tipos, siendo Hielo el más homogéneo")
print("en cuanto a ataque y defensa, pero esto puede ser engañoso, ya que sólo hay dos Pokemon tipo Hielo como tipo principal: Jynx y Articuno.")
print("El segundo tipo de Pokemon más balanceado en este aspecto es el tipo Planta, seguido por el tipo Eléctrico. En el ejercicio 6 también podemos")
print("sacar más datos, como los de ataque, siendo los tipo Bicho, Fantasma y Planta los más homogéneos (con menos desviación estándar). Al repetirse")
print("dos veces los tipo Planta podemos fijarnos en estos, en el ejercicio 4 vemos que en los dos gráficos los tipo Planta son muy balanceados en")
print("cuanto a PS y Defensa. Con estos datos podemos decir que los Pokemon más balanceados son los de tipo Planta. En cuanto a los más especializados,")
print("podemos decir que los más especializados en PS son los de tipo Normal al tener más outliers, en defensa son los tipo Agua, al tener a Cloyster")
print("como el Pokemon con más defensa, en cuanto ataque los más especializados son los tipo Lucha y Dragón, y en cuanto a defensa son los tipo Roca.")
print("Los Pokemon de tipo Eléctrico están más especializados en velocidad.\n")

print("Para ambos casos se podrían sacar más datos para determinar mejor la respuesta, pero sólo estamos mirando los datos obtenidos hasta ahora.")
import numpy as np
# EJERCICIO 2

def cargarDatos(nomArchivo) :
  file = open(nomArchivo,"r")
  dic = {}
  file.readline()
  for linea in file : 
    info = linea.strip("\n").split("|")
    usuario = info[0]
    lista_peliculas = info[1:]
    dic[usuario] = dic.get(usuario,{"generos" : set() , "peliculas" : [] })
    for pelicula in lista_peliculas : 
      listainfopelicula = pelicula.split(";")
      nomPelicula = listainfopelicula[0]
      dic[usuario]["peliculas"].append(nomPelicula)
      listageneros = listainfopelicula[1:]
      for genero in listageneros : 
        dic[usuario]["generos"].add(genero)
  file.close()
  return dic

def perfectMatch(usuario,dic_gustos) :
  lista_personas = []
  for usuarioDic,dicInfo in dic_gustos.items() :
    if (usuarioDic != usuario) :
      if ( dic_gustos[usuario]["generos"] == dic_gustos[usuario]["generos"] & dicInfo["generos"] ) :
        lista_personas.append(usuarioDic)
  return lista_personas


#PROGRAMA PRINCIPAL

dic = cargarDatos("4 SEMANA/informacion.csv")
lista_personas = perfectMatch("Paul Alvarez",dic)

lista_peliculas_recomendadas = []
dicPeliculas = {}

for persona in lista_personas : 
  peliculas = dic[persona]["peliculas"]
  for pelicula in peliculas:
    if pelicula not in dic["Paul Alvarez"]["peliculas"] : 
      dicPeliculas[pelicula] = dicPeliculas.get(pelicula,0)
      dicPeliculas[pelicula]+=1

print(dicPeliculas)
l_peliculas,l_veces = list(dicPeliculas.keys()),list(dicPeliculas.values())

v_peliculas = np.array(l_peliculas)
v_veces = np.array(l_veces)

indices = np.argsort(v_veces)[::-1]

v_mas_vistas = v_peliculas[indices][:10]

print(list(v_mas_vistas))
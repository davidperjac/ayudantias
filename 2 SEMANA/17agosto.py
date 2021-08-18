import numpy as np

# EJERCICIO 1 examen I PAO 2018 - 2019 / ejercicio con diccionarios y matrices

dic = { 'Quito': {'robo vehiculo' : 540, 'asalto' : 4523, 'escandalo' : 24},
        'Guayaquil' : {'robo vehiculo' : 605, 'asalto' : 6345 , 'escandalo' : 5},
        'Cuenca' :  {'robo vehiculo' : 123, 'asalto' : 676, 'escandalo' : 133},
        'Machala' : {'robo vehiculo' : 67, 'asalto' : 1234, 'escandalo' : 412}
      }

#literal a 

#( () , ())
def ciudadesCrimines(dic) :
  
  ciudades = tuple(dic.keys())
  crimenes = tuple(dic[ciudades[0]].keys())
  
  resultado = (ciudades,crimenes)
  return resultado

#literal b

def crearMatriz(dic) :
  
  ciudades = list(dic.keys())
  crimenes = list(dic[ciudades[0]].keys())

  matriz = np.zeros((len(ciudades),len(crimenes)),int)

  contFilas = 0
  for ciudad,dicCrimenes in dic.items():
    contColumnas = 0
    for crimen,cantidad in dicCrimenes.items():
      matriz[contFilas,contColumnas] = cantidad
      contColumnas+=1
    contFilas+=1
  return matriz


import numpy as np

dicRegiones = { "LatinAmerica": { "Colombia": ["Bogota","Manizales","Medellin"],
                                  "Ecuador": ["Quito","Guayaquil"],
                                  "Peru" :["Lima"],
                                  "Bolivia" : ["La Paz"],
              }, 
              "NorteAmerica": {"USA" : ["Dallas","New York City"]} 
              }

def cargar_info (nom_file,mes) :
  file = open(nom_file,"r")
  file.readline()
  file.readline()
  #separacion por :
  nomVacunas = file.readline().split(":")[1].strip("\n").split(",")
  nomCiudades = file.readline().split(":")[1].strip("\n").split(",")
  file.readline()
  file.readline()
  file.readline()
  #separacion por ,
  poblacionC = file.readline().strip("\n").split(",")
  poblacion = []
  for ciudadC in poblacionC :
    c,p = ciudadC.split(":")
    poblacion.append(p)
  #separacion por ;
  file.readline()
  file.readline()
  file.readline()
  #creacion de matriz
  matriz = np.zeros((len(nomVacunas),len(nomCiudades)))
  for linea in file : 
    ciudad,fecha,vacunas = linea.strip("\n").split(";")
    if (int(fecha.split("-")[1][1]) == mes):
      ind_col = nomCiudades.index(ciudad)
      for vacunaD in vacunas.split("|"):
        vacuna,dosis = vacunaD.split(",") 
        ind_fil = nomVacunas.index(vacuna)
        matriz[ind_fil,ind_col] += int(dosis)
  return (np.array(poblacion),np.array(nomVacunas),np.array(nomCiudades),matriz )

def totalVacunados(nomArchivo,mesInicio,mesFin):
  #mayo 5 , #septiembre 9 = 9 - 5 = 4
  matriz = cargar_info(nomArchivo,mesInicio)[3]
  mesI = mesInicio
  for i in range((mesFin - mesI) +1):
    matriz += cargar_info(nomArchivo,mesI)[3]
    mesI+=1
  return matriz

def masVacunados(nomArchivo,mes,N):
  poblacion,nomVacunas,nomCiudades,matriz = cargar_info(nomArchivo,mes)
  
  masVacunados = []
  
  for vacuna in nomVacunas:
    ind = list(nomVacunas).index(vacuna)
    totalDosis = matriz[ind,:]
    indices = np.argsort(totalDosis)[::-1]
    mayores_ciudades = nomCiudades[indices][:N]
    masVacunados.append(mayores_ciudades)
  return tuple(masVacunados)

def region(dRegiones,vCiudades) :
  lista_salida = []
  for ciudad in vCiudades:
    for region,dicR in dRegiones.items():
      for pais,ciudades in dicR.items():
        if (ciudad in ciudades) :
          lista_salida.append(region)
  return np.array(lista_salida)


#PROGRAMA PRINCIPAL

#5
eneroYagosto = totalVacunados("5 SEMANA/vacunacion.txt",1,8)

#6
poblacion,vacunas,ciudades,matriz = cargar_info("5 SEMANA/vacunacion.txt",3)

ciudades25 = []
for ciudad in ciudades : 
  ind_col = list(ciudades).index(ciudad)
  totalV = eneroYagosto.sum(axis = 0)
  if (totalV >= poblacion[ind_col]*0.25):
    print("Esta ciudad tiene mas del 25\%\ de la poblacion vacunado",ciudad)
    ciudades25.append(ciudad)

#7 
for ciudad in ciudades25 :
  matriz_abril = cargar_info("5 SEMANA/vacunacion.txt",4)[3]
  matriz_junio = cargar_info("5 SEMANA/vacunacion.txt",6)[3]
  
  ind_col = list(ciudades).index(ciudad)
  total_abril = matriz_abril.sum(axis = 0)[ind_col]
  total_junio = matriz_junio.sum(axis = 0)[ind_col]
  
  v_resultado = total_junio - total_abril
  print(v_resultado)




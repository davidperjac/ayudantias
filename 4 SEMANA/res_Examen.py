import numpy as np

tipo = {"V": "Vestimenta",
"A": "Alimentacion",
"E": "Educación",
"N": "Entretenimiento",
"S": "Salud",
}

barrios = {"Sector1": ["Alborada","Sauces III","Sauces IV"],
"Sector2": ["La Floresta","Guangala"],
}

#RESOLUCION

def cargarDatos(nomArchivo,dic_tipos, dic_barrios) :
  file = open(nomArchivo,"r")
  
  lista_tipos = list(dic_tipos.keys())
  lista_barrios = []
  
  for sector,lista in dic_barrios.items():
    for barrio in lista :
      lista_barrios.append(barrio)
  
  matriz= np.zeros( ( len(lista_barrios) , len(lista_tipos)*2 )  )
  file.readline()
  for linea in file :
    barrio,infoVenta = linea.strip("\n").split(":")
    fecha,local,tipo,valor = infoVenta.split(",")
    valor = float(valor[1:])
    for i in range(len(lista_barrios)):
      for j in range(len(lista_tipos)):
        if (fecha[-2:] == '19') :
            if (barrio == lista_barrios[i]) :
              if (tipo == lista_tipos[j]):
                matriz[i,j] += valor
        else : 
            if (barrio == lista_barrios[i]) :
              if (tipo == lista_tipos[j]):
                matriz[i,j+len(lista_barrios)] += valor
  file.close()
  return (matriz,lista_tipos,lista_barrios)


matriz,lista_tipos,lista_barrios = cargarDatos("4 SEMANA/compras.csv",tipo,barrios)

def promedios(M,año,l_tipos,t_barrios) :
  matriz = ''
  lista_barrios_final = []
  
  if (año == '19') :
    matriz = M[:,0:len(l_tipos)]
  else : 
    matriz = M[:,len(l_tipos):]
  
  v_suma = np.sum(matriz,axis=1)
  prom = v_suma.sum() / v_suma.size

  v_barrios = np.array(lista_barrios)
  v_barrios = v_barrios[v_suma > prom]
  
  return v_barrios

#PROGRAMA PRINCIPAL

v_barrios_prom = promedios(matriz,'20',lista_tipos,lista_barrios)
#print(v_barrios_prom)

deseo = input("Ingrese un sector: ")

while deseo not in ["7","1","4","2"] : 
  print("Error!, ingrese nuevamente")
  deseo = input("Ingrese un sector: ")

lista_sectores = barrios["Sector"+deseo]

ind_inicial = lista_barrios.index(lista_sectores[0])
ind_final = lista_barrios.index(lista_sectores[-1])

nueva_matriz = matriz[ind_inicial:ind_final +1, : ]

matriz_2019 =  nueva_matriz[:,0:len(lista_tipos)]
matriz_2020 = nueva_matriz[:,len(lista_tipos):]

suma_19 = matriz_2019.sum(axis=1)
suma_20 = matriz_2020.sum(axis=1)

v_resta_total = suma_20 - suma_19

indices = np.argsort(v_resta_total)[::-1]

v_barrios = np.array(lista_sectores)
mayores_barrios = v_barrios[indices][:5]

print(mayores_barrios)

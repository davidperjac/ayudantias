import numpy as np
# TERCERA EVALUACION PAO II 2020

lConductores = ["Pedro Perez",...]

M1 = np.array()
M2 = np.array()

l_tipos = []
l_barrios = []

def cargarDatos(conductor) :
  meses = ["Enero","Febrero"] #,"Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
  mesesNum = [1,2] #3,4,5,6,7,8,9
  dic = {}
  for mes in meses:
    dic[mes] = dic.get(mes,{"kms totales": 0,"lbs totales": 0,"barrios": set() })
  file = open(conductor+".txt","r")
  file.readline()
  for linea in file : 
    fecha,origen,destino,tipo,km,lbs = linea.strip("\n").split(",")
    dia,mes_A,anio = fecha.split("-")
    for i in range(len(mesesNum)):
      if (int(mes_A) == mesesNum[i]) :
        dic[meses[i]]["kms totales"]+=float(km)
        dic[meses[i]]["lbs totales"]+=float(lbs)
        dic[meses[i]]["barrios"].add(origen)
        dic[meses[i]]["barrios"].add(destino)
  file.close()
  return dic

def pagoConductor(conductor,mes) :
  dic_conductor = cargarDatos(conductor)
  kms = dic_conductor[mes]["kms totales"]
  if (kms < 200) :
    return kms * 0.085
  elif (kms >= 201 and kms <= 300):
    return kms * 0.075
  elif (kms > 300):
    return kms * 0.060

def barriosMasVisitados (l_conductores,mes):
    dic_barrios = {}
    #creacion del diccionario de barrios
    for conductor in l_conductores : 
      dic_conductor = cargarDatos(conductor)
      conj_barrios = dic_conductor[mes]["barrios"]
      for barrio in conj_barrios : 
          dic_barrios[barrio]= dic_barrios.get(barrio, 0)
          dic_barrios[barrio]+=1
    #ordenar por top 4
    v_barrios = np.array(dic_barrios.keys())
    v_veces = np.array(dic_barrios.values())
    ind_orden = np.argsort(v_veces)[::-1]
    return v_barrios[ind_orden][:4]

# PROGRAMA PRINCIPAL

#Muestre por pantalla los nombres de los 5 barrios en los que se entregaron más paquetes en los primeros 15 días del mes.

matriz_15 = M1[:,:15]
total_barrios= np.sum(matriz_15, axis = 1)
ind_orden = np.argsort(total_barrios)[::-1]
v_barrios = np.array(l_barrios)
top_5 = v_barrios[ind_orden][:5]
print(top_5)

#Muestre por pantalla cuál es el tipo de artículo que más se envía desde cada uno de los barrios mostrados en el numeral 4.

for barrio in top_5 : 
    ind_barrio = l_barrios.index(barrio)
    v_suma_articulos = M2[ind_barrio,:]
    ind_maximo = np.argmax(v_suma_articulos)
    v_tipos = np.array(l_tipos)
    print("Para el barrio {} el articulo máximo es {}".format(barrio,v_tipos[ind_maximo]))

#Muestre por pantalla los nombres de todos los barrios que durante el mes han enviado (salieron) más paquetes de lo que han recibido (entregados).


v_total_salida = np.sum(M2, axis = 1 )
v_total_entregado = np.sum(M1 , axis = 1)

v_operacion = v_total_salida - v_total_entregado  
v_barrios = np.array(l_barrios)

v_barrios_mas_salieron = v_barrios[v_operacion > 0]

print(v_barrios_mas_salieron)
import numpy as np

#PAO II 2016-2017 TERCERA EVALUACION

#TEMA 1

#literal 1
def obtenerClientes(nomarchivo) :
  file = open(nomarchivo,"r")
  dic = {}
  
  for linea in file:
    cedula,numero,sector,minutos,estado = linea.strip("\n").split(",")
    nac,inter = minutos.split("|")
    dic[cedula] = dic.get(cedula,{})
    dic[cedula][numero] = dic.get(numero,{'sector':sector,'nac':nac,'inter':inter ,'estado' : estado })
  return dic


dic = obtenerClientes("2 SEMANA/Clientes.csv")

#literal 2

def generarFactura(dic) :
  
  for cedula,dicNumeros in dic.items():
    #formato del archivo de salida
    file = open(cedula+".txt","a")
    file.write("Empresa David")
    file.write("\n")
    file.write("Cliente: " + cedula)
    file.write("\n")
    file.write("Detalle Deuda: ")
    file.write("\n")
    
    completo = 0
    for numero,dicInfo in dicNumeros.items():
      dinero_nacional = int(dicInfo['nac'])*0.03
      dinero_inter = int(dicInfo['inter'])
      
      if (dinero_inter < 60) :
        dinero_inter*=0.05
      elif (dinero_inter >= 60 and dinero_inter <= 90 ):
        dinero_inter*=0.04
      elif (dinero_inter > 90):
        dinero_inter*=0.03
      
      total_num = dinero_nacional + dinero_inter
      completo+=total_num
      file.write(str(numero) + " nac : " + str(dinero_nacional) + " inter : " + str(dinero_inter) + " total : " + str(total_num))
      file.write("\n")
    file.write("TOTAL A PAGAR : "+ str(completo))

#generarFactura(dic)

#literal 3

def estadisticaSector(dic,sector):
  
  lista_nacionales = []
  lista_internacionales = [] 
  
  for cedula,dicNumeros in dic.items():
    for numero,dicInfo in dicNumeros.items():
      
      if (dicInfo['estado'] == "Activo" and dicInfo['sector'] == sector ) :
        lista_nacionales.append(int(dicInfo['nac']))
        lista_internacionales.append(int(dicInfo['inter']))
    
  dicPromedio = {'Nacionales': (sum(lista_nacionales)/len(lista_nacionales)) , 'Internacionales' : (sum(lista_internacionales)/len(lista_internacionales))}
  return dicPromedio

dicPromedio = estadisticaSector(dic,"Norte")
print(dicPromedio)
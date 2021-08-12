
# TEMA 2 EXPORTACIONES

def calculaTotales(categoria) :
  file = open(categoria,"r")
  file.readline() 
  dic = {}
  for linea in file:
    comp,vend,prod,unidades,ventas,fecha = linea.strip().split(",")
    
    dic[ (comp,vend,prod) ] = dic.get((comp,vend,prod),0)
    dic[(comp,vend,prod)]+=float(ventas)
  file.close()
  return dic

prueba = calculaTotales("1 SEMANA/flores.txt")
print(prueba)

# UNIDAD 7 COLECCIONES

def informacionCovid(archivo) : 
  file = open(archivo, "r")
  file.readline()
  dic = {}
  for linea in file:
    pais,infec,muertos,continente = linea.strip().split(",")
    dic[continente] = dic.get(continente,{})
    dic[continente][pais] = dic[continente].get(pais,{'infectados':infec,'fallecidos':muertos})
  file.close()
  return dic

prueba2 = informacionCovid("1 SEMANA/infectados.txt")
#print(prueba2)
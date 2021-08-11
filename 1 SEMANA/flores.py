
# TEMA 2 EXPORTACIONES

def calculaTotales(categoria) :
  file = open(categoria,"r")
  file.readline() 
  dic = {}
  for linea in file:
    comp,vend,prod,unidades,ventas,fecha = linea.split(",").strip()
    
    dic[ (comp,vend,prod) ] = dic.get((comp,vend,prod),0)
    dic[(comp,vend,prod)]+=float(ventas)
  file.close()
  return dic

#prueba = calculaTotales("flores.txt")
#print(prueba)

# UNIDAD 7 COLECCIONES

def informacionCovid(archivo) : 
  file = open("infectados.txt", "r")
  file.readline()
  dic = {}
  for linea in file:
    pais,infec,muertos,continente = linea.split(",").strip()
    dic[continente] = dic.get(continente,{})
    dic[continente][pais] = dic[continente].get(pais,{'infectados':infec,'fallecidos':muertos})
  file.close()
  return dic

prueba2 = informacionCovid("infectados.txt")
print(prueba2)
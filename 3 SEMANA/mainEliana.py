'''
Implemente la funcion escribir_review(nombre_archivo,usuario,nombre_restaurante,puntaje,review) para que registre el review de una usuario.  
'''
def escribir_review(nombre_archivo,usuario,nombre_restaurante,puntaje,review):
  #usuario1,la hamburguesas de nina,5,deliciosas hamburguesas y la porcion super grande
  file=open(nombre_archivo,"a")
  file.write("\n"+usuario+","+nombre_restaurante+","+puntaje+","+review)
  file.close()



'''
Implemente la funcion calcular_promedio_restaurante(nombre_archivo, nombre_restaurante) para que reciba el nombre del archivo con los reviews y el nombre de un restaurante y retorne la calificacion promedio del restaurante
'''
def calcular_promedio_restaurante(nombre_archivo, nombre_restaurante):
  file=open(nombre_archivo,"r")
  #usuario1,la hamburguesas de nina,5,deliciosas hamburguesas y la porcion super grande
  calificacion_prom=[]
  for linea in file:
    usuario,restaurante,puntaje,review = linea.strip("\n").split(",")
    
    if restaurante == nombre_restaurante : 
      calificacion_prom.append(int(puntaje))
  file.close()
  return sum(calificacion_prom)/len(calificacion_prom)
    # puntajes=[]
    # for line in file:
    #   if usuario== line[1]:
    #     puntajes.append(line[2])
    #   puntajes1=int(puntajes)
    # prom_p=sum(puntajes1)/len(puntajes)
    # calificacion_prom+=prom_p
  #return calificacion_prom



'''
Implemente la funcion cargar_restaurante_info(archivo_restaurante, archivo_review) que reciba el nombre del archivo de restaurantes y el nombre del archivo de reviews y retorne un diccionario donde las claves son los nombres de los restaurantes y el valor asociado es es otro diccionario 
{
  "la hamburguesas de nina":
    {
      "puntaje": 4.33,
      "ubicacion":(5,7),
      "platos": ['hamburguesas','papas']
    },
  "picanteria doña ceci":
    {
      "puntaje": 4.5,
      "ubicacion":(2,4),
      "platos": ['ceviche','encebollado','bollo']
    },
  "comidas de victor":
    {
      "puntaje": 3,
      "ubicacion":(6,7),
      "platos": ['seco de pollo','menestra','bollo']
    },
}
'''
def cargar_restaurante_info(archivo_restaurante, archivo_review):
  fileRestaurantes=open(archivo_restaurante,"r")
  #la hamburguesas de nina,5|7,hamburguesas|papas
  
  dic = {}
  
  for linea in fileRestaurantes :
    
    restaurante,ubicacion,platos = linea.strip("\n").split(",")
    num1,num2 = ubicacion.split("|")
    
    ubicacion = (int(num1),int(num2)) 

    platos = platos.split("|")
    puntaje = calcular_promedio_restaurante(archivo_review,restaurante)
    
    dic[restaurante]=dic.get(restaurante,{"puntaje":puntaje,"ubicacion":ubicacion,"platos":platos})
  
  return dic
  
  
  
  
  
  # dic_restaurantes={}
  # for data in file1:
  #   data.strip("\n").split(",")
  #   restaurante=data[0]
  #   coordenadas=(data[1])
  #   platos=(data[2]).split("|")
  #   for info in file2:
  #     info.strip("\n").split(",")
  #     puntaje=info[2]
  #     #mira el comentario
  #     dic_restaurantes["restaurante"]=dic_restaurantes.get(restaurante,{"puntaje":puntaje,"ubicacion":coordenadas,"platos":platos})
  # return dic_restaurantes



'''
Implemente la funcion generar_reporte_plato(dic_restaurantes, nombre_plato) que recibe el diccionario con la informacion de los restaurantes y el nombre de un plato y genera un archivo con los nombres de los restaurantes que ofrecen el platillo con su puntaje promedio. El nombres del archivo generado es nombre_plato.txt
'''
def generar_reporte_plato(dic_restaurantes, nombre_plato):
  file=open(nombre_plato+".txt","w")
  
  for nombre_r,info_r in dic_restaurantes.items():
    if (nombre_plato in info_r["platos"]) :
      file.write(nombre_r+","+str(info_r["puntaje"])+"\n")
    
    # plato_r=dic_restaurantes["restaurante"]["platos"]
    # puntaje_r=dic_restaurantes["restaurante"]["puntaje"]
    # if nombre_plato == plato_r:
    #   file.write(nombre_r,puntaje_r)
  file.close()


'''
Implemente la funcion criticos_destacados(archivo_reviews) que recibe el archivo de reviews y muestra en pantalla el nombre de los tres usuarios que mas reviews han hechos. 
'''
def criticos_destacados(archivo_reviews):
  file=open(archivo_reviews,"r")
  dic = {}
  for linea in file :
    usuario,restaurante,puntaje,review = linea.strip("\n").split(",")
    dic[usuario] = dic.get(usuario,0)
    dic[usuario]+=1
  lista_tuplas =list(dic.items())
  lista_orden = []
  for i in range(len(lista_tuplas)) : 
    if len(lista_orden) < 3 :
      lista_orden.append(lista_tuplas[i])
    else : 
      for j in range(len(lista_orden)):
        if (lista_tuplas[i][1] > lista_orden[j][1]) :
          lista_orden[j] = lista_tuplas[i]
  
  print(lista_orden)
  
  
  # usuario=[]
  # for line in file:
  #   line.strip("\n").split("|")
  #   usuario_f=line[0]
  #   for data in file:
  #     usuario_nf=data[0]
  #     if usuario_f == usuario_nf:
  #       usuario.append(usuario_nf)

ARCHIVO_REVIEW = "reviews.txt"
ARCHIVO_RESTAURANTE = "restaurantes.txt"

#probando

#escribir_review(ARCHIVO_REVIEW , "David", "los arbolitos",'5',"muy rico ")

#prom = calcular_promedio_restaurante(ARCHIVO_REVIEW,'la hamburguesas de nina')
#print(prom)

#dic = cargar_restaurante_info(ARCHIVO_RESTAURANTE,ARCHIVO_REVIEW)
#print(dic)

#generar_reporte_plato(dic,"menestra")

criticos_destacados(ARCHIVO_REVIEW)




# opcion = ""
# while opcion!="4":
#   print("1. registrar review")
#   print("2. recomendar restaurante")
#   print("3. criticos destacados")
#   print("4. salir")
#   opcion = input("ingrese opcion: ")
#   if opcion=="1":
#     print("Registrar review")
#     nombre_usuario=input("ingrese nombre de usuario: ")
#     nombre_restaurante=input("ingrese nombre de restaurante: ")
#     puntaje=input("ingrese puntaje: ")
#     review=input("ingrese review: ")
#     f_review=escribir_review("reviews.txt",nombre_usuario,nombre_restaurante,puntaje,review)
#     #TODO: REGISTRE EL REVIEW

#   elif opcion=="2":
#     print("Reporte plato")
#     #PIDA AL USUARIO EL NOMBE DEL PLATO DEL QUE QUIERE EL REPORTE Y GENERE EL REPORTE
#     plato_nombre=input("Ingrese nombre del plato: ")
#     reporte_plato=generar_reporte_plato(dic_restaurantes,plato_nombre)
  
#   elif opcion=="3":
#     print("Criticos destacados")
#     #MUESTRE LOS NOMBRES DE LOS CRITICOS DESTACADOS
#     print(criticos_destacados("reviews.txt"))

#   else:
#     print("salir")

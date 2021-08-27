tiposdelitos={"robo":10,"asesinato":15,"vandalismo":5,"terrorismo":30}

palabrasclaves=["TNT","bomba","polvora","mision","muerte"]

def peligrosidad(personas, tiposdelitos):
  file=open(personas,"r")
  file.readline()  #cabecera

  dic={}
  for linea in file:
    partes=linea.strip("\n").split(",")
    ID=partes[0]
    edad=int(partes[1])
    instruccion=partes[2]

    detenciones=[]
    if len(partes)>3:
      detenciones=partes[3:]
    
    ptsprevios=0
    if len(detenciones)>1:
      ptsprevios = len(detenciones)*10

    ptsedad=0 
    if edad>= 20 and edad<=45:
      ptsedad= 10

    ptsinstr=0
    if (instruccion== "secundaria") or (instruccion=="tercer nivel"):
      ptsinstr=10
    
    ptsdelitos = 0
    for delito in detenciones : 
      if (delito == "robo") :
        ptsdelitos+=10
      elif (delito == "asesinato"):
        ptsdelitos+=15
      elif (delito == "vandalismo") :
        ptsdelitos+=5
      elif (delito == "terrorismo") :
        ptsdelitos+=30

    total= ptsprevios + ptsedad+ ptsinstr + ptsdelitos

    dic[ID]=total
  file.close()

  return dic

dicc_peligrosidad= peligrosidad("personas.txt", tiposdelitos)
print(dicc_peligrosidad)


def analizar_mensaje(linea, palabrasclaves): 
  
  linea=linea.split(" ")

  palabras=[]
  
  for i in range(len(linea)):
    if linea[i] in palabrasclaves:
      palabras.append(linea[i])
      datos=linea[0]

      separar=datos.split(":")
      plataforma=separar[0]
      

  tupla= (plataforma.title(), len(palabras))  
  
  return tupla


analizar= analizar_mensaje("twitter:la bomba esta en tucasa Pedir mas TNT", palabrasclaves )
#print(analizar)


def leer_mensajes(dicc_peligrosidad, palabrasclaves):
  dic={}

  for idpersona in dicc_peligrosidad:
    file= open(idpersona + ".txt")
    file.readline()

    dic[idpersona]= []
    for linea in file:
      plataforma,palabras=linea.strip().split(":")
      lista= palabras.split(" ")

      pal_sosp=[]
      for i in range(len(lista)):
        if  lista[i] in palabrasclaves  :
          pal_sosp.append(lista[i])
      dic[idpersona].append({"plataforma":plataforma, "palabras_sospechosas": len(pal_sosp) , "mensaje": palabras  } )
    file.close()
  return dic, pal_sosp

dicc_mensajes, pal_sosp= leer_mensajes(dicc_peligrosidad, palabrasclaves)
print(dicc_mensajes)

def generar_reporte(dicc_peligrosidad, dicc_mensajes):
  #NO HAGAN EN CASA
  #file= open("reporte.txt", "w")
  #persona=[]
  #rankings=[]
  
  #for clave in dicc_peligrosidad:
    #ranking=dicc_peligrosidad[clave]
    #if ranking>=30 and dicc_mensajes[{}] :
      #persona.append(clave)
      #rankings.append(ranking)

      #file.write("idsospechoso"+"ranking"+"numeropalabrassospechosas"+"\n")
  #file.close()
  #return file
  
  #SI
  file = open("reporte2.txt","a")
  
  for id,puntos in dicc_peligrosidad.items():
    lista_dic_id = dicc_mensajes[id]
    total_palabras_sospechosas = 0
    for dic_id in lista_dic_id : 
      total_palabras_sospechosas += dic_id['palabras_sospechosas']
    
    if (puntos >= 30 and total_palabras_sospechosas >= 2) :
      file.write(id+","+str(puntos)+","+str(total_palabras_sospechosas)+"\n")
  file.close()


#generar_reporte(dicc_peligrosidad, dicc_mensajes)


#extra
#implemente la funcion plataformas_mas_usadas para que imprima el pantalla las dos plataformas que mas se usaron en el envio de mensajes sospechos. Se debe imprimir el nombre de la plataforma y el numero de veces usadas
def plataformas_mas_usadas(dicc_mensajes):
  pass



#1. llame a la funcion peligrosida e imprima el resulado en pantalla

#2. analizar_mensaje a la funcion analizar_mensaje e imprima la salida en pantalla

#3. llame a la funcion leer_mensajes e imprima la salida en pantalla

#4. llame a la funcioon generar_reporte y genere el reporte
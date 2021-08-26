
#TALLER COLECCIONES Y ARCHIVOS

#FUNCION 1

def obtenerInfoEstudiantes(nomArchivoNotas,nomArchivoEstudiantes) :
  fileEstudiante = open(nomArchivoEstudiantes,"r")
  dic = {}
  
  for linea in fileEstudiante:
    infoEstudiante = linea.strip("\n").split(",")
    dic[infoEstudiante[0]] = dic.get(infoEstudiante[0],{"nombres":infoEstudiante[1],"apellidos":infoEstudiante[2],"asignaturas":[],"calificaciones":[]})
    
    
    #dic[infoEstudiante[0]]["asignaturas"].append(infoEstudiante[4:])
    cont = 0
    for i in range(int(infoEstudiante[3])):
      dic[infoEstudiante[0]]["asignaturas"].append(infoEstudiante[4+cont])
      cont+=1
    
    fileNotas = open(nomArchivoNotas,"r")
    
    for linea in fileNotas:
      infoNotas = linea.strip("\n").split(",")
      if (infoNotas[0]==infoEstudiante[0]):
        
        #dic[infoEstudiante[0]]["calificaciones"].append(infoNotas[1:])
        
        contNotas = 0
        for i in range(int(infoEstudiante[3])):
          dic[infoEstudiante[0]]["calificaciones"].append(float(infoNotas[1+contNotas]))
          contNotas+=1
      dic[infoEstudiante[0]]["asignaturas"] = tuple(dic[infoEstudiante[0]]["asignaturas"])
      
    dic[infoEstudiante[0]]["calificaciones"] = tuple(dic[infoEstudiante[0]]["calificaciones"])
  return dic


dic = obtenerInfoEstudiantes("3 SEMANA/notas.txt","3 SEMANA/estudiantes.txt",)


#FUNCION 2

def calcularPromediosEstudiantes(dic) : 
  dicPromedios = {}
  for matricula,dicInfo in dic.items():
    notas = dicInfo["calificaciones"]
    promedio = sum(notas) / len(notas)
    dicPromedios[matricula] = dicPromedios.get(matricula,promedio )
  
  return dicPromedios

dicPromedios = calcularPromediosEstudiantes(dic)

#FUNCION 3

lista_matriculas = list(dicPromedios.keys())

def obtenerPromedioEstudiantes(dic,lista_matriculas,nombre="reporte.txt") :
  file = open(nombre,"a")

  for matricula,nota in dic.items():
    file.write(matricula+"|"+str(nota)+"\n")


obtenerPromedioEstudiantes(dicPromedios,lista_matriculas)
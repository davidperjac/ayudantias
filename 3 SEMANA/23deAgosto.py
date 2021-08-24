
#TALLER COLECCIONES Y ARCHIVOS

#FUNCION 1

def obtenerInfoEstudiantes(nomArchivoNotas,nomArchivoEstudiantes) :
  fileEstudiante = open(nomArchivoEstudiantes,"r")
  dic = {}
  
  for linea in fileEstudiante:
    infoEstudiante = linea.strip("\n").split(",")
    dic[infoEstudiante[0]] = dic.get(infoEstudiante[0],{"nombres":infoEstudiante[1],"apellidos":infoEstudiante[2],"asignaturas":[],"calificaciones":[]})
    
    cont = 0
    for i in range(int(infoEstudiante[3])):
      dic[infoEstudiante[0]]["asignaturas"].append(infoEstudiante[4+cont])
      cont+=1
    
    fileNotas = open(nomArchivoNotas,"r")
    
    for linea in fileNotas:
      infoNotas = linea.strip("\n").split(",")
      if (infoNotas[0]==infoEstudiante[0]):
        
        contNotas = 0
        for i in range(int(infoEstudiante[3])):
          dic[infoEstudiante[0]]["calificaciones"].append(infoNotas[1+contNotas])
          contNotas+=1
      dic[infoEstudiante[0]]["asignaturas"] = tuple(dic[infoEstudiante[0]]["asignaturas"])
      
    dic[infoEstudiante[0]]["calificaciones"] = tuple(dic[infoEstudiante[0]]["calificaciones"])
  print(dic)


obtenerInfoEstudiantes("3 SEMANA/notas.txt","3 SEMANA/estudiantes.txt",)



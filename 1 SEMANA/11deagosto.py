import numpy as np

#Ejercicio de Maria de diccionarios y archivos

#1087654321 se llama Jorge

dicJorge = {'cedula':"1087654321" ,'Estudiantes' : {'cedula': [],'materias':[], 'total2Vez': 0 } } 

def anadirEstudiantes(nomArchivo,d):
  file = open(nomArchivo,"r")
  file.readline()
  
  for linea in file:
    id,usEstud,cedEstud,nombEstud,cedProf,materia,vecestomada = linea.strip("\n").split(",")
    
    materias = d['Estudiantes']['materias']
    
    if cedProf == d['cedula']:
      
      if materia not in d['Estudiantes']['materias']:
        d['Estudiantes']['materias'].append(materia)
        
      if cedEstud not in d['Estudiantes']['cedula']:
        d['Estudiantes']['cedula'].append(cedEstud)
    
      if int(vecestomada) == 2 :
        d['Estudiantes']['total2Vez']+=1

  d['Estudiantes']['cedula'] = tuple(d['Estudiantes']['cedula'])

#test

anadirEstudiantes("1 SEMANA/estudiantes.txt",dicJorge)

#print(dicJorge)

# ejercicio de maria de numpy
salida = np.full((13),-2,int)
cadena = 'djurado,1087654321,David Jurado,4-3-3-2-3'

usuario,cedula,nombre,materias = cadena.split(",")
#4-3-3-2-3
materias = materias.replace("-","")
#43323
for i in range(len(materias)):
  salida[i] = int(materias[i])

print(salida)
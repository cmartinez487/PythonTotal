from os import system
from pathlib import Path, PureWindowsPath

#modos de apertura
'''
r: Abre el fichero en modo lectura.
r+: Si quieres leer y escribir en el fichero.
w: Para sobreescribir el contenido.
a: Para añadir al final del fichero en el caso de que ya exista.
'''
#Apertura
#myFile = open('Prueba.txt', 'a')

#leer todo el archivo
'''
print(myFile.read())
'''

#Leer el archivo mediante un for
'''
counter = 0
for line in myFile:
    counter +=1
    print(f"linea nro {counter}: {line.rstrip()}")
'''

#Trabajar como una lista
'''
listLines = myFile.readlines()

listLines.pop()

print(listLines)
'''

#escritura del archivo
'''
#de esta forma no se agrega el salto de linea
myFile.write('Sieg Zeon!')
myFile.write('Sieg Zeon!!!!')
'''
#agregando saltos de linea
'''
myFile.write('Sieg Zeon! \n')
myFile.write('Sieg Zeon!!!! \n')
'''

#agregandolo como lista
'''
listLines = ['Char', 'Camile', 'Judai', 'Amuro']
#(este metodo es poco eficaz)
#myFile.writelines(listLines)

#(el for es mas eficaz)

for line in listLines:
    myFile.writelines(line + '\n')

'''

#Cierre
#myFile.close()

#trabajando con archivos en diferentes ubicaciones
#ruta de origen
#routePath = os.getcwd()

#Crear directorio, Establecer nuevo Directorio y Borrar Directorio
#nota: en linux y mac usar el metodo Path para poder usarlo al crear, borrar o acceder a un directorio
'''
#Crear un nuevo directorio
pathFolder = Path('/home/crmm/Repositorios/Python/PythonTotal/Day6/Alternative')
newPath = (pathFolder / 'Alternative2')
#newPathFolder = os.makedirs(newPath)

#remover un directorio
#os.rmdir(newPath)

#cambio de ruta
routePath = os.chdir(pathFolder)

newFile = pathFolder / 'test.txt'
myFile = open(newFile, 'r')
print(myFile.read())
'''

#Leyendo el archivo y directorios usando Path
'''
pathFolder = Path('/home/crmm/Repositorios/Python/PythonTotal/Day6/Files')
myFilePath = pathFolder / 'test.txt'


winPath = PureWindowsPath(pathFolder)

myFilePath.write_text('nuevo archivo \n')
print(winPath)
print(myFilePath.read_text())

#directorio base del usuario
basePath = Path.home()
print(basePath)

#usando el metodo path de forma correcta
pathFolder = os.getcwd()
myFilePath = Path(pathFolder, 'Files')

print(myFilePath)
'''

#Limpiar consola
'''
name = input("Usuario, tu nombre: ")
age = input("y tu edad, Usuario: ")

print(f'el usuario {name} tiene una edad de {age}... ahora borraremos estos datos de la pantalla')
system('clear')
print(f'datos borrados de la pantalla')
'''


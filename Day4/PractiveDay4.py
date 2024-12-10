#from random import randint #importacion especifica de una libreria
from random import * #importacion de toda la libreria

#valores de comparacion
'''
myBool = 10==25
print(myBool)

myBool = 'blanco' == 'Blanco'.lower()
print(myBool)

myBool = 'blanco' == 'Blanco'.lower()
print(myBool)

#myBool = 4<5 and 5>6
myBool = 4<5 and 5>6
print(myBool)

myBool = not 3 >= 3
print(myBool)

'''

#Control de flujo (if, elif, else)
'''
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))

if num1>num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")
'''

#loop For
'''
myList = ['a','b','c']
for letter in myList:
    nLetter = myList.index(letter) + 1
    print(f"letter {nLetter}: {letter}")

myList = ['Carlos','Rafael','Calavera', 'Char']

for name in myList:
    if name.startswith('R'):
        print(name)

myList = [1,2,3,4,5]
nvalor = 0
for number in myList:
    nvalor = nvalor + number

print(nvalor)

Word = 'Python'
for letter in Word:
    print(letter)

for letter in 'GO':
    print(letter)

myList = [[1,2],[3,4],[5,6]]
for list1, list2 in myList:
    print(f"list1: {list1}")
    print(f"list2: {list2}")

myDic = {'valor':'clave', 'valor1':'clave1'}
for item in myDic:
    print(f"item: {item}")
'''

#loop while
'''
monedas = 5
while monedas>0:
    print(f"tienes {monedas} monedas")
    monedas -= 1
else:
    print("te quedaste sin monedas...")

respuesta = 's'

while respuesta =='s':
    print(f"Adivina para salir del loop!!!! tu respuesta anterior fue una la correcta, si no es la indicada no podras salir!!!")
    respuesta = input("quieres intentarlo nuevamente? :")
    if respuesta != 's' and respuesta != 'n':
        respuesta = 's'

else:
    print('Gracias por probar el codigo!!!')
'''

#Rangos - Range
'''
for num in range(5):
    print(num)

for num in list(range(1,11)):
    print(num)

#enumeradores
myList = ['a','b','c']

for index, item in enumerate(myList):
    print(index, item)

myTuples = list(enumerate(myList))
print(myTuples)
print(myTuples[1][0])
'''

#zip
'''
paises = ['Alemania','Japon','EEUU']
numeros = [1,2,3]
pistas = ['Nürburgring', 'Suzuka', 'Laguna Seca']

combineList = zip(paises, numeros)
print(combineList)
print(list(combineList))

combineList2 = zip(paises, numeros, pistas)
#print(list(combineList2))

for pais, numero, pista in combineList2:
    print(f"{numero} - {pais} tiene la pista de {pista}")
'''

#min y max
'''
menor = min(58,96,101,12,52)
mayor = max(58,96,101,12,52)
print(menor, mayor)

lista = [58,96,101,12,52]
print(min(lista), max(lista))

paises = ['Alemania','Japon','EEUU']
print(min(paises), max(paises))

nombre = 'Carlos'
print(min(nombre), max(nombre))
'''

#random
'''
pilots = ['Amuro','Char','Gato', 'Judai', 'Camile', 'Frontier']
numbers = list(range(5,50,5))
randomNumber = randint(1, 50)
randomUniform = uniform(1,5)
randomNumber2 = random()
aleatorioChoice = choice(pilots)
shuffle(numbers)
print(f'randint: {randomNumber}')
print(f'uniform: {randomUniform}')
print(f'random: {randomNumber2}')
print(f'choice: {aleatorioChoice}')
print(f'shuffle: {numbers}')
'''

#comprension de listas
#metodo tradicional
'''
word = 'Python'
myList = []

for letter in word:
    myList.append(letter)
'''
#metodo acortado
'''
word = 'Python'
numbers = range(0,21, 2)
myList = [letter for letter in word]
#myListNum = [number for number in numbers]
#myListNum = [number/2 for number in numbers]
#myListNum = [number for number in numbers if number*2>10]
myListNum = [number if number*2>10 else 'no' for number in numbers]

print(myList)
print(myListNum)

pies = [10,20,30, 40, 50]
metros = [metro*3.281 for metro in pies]
print(metros)
'''

#Mach
'''
#ejemplo con if

num1 = 2
num2 = 2

if num1>num2:
    print(f"{num1} es mayor que {num2}")
elif num1<num2:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")

#match
match num1>num2:
    case True:
        print(f"{num1} es mayor que {num2}")
    case False:
        print(f"{num2} es mayor que {num1}")
    case _:
        print(f"{num1} y {num2} son iguales")
        
        
cliente = {'nombre':'Carlos', 'edad':37, 'ocupacion': 'Programador'}
pelicula = {'titulo':'Matrix', 'fichaTecnica':{'protagonista':'Keanu Reeves',
                                               'director':'Hermanas Wachoski'}}
elementos = [cliente, pelicula, 'Libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad':edad,
              'ocupacion':ocupacion}:
            print(f'Datos del Cliente: '
                  f'nombre: {nombre}, edad: {edad}, ocupacion: {ocupacion}')
        case {'titulo':titulo,
              'fichaTecnica': {
                  'protagonista': protagonista,
                  'director': director
              }}:
            print(f'Datos de la Pelicula: '
                  f'Titulo: {titulo}, Protagonista: {protagonista}, Director: {director}')
        case _:
            print("sepa dios que es esto...")       
'''



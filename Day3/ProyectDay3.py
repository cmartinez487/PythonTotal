#Ingresa un texto en una variable, ingresar 3 letras a su eleccion en 3 variables mas y ejecuta las siguientes tareas
# 1ro - Cuantas veces aparecen las letras en el texto - pude con ayuda
# 2do - Cuantas palabras hay a lo largo del texto ingresado - listo
# 3ro - cuales son la 1era y la ultima letra - listo
# 4to - texto en orden inverso - listo
# 5to - si la palabra python aparece en el texto - no pude
#

myText = input('Ingresa el texto a analizar: ')
letters = []
myText = myText.lower()
countLetters = len(myText)
invertText = myText[::-1]

letters.append(input('ingresa la 1era letra: ').lower())
letters.append(input('ingrese la 2da letra: ').lower())
letters.append(input('ingresa la 3era letra: ').lower())

test1 = myText.index(letters[0])
ctest1 = myText.count(letters[0])
test2 = myText.index(letters[1])
ctest2 = myText.count(letters[1])
test3 = myText.index(letters[2])
ctest3 = myText.count(letters[2])

fLetter = myText[0]

lenText = len(myText)
pLenText = len(myText)-1
lLetter = myText[pLenText:lenText]

palabras = myText.split()

print("\n")
print("Texto a analizar: " + myText)
print(f"Letras: {letters}")
print("\n")
print("Texto Invertido: " + invertText)
print("\n")
print(f"1era aparicion de la letra {letters[0]}: {test1}, cantidad de veces que se repite {ctest1}")
print(f"1era aparicion de la letra {letters[1]}: {test2}, cantidad de veces que se repite {ctest2}")
print(f"1era aparicion de la letra {letters[2]}: {test3}, cantidad de veces que se repite {ctest3}")
print("\n")
print(f"Conteo de letras:  {countLetters}")
print(f"Primera letra:  {fLetter}")
print(f"Ultima letra:  {lLetter}")
print("\n")
print(f"Palabras contenidas en el mensaje:  {palabras}")
print(f"Cantidad de palabras contenidas en el mensaje:  {len(palabras)}")

searchPython = 'python' in myText
if searchPython:
    print(f"la palabra python esta contenida en el texto")
elif not searchPython:
    print(f"la palabra python no esta contenida en el texto")
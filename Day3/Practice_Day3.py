myText = "esta es una prueba"

#manejo del index() y rindex()
#resultText = myText.index("prueba")
#resultText = myText.rindex("prueba")
#resultText = myText.index("a", 5, 11)
#print('index: ' + str(resultText))

#manejo del substring
lenText = len(myText)
pLenText = len(myText)-1

resultText = myText[pLenText:lenText]
#print(resultText)

print(resultText)


#funcion especial del substring
myText2 = "abcdefghijklmnopqrstuvwxyz"
fragment = myText2[2:10:4] #el ulimo se usa para saltear el nro de caracteres que se ordene
#print(fragment)

#Metodos de String que podrian ser utiles

#Upper, Lower. split
myText2 = "abcdefghijklmnopqrstuvwxyz"
#print(myText2.upper())
#print(myText2.lower())
#print(myText.split())
#print(myText.split("e")) #split con criterio de separacion

#join, find, replace
a = "Esto"
b = "es"
c = "muy"
d = "aburrido"
resultText = " ".join([a,b,c,d])
#print(resultText)
#print(resultText.find("aburrido"))
#print(resultText.replace("aburrido", "divertido"))

#Listas
myList = ['a', 'b', 'c']
myList2 = ['d', 'e', 'f']
myList[0] = 'c'
myList[2] = 'a'
mylist3 = myList + myList2
mylist3.append('g')
pop_list3 = mylist3.pop(6)
#print(mylist3)

#nota sort solo funciona cuando esta en su lugar... solo funciona cuando esta fuera de un print, por si sola...
# tampoco se puede generar una variable de ella porque solo devolveria un none
mylist3.sort()
#print(mylist3)
#print(pop_list3)

#diccionarios
myDicctionary = {'c1':1, 'c2':2}
#print(myDicctionary)

resultDic = myDicctionary['c2']
#print(resultDic)

clientDic = {'name': 'canonical', 'ubication': 'Reino Unido', 'product':'Ubuntu Distro'}

nameClient = clientDic['name']
#print(nameClient)

charDic = {'val1':[4,'abril',1987], 'val2':37, 'val3':{'name1':'Carlos', 'name2':'Rafael'}}
#print(charDic['val1'][1])
#print(charDic['val3']['name1'])

dic = {'a1':['a', 'b', 'c'], 'a2':['d', 'e', 'f']}
#print(dic['a2'][1].upper())

dic2 = {1:1,2:2}
dic2[3] = 3 #agregando valores a un diccionario
dic2[2] = 2.2 #modificando valor en un diccionario
#print(dic2.keys())
#print(dic2.values())
#print(dic2.items())

#tuplas, set, boolean
myNumTuples = (1,2,3,4)
#print(type(myNumTuples))

mySet = set([1,2,3,4,5])
#print(type(mySet))

#mySet2 = {1,2,3,4,5}
#print(type(mySet2))
mySet.add(6)
#print(mySet)

set1 = {9,8,7}
set2 = {7,6,5}
set3 = set1.union(set2)
#print(set3)

numero = 5>(2+2)
numero = bool(5>(3+2))
#print(type(numero))
#print(numero)



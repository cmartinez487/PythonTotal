#1er Ejercicio
def devolverDistintos(num1, num2, num3):
    numResult = 0
    numList = [num1, num2, num3]  # Aquí está la corrección
    suma = num1+num2+num3
    message = ''

    if suma > 15:
        for number in numList:
            if  number> numResult:
                numResult = number
        message = f'suma = {suma}, numero mayor = {numResult}'
    elif suma < 10:
        for number in numList:
            if  number < numResult or numResult == 0:
                numResult = number
        message = f'suma = {suma}, numero menor = {numResult}'

    elif 15 >= suma >= 10:
        numList.sort()
        numResult = numList[1]
        message = f'suma = {suma}, numero intermedio = {numResult}'
    return message

#print(devolverDistintos(1,2,3))
#print(devolverDistintos(1,6,9))
#print(devolverDistintos(3,2,9))

#2do Ejercicio
def usedSets(word):
    wordSet = set()
    for letter in word:
        wordSet.add(letter)

    listWord = sorted(wordSet)

    return listWord

#print(usedSets("pararangaricutirimicuaro"))

#3er Ejercicio
def inumeratedArgument(*args):
    listNum = []
    response = False
    for arg in args:
        listNum.append(arg)
        cantList=len(listNum)-1

        if cantList>0:
            if listNum[cantList] == listNum[cantList-1]:
                response = True

    return response

args = [1,2,0,3,0,0,4]
#print(inumeratedArgument(*args))

#4to Ejercicio - no lo realice yo...

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def contar_primos(num):
    primos = []
    for i in range(num + 1):
        if es_primo(i):
            primos.append(i)

    print(f"Números primos hasta {num}: {primos}")
    return len(primos)


# Ejemplo de uso
#cantidad_primos = contar_primos(487)
#print(f"Cantidad de números primos encontrados: {cantidad_primos}")

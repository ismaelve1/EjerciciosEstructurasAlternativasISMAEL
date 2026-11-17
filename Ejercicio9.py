num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))
num3 = float(input("Introduce el tercer numero: "))

#esto es una lista. guarda variables dentro de otra
numeros = [num1, num2, num3]

#sort es una funcion que ordena los elementos de una lista
#lo de reverse es para que el orden sea inverso y el true es para que si lo haga
numeros.sort(reverse=True)

print(numeros)
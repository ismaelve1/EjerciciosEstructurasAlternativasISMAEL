nota = int(input("Ingrese su nota: "))
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo: ")

if nota >= 5 and edad >= 18 and sexo =="F":
    print("ACEPTADA")
elif nota >= 5 and edad >= 18 and sexo =="M":
    print("POSIBLE")
else:
    print("NO ACEPTADA")
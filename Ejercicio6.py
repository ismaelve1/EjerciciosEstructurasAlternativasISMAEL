letra = input("Introduce una letra: ")

if len(letra) == 0:
    print("No has introducido ninguna letra")
elif letra.isupper() and len(letra) == 1:
    print("Es una letra mayuscula")
else:
    print("No es una letra mayuscula")
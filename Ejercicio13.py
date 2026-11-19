dia = int(input("Introduce el dia: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

if mes < 1 or mes > 12:
    print("La fecha no es correcta")

elif dia < 1:
    print("La fecha no es correcta")

elif mes == 2:
    if dia <= 29:
        print("La fecha es correcta")
    else:
        print("La fecha no es correcta")

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia <= 30:
        print("La fecha es correcta")
    else:
        print("La fecha no es correcta")

else:
    if dia <= 31:
        print("La fecha es correcta")
    else:
        print("La fecha no es correcta")
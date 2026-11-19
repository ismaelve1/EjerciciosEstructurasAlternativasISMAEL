A = float(input("Introduce el lado A: "))
B = float(input("Introduce el lado B: "))
C = float(input("Introduce el lado C: "))

if A**2 + B**2 == C**2 or A**2 + C**2 == B**2 or B**2 + C**2 == A**2:
    print("Es un triangulo rectangulo")

elif A == B == C:
    print("Es un triangulo equilatero")

elif A == B or A == C or B == C:
    print("Es un triangulo isosceles")

else:
    print("Es un triangulo escaleno")
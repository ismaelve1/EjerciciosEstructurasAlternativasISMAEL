import math

x1 = float(input("Introduce x1: "))
y1 = float(input("Introduce y1: "))
x2 = float(input("Introduce x2: "))
y2 = float(input("Introduce y2: "))

r1 = float(input("Introduce el radio 1: "))
r2 = float(input("Introduce el radio 2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if distancia > r1 + r2:
    print("Son exteriores")

elif distancia == r1 + r2:
    print("Son tangentes exteriores")

elif distancia > abs(r1 - r2):
    print("Son secantes")

elif distancia == abs(r1 - r2):
    print("Son tangentes interiores")

elif distancia < abs(r1 - r2):
    print("Son interiores")

else:
    print("Son concéntricas")
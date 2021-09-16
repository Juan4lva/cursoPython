# arreglos

n = int(input('ingrese el tamano del arreglo: '))
m = int(input('ingrese el numero de multiplos: '))

a = []
for i in range(0,n):
    a.append(i*m)

print(a)
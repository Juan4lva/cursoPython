# la usma de los primeros n numeros

n = int(input('ingrese un numero: '))

suma = 0
for i in range(1, n + 1):
    suma = suma + i
print('la suma de los n numero', n, 'es', suma)
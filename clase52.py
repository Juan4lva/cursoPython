# arreglos

# calcular 10 numeros aleatorios

import random

def vector_aleatorio(n):
    vector = [0]*n
    for i in range(n):
        vector[i] = random.randint(0,10)
    return vector

print('ingrese cuantos numeros aleatorios desea obtener')
n = int(input())

aleatorio = vector_aleatorio(n)
print(aleatorio)
# mostrar la suma de los n primeros numeros
n = int(input('ingrese un numero: ')) 
suma = 0
i = 1
while i<=n:
    suma = suma + i
    i = i + 1
print('la suma de los numeros hasta ', n, 'es: ', suma)
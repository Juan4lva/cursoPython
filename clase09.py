# opcion b (elif)
# verificar si un numero es positivo, neutro o negativo
b = int(input('ingrese un numero: '))
if b < 0:
    R = 'negativo'
elif b ==0:
    R = 'neutro'
else:
    R = 'positivo'
print('el numero es: ',R)
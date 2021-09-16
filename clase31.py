# seleccionar impares y terminar al encontrar el primero divisible por 6
n = int(input('ingrese un numero: '))
for i in range(1,n+1):
    if not(i % 2) & (i % 6):
        continue
    if i % 6 == 0:
        break
    print(i)
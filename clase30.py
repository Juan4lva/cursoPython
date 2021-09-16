# break
n = int(input('ingrese un numero: '))
for i in range(1,n+1):
    if i % 2 == 0:
        break # sale del ciclo
        print(i)
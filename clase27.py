# identificar pares e impares
n1 = int(input('ingrese un numero: '))
n2 = int(input(f'ingrese un numero mayor o igual que {n1}: '))

if n2 < n1:
    print(f'ingrese un numero mayor o igual que {n1}')
else:
    for i in range(n1,n2+1):
        if i % 2 == 0:
            print(f'el numero {i} es par')
        else:
            print(f'el numero {i} es impar')

# numero factorial
# ejempo:
# 2! = 1 * 2 =2

n = int(input('ingrese un numero: '))
if n <= 0:
    print('ingrse un numero positivo')
else:
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    print(f'el factorial es {n} es {factorial}')
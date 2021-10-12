# calificacion de notas
# datos:
# n: notas
# r: respuesta

n = float(input('ingrese su nota: '))
if n <= 50:
    r = 'reprobado'
elif n <= 80:
    r = 'aprobado'
elif n <= 90:
    r = 'sobresaliente'
else:
    r = 'excelente'

print('su nota', n, r)
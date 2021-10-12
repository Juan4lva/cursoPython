#funciones para atributos

class Persona:
    edad = 27
    nombre = 'victor'
    pais = 'brasil'

doctor = Persona()

print('la edad es: ',doctor.edad)
print('la edad es: ', getattr(doctor,'edad'))
print('el doctor tiene una edad?',hasattr(doctor,'edad'))
print(doctor.nombre)
setattr(doctor, 'nombre', 'hector')
print(doctor.nombre)
delattr(Persona, 'pais')
print(doctor.edad)
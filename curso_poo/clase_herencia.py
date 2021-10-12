#herencia

class pokemon: #clase padre
    pass
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def descripción(self):
        return '{} es un pokemon de tipo: {}'.format(self.nombre, self.tipo)

class pikachu(pokemon): #clase hijo
    def ataque(self,tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipoataque)

class charmander(pokemon):
    def ataque(self,tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipoataque)

nuevo_pokemon = pikachu('boby', 'electrico')
print(nuevo_pokemon.descripción())
print(nuevo_pokemon.ataque('Impacto trueno'))
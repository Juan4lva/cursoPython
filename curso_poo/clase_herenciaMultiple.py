#herencia multiple
class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print('llamando...')
    def ocupado(self):
        print('ocupado...')

class Camara:
    def __init__(self):
        pass
    def fotografia(self):
        print('tomando fotos...')

class Reproduccion:
    def __init__(self):
        pass
    def reproduccionmusica(self):
        print('reproduciendo musica')
    def reproducirvideo(self):
        print('reproducir un video...')

class smartphone(Telefono, Camara, Reproduccion):
    def __del__(self):
        print('telefono apagado')

movil = smartphone()

#print(dir(movil))

print(movil.fotografia())

print(movil.llamar())
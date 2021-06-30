from pila import Pila
from random import randint

class Traje(object):
    # modelo, pelicula, estado = '', '', ''

    def __init__(self, modelo, pelicula, estado):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado

    def __str__(self):
        return self.modelo+' - '+self.pelicula+' - '+self.estado

pila = Pila()
pila_aux = Pila()

traje = Traje('Mark III', 'Avengers I', 'Dañado')
pila.apilar(traje)
traje = Traje('Mark I', 'Iron Man I', 'Destruido')
pila.apilar(traje)
traje = Traje('Mark XLIV', 'Capitan America: Civil War', 'Dañado')
pila.apilar(traje)
traje = Traje('Mark III', 'Iron Man I', 'Impecable')
pila.apilar(traje)
traje = Traje('Mark XXV', 'Avengers II', 'Dañado')
pila.apilar(traje)

control_traje = False

while(not pila.pila_vacia()):
    x = pila.desapilar()
    # punto a
    if(x.modelo == 'Mark XLIV'):
        print('el moelo Mark XLIV fue utilizado en', x.pelicula)
    #punto b
    if(x.estado == 'Dañado'):
        print('el modelo', x.modelo, 'resulto dañado')
    #punto c
    if(x.estado == 'Destruido'):
        print('el modelo', x.modelo, 'resulto destruido')
    else:
        pila_aux.apilar(x)
    if(x.pelicula == 'Capitan America: Civil War' or x.pelicula == 'Spiderman'):
        print(x.modelo, 'es utilizado en las peliculas indicadas')

while(not pila_aux.pila_vacia()):
    pila.apilar(pila_aux.desapilar())

# if(not control_traje):
#     traje = Traje('Mark LXXXV', 'Avengers II', 'Dañado')
#     pila.apilar(traje)

while(not pila.pila_vacia()):
    print(pila.desapilar())
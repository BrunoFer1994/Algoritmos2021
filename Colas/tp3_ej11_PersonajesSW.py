"""11. Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta de origen. 
Desarrollar las funciones necesarias para resolver las siguientes actividades:
 a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
 b. indicar el planeta natal de Luke Skywalker y Han Solo
 c. insertar un nuevo personaje antes del maestro Yoda
 d. eliminar el personaje ubicado después de Jar Jar Binks"""

from cola import Cola

class Starwars(object):

    def __init__(self, personaje, planeta):
        self.personaje = personaje
        self.planeta = planeta

    def __str__(self):
        return self.personaje+' - '+self.planeta

cola = Cola()
cola1 = Cola()

personaje_info = Starwars('Darth Vader', 'Tatooine')
cola.arribo(personaje_info)
personaje_info = Starwars('Jar Jar Binks', 'Naboo')
cola.arribo(personaje_info)
personaje_info = Starwars('Obi-Wan', 'Stewjon')
cola.arribo(personaje_info)
personaje_info = Starwars('Luke Skywalker', 'Tatooine')
cola.arribo(personaje_info)
personaje_info = Starwars('Han Solo', 'Mos Eisley')
cola.arribo(personaje_info)
personaje_info = Starwars('Maestro Yoda', 'Endor')
cola.arribo(personaje_info)
personaje_info = Starwars('Princesa Leia', 'Alderaan')
cola.arribo(personaje_info)


print('la cola ingresada es: ')
for i in range(cola.tamanio()):
    print(cola.mover_final())
print('\n')


while(not cola.cola_vacia()):
    X = cola.atencion()
    # a
    if(X.planeta == 'Alderaan' or X.planeta == 'Endor' or X.planeta == 'Tatooine'):
        print('Los personajes del planeta Alderaan, Endor o Tatooine son:\n', X.personaje + ' -> ' + X.planeta)
            

    # b
    if(X.personaje == 'Luke Skywalker'):
        print('Luke Skywalker es del planeta:\n', X.planeta)

    if(X.personaje == 'Han Solo'):
        print('Han Solo es del planeta:\n', X.planeta)

    # C y D
    if(X.personaje == 'Maestro Yoda'):
        cola1.arribo(Starwars('Chewbacca', 'Kashyyyk'))
    elif(X.personaje == 'Jar Jar Binks' and not cola.cola_vacia()):
        cola.atencion()
    cola1.arribo(X) 

cantidad = cola.tamanio()
i = 0
while(i < cantidad):
    X = cola.atencion()
    if(X.personaje == 'Maestro Yoda'):
        cola.arribo(Starwars('Chewbacca', 'Kashyyyk'))
    elif(X.personaje == 'Jar Jar Binks' and i < cantidad-1):
        cola.atencion()
        i += 1
    cola.arribo(X)
    i += 1

print('\n')
print('La cola actualizada para el punto C y D es: ')
for i in range(cola1.tamanio()):
    print(cola1.mover_final())

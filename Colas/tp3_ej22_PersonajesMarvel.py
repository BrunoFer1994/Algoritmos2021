"""22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe y 
su género (Masculino M y Femenino F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., 
desarrollar un algoritmo que resuelva las siguientes actividades:
 a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
 b. mostrar los nombre de los superhéroes femeninos;
 c. mostrar los nombres de los personajes masculinos;
 d. determinar el nombre del superhéroe del personaje Scott Lang;
 e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
 f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes."""

from cola import Cola

class Marvel(object):

    def __init__(self, nombre, personaje, genero):
        self.nombre = nombre
        self.personaje = personaje
        self.genero = genero

    def __str__(self):
        return self.nombre+' - '+self.personaje+' - '+self.genero

cola = Cola()
cola1 = Cola()

personaje_info = Marvel('Stark Tony', 'Iron Man', 'M')
cola.arribo(personaje_info)
personaje_info = Marvel('Steve Rogers', 'Capitán América', 'M')
cola.arribo(personaje_info)
personaje_info = Marvel('Natasha Romanoff', 'Black Widow', 'F')
cola.arribo(personaje_info)
personaje_info = Marvel('Peter Parker', 'Spider Man','M')
cola.arribo(personaje_info)
personaje_info = Marvel('Chris Hemsworth', 'Thor', 'M')
cola.arribo(personaje_info)
personaje_info = Marvel('Carol Danvers', 'Capitana Marvel', 'F')
cola.arribo(personaje_info)
personaje_info = Marvel('Scott Lang', 'Ant-Man','M')
cola.arribo(personaje_info)

print('la cola ingresada es: ')
for i in range(cola.tamanio()):
    print(cola.mover_final())
print('\n')

while(not cola.cola_vacia()):
    x = cola.atencion()
    # a
    if (x.personaje == 'Capitana Marvel'):
        print('El nombre del personaje de la superhéroe Capitana Marvel es: ', x.nombre)

    # b
    if (x.genero == 'F'):
        print('Los personajes femeninos son: ', x.personaje)

    # c
    if (x.genero == 'M'):
        print('Los personajes masculinos son: ', x.personaje)

    # d
    if (x.nombre == 'Scott Lang'):
        print('El nombre del superhéroe del personaje Scott Lang es: ', x.personaje)

    # e
    for letra in (x.nombre):
        if letra == "S":
            print ('Los personajes que empiezan con S son: ', x.nombre+' - '+x.personaje+' - '+x.genero)

    # f
    if (x.nombre == 'Carol Danvers'):
        print("Carol Danvers esta en la cola y su personaje es: ", x.personaje)
        continue

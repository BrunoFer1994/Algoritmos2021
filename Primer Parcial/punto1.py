def barrido(vec):
    if(len(vec)>0):
        print (vec[0])
        barrido(vec[1:])
        
def starwars(personaje,pos=0):
    if(pos < len(personaje)):
        if(personaje[pos] == 'Maestro Yoda'):
            print('El Maestro Yoda se encuentra en el vector y esta en la posicion: ' )
            return pos
        else:
            return starwars(personaje, pos+1)
    else:
        return ('El Maestro Yoda no se encuentra en el vector')

personajes = ['Darth Vader','Luke Skywalker','Leia Organa','Maestro Yoda','Chewbacca']

print('Los personajes del vector son: ')
barrido(personajes)
print()
print(starwars(personajes))
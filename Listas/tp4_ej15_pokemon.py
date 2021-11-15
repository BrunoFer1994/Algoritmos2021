from lista import Lista

entrenadores = Lista()
pokemones = Lista()
entrenadores_79 = Lista()
lista_tipos = Lista()

file = open('entrenadores.txt')
file2 = open('pokemones.txt')

lineas = file.readlines()
lineas.pop(0)

for linea in lineas:
    entrenador = linea.split(';')
    entrenador_data = {}
    entrenador_data['Nombre'] = entrenador[0]
    entrenador_data['Torneos'] = int(entrenador[1])
    entrenador_data['Perdidas'] = int(entrenador[2])
    entrenador_data['Ganadas'] = int(entrenador[3])
    entrenador_data['ID'] = int(entrenador[4].split('\n')[0])
    entrenador_data['Pokemones'] = Lista()
    entrenadores.insertar(entrenador_data, 'Nombre')

lineas = file2.readlines()
lineas.pop(0)

for linea in lineas:
    pokemon = linea.split(';')
    pokemon_data = {}
    pokemon_data['Nombre'] = pokemon[0]
    pokemon_data['Nivel'] = int(pokemon[1])
    pokemon_data['Tipo'] = pokemon[2]
    pokemon_data['Subtipo'] = pokemon[3]
    pokemon_data['ID'] = int(pokemon[4].split('\n')[0])
    pokemones.insertar(pokemon_data, 'ID')

for i in range (entrenadores.tamanio()):
    id_entrenador = entrenadores.obtener_elemento(i)['ID']
    for j in range (pokemones.tamanio()):
        id_pokemon = pokemones.obtener_elemento(j)['ID']
        if (id_entrenador ==  id_pokemon):
            entrenadores.obtener_elemento(i)['Pokemones'].insertar(pokemones.obtener_elemento(j), 'Nombre')

def mostrar_datos (lista, pos):
    """Muestra los datos de los entrenadores y los datos de cada pokemon del entrenador."""
    entrenador = lista.obtener_elemento(pos)
    print('•',entrenador['Nombre'])
    print ('Torneos Ganados:', entrenador['Torneos'], '| Batallas perdidas:', entrenador['Perdidas'], '| Batallas ganadas:', entrenador['Ganadas'] )
    print ('Pokemones:')
    for j in range(0, entrenador['Pokemones'].tamanio()):
        pokemones = lista.obtener_elemento(pos)['Pokemones']
        print(pokemones.obtener_elemento(j)['Nombre'], '| Nivel:', pokemones.obtener_elemento(j)['Nivel'], '| Tipo:', 
        pokemones.obtener_elemento(j)['Tipo'], '| Subtipo:', pokemones.obtener_elemento(j)['Subtipo'])

for i in range (entrenadores.tamanio()):
    mostrar_datos(entrenadores, i)
    print()

# Punto a
entr = input('Ingrese el nombre del entrenador para saber su cantidad de Pokemon: ').capitalize()
pos = entrenadores.busqueda(entr, 'Nombre')
if pos != -1:
    print ('La cantidad de Pokemon de', entr, 'es:', entrenadores.obtener_elemento(pos)['Pokemones'].tamanio())
print()

may_torneos = entrenadores.obtener_elemento(0)

# Punto b
print('Entrenadores que han ganado mas de 3 torneos:')
for i in range (entrenadores.tamanio()):
    entrenador = entrenadores.obtener_elemento(i)
    poke_lista = entrenador['Pokemones']
    if (entrenador['Torneos']>3):
        print(entrenador['Nombre'],'ha ganado', entrenador['Torneos'], 'torneos.')
    if entrenador['Torneos']>may_torneos['Torneos']:
        may_torneos = entrenador
    if (entrenador['Ganadas']*100//(entrenador['Perdidas']+entrenador['Ganadas']) > 79):
        entrenadores_79.insertar(entrenador, 'Nombre')
    for j in range (poke_lista.tamanio()):
        pokemon = poke_lista.obtener_elemento(j)
        if ((pokemon['Tipo'] == 'Fuego' and pokemon['Subtipo']== 'Planta') or (pokemon['Tipo'] == 'Agua' and pokemon['Subtipo']== 'Volador')):
            lista_tipos.insertar(entrenador, 'Nombre')


print()

# Punto c
poke_lista = may_torneos['Pokemones']
may_nivel = poke_lista.obtener_elemento(0)
for i in range(poke_lista.tamanio()):
    if (poke_lista.obtener_elemento(i)['Nivel'] > may_nivel['Nivel']):
        may_nivel = poke_lista.obtener_elemento(i)

print('El pokemon de mayor nivel de', may_torneos['Nombre'], 'es', may_nivel['Nombre'])
print()

# Punto d
entr = input('Ingrese el nombre del entrenador para mostrar sus datos y Pokemon: ').capitalize()
pos = entrenadores.busqueda(entr, 'Nombre')
if (pos != -1):
    mostrar_datos(entrenadores, pos)
print()

# Punto e
print('Entrenadores cuyo porcentaje de batallas ganadas es mayor al 79%:')
for i in range(entrenadores_79.tamanio()):
    print(entrenadores_79.obtener_elemento(i)['Nombre'])
print()

# Punto f
print('Entrenadores que tienen Pokemon de tipo fuego/planta o agua/volador:')
for i in range(lista_tipos.tamanio()):
    print(lista_tipos.obtener_elemento(i)['Nombre'])
print()

# Punto g
def promedio_nivel (lista_pokemon):
    """Calcula el promedio de nivel de los pokemones en una lista de pokemones dada."""
    total_niveles = 0
    for i in range (lista_pokemon.tamanio()):
        total_niveles += lista_pokemon.obtener_elemento(i)['Nivel']
    return total_niveles/lista_pokemon.tamanio()

entr = input('Ingrese el nombre del entrenador para calcular el promedio de nivel de sus Pokemon: ').capitalize()
pos = entrenadores.busqueda(entr, 'Nombre')
if (pos != -1):
    promedio = round(promedio_nivel(entrenadores.obtener_elemento(pos)['Pokemones']),2)
    print('El promedio de nivel de los Pokemon de', entr, 'es:', promedio)
print()

# Punto h
def entrenadores_pokemon (pokemon, lista):
    """Determina cuantos entrenadores tienen a un determinado pokemon."""
    cantidad_entrenadores = 0
    for i in range (lista.tamanio()):
        pos = lista.obtener_elemento(i)['Pokemones'].busqueda(pokemon, 'Nombre')
        if (pos != -1):
            cantidad_entrenadores += 1
    return cantidad_entrenadores

poke = input('Ingrese el nombre del Pokemon para determinar cuantos entrenadores lo tienen: ').capitalize()
print (entrenadores_pokemon(poke, entrenadores), 'entrenador(es) tiene(n) a', poke)
print()

# Punto j
print('Los entrenadores que tienen un Tyrantrum, Terrakion o Wingull son:')
for i in range(entrenadores.tamanio()):
    entrenador =  entrenadores.obtener_elemento(i)
    lista_pokemones = entrenador['Pokemones']
    for j in range(lista_pokemones.tamanio()):
        if (lista_pokemones.obtener_elemento(j)['Nombre'] == 'Tyrantrum' or 
            lista_pokemones.obtener_elemento(j)['Nombre'] == 'Terrakion' or 
            lista_pokemones.obtener_elemento(j)['Nombre'] == 'Wingull'):
            print(entrenador['Nombre'])
print()
        
# Punto k
ent = input('Ingrese el nombre del entrenador para saber si tiene a un Pokemon: ').capitalize()
pos = entrenadores.busqueda(ent, 'Nombre')
if pos != -1:
    poke = input('Ingrese el nombre del pokemon: ').capitalize()
    pos2 = entrenadores.obtener_elemento(pos)['Pokemones'].busqueda(poke, 'Nombre')
    if pos2 != -1:
        print(ent, 'tiene a', poke)
        entrenador = entrenadores.obtener_elemento(pos)
        print(ent, '| Torneos Ganados:', entrenador['Torneos'], '| Batallas perdidas:', entrenador['Perdidas'], '| Batallas ganadas:', entrenador['Ganadas'])
        pokemon = entrenadores.obtener_elemento(pos)['Pokemones'].obtener_elemento(pos2)
        print (poke, '| Nivel:', pokemon['Nivel'], '| Tipo:', pokemon['Tipo'], '| Subtipo:', pokemon['Subtipo'])
    else:
        print(ent, 'no tiene a', poke)
else:
    print ('No existe entrenador con ese nombre.')
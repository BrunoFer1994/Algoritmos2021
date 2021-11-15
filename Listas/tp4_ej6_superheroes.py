from lista import Lista

datos = [
    {'nombre':'Wolverine','año_aparicion': 1974, 'editorial' : 'Marvel', 'biografia': 'biografia wolverine'},
    {'nombre':'Batman','año_aparicion': 1939, 'editorial' : 'DC', 'biografia': 'biografia batman traje'},
    {'nombre':'Dr. Strange','año_aparicion': 1963, 'editorial' : 'MRVL', 'biografia': 'biografia dr. strange'},
    {'nombre':'Linterna Verde','año_aparicion': 1940, 'editorial' : 'DC', 'biografia': 'biografia linterna verde'},
    {'nombre':'Mujer Maravilla','año_aparicion': 1941, 'editorial' : 'DC', 'biografia': 'biografia wonder woman'},
    {'nombre':'Flash','año_aparicion': 1940, 'editorial' : 'DC', 'biografia': 'biografia flash'},
    {'nombre':'Starfire','año_aparicion': 1980, 'editorial' : 'DC', 'biografia': 'biografia starfire'},
    {'nombre':'Capitana Marvel','año_aparicion': 1967, 'editorial' : 'Marvel', 'biografia': 'biografia cap marvel'},
    {'nombre':'Scarlet Witch','año_aparicion': 1964, 'editorial' : 'Marvel', 'biografia': 'biografia scarlet witch'},
    {'nombre':'Star-Lord','año_aparicion': 1976, 'editorial' : 'Marvel', 'biografia': 'biografia star lord armadura'},
]

def mostrar_datos (lista, pos):
    print ('Nombre:', lista.obtener_elemento(pos)['nombre'])
    print ('Año de aparición:', lista.obtener_elemento(pos)['año_aparicion'])
    print ('Editorial:', lista.obtener_elemento(pos)['editorial'])
    print ('Biografía:', lista.obtener_elemento(pos)['biografia'])
    print ()

lista_personajes = Lista()

for personaje in datos:
    lista_personajes.insertar(personaje, 'nombre')

# Punto a
buscado = lista_personajes.busqueda('Linterna Verde', 'nombre')
if (buscado != -1):
    lista_personajes.eliminar(lista_personajes.obtener_elemento(buscado)['nombre'], 'nombre')

# Punto b
buscado = lista_personajes.busqueda('Wolverine', 'nombre')
if (buscado != -1):
    print('Wolverine aparecio en el año: ', lista_personajes.obtener_elemento(buscado)['año_aparicion'])

# Punto c
buscado = lista_personajes.busqueda('Dr. Strange', 'nombre')
if (buscado != -1):
    lista_personajes.obtener_elemento(buscado)['editorial'] = 'Marvel'

# Punto d
print('Superheroes cuya biografia contiene la palabra "traje" o "armadura":')

for i in range(lista_personajes.tamanio()):
    personaje = lista_personajes.obtener_elemento(i)
    if ('traje' in personaje['biografia']
        or 'armadura' in personaje['biografia']):
        print(personaje['nombre'])
print()

# Punto e
print('Superheores cuya fecha de aparicion es anterior a 1963:')

for i in range (lista_personajes.tamanio()):
    personaje = lista_personajes.obtener_elemento(i)
    if personaje['año_aparicion'] < 1963:
        print(personaje['nombre'], '-', personaje['año_aparicion'])
print()

# Punto f
def mostrar_casa (lista, personaje):
    """Muestra la editorial del personaje dado."""
    pos = lista.busqueda(personaje, 'nombre')
    if pos != -1:
        print ('La editorial de', personaje, 'es', lista.obtener_elemento(pos)['editorial'])

mostrar_casa(lista_personajes, 'Capitana Marvel')
mostrar_casa(lista_personajes, 'Mujer Maravilla')
print()

# Punto g
buscado = lista_personajes.busqueda('Flash', 'nombre')
if buscado != -1:
    mostrar_datos(lista_personajes, buscado)

buscado = lista_personajes.busqueda('Star-Lord', 'nombre')
if buscado != -1:
    mostrar_datos(lista_personajes, buscado)

# Punto h y Punto i
cont_Marvel = 0
cont_DC = 0
print('Superheroes cuyo nombre comienza con B, M, o S')
for i in range(lista_personajes.tamanio()):
    personaje = lista_personajes.obtener_elemento(i)
    if (personaje['nombre'][0] == 'B' or personaje['nombre'][0] == 'M' or personaje['nombre'][0] == 'S'):
        print(personaje['nombre'])
    if (personaje['editorial'] == 'Marvel'):
        cont_Marvel += 1
    else:
        cont_DC += 1
print()
print('Cantidad de superheroes de DC:', cont_DC)
print('Cantidad de superheroes de Marvel:', cont_Marvel)
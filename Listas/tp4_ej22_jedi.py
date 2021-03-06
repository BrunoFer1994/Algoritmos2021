from lista import Lista

lista_jedis = Lista()
lista_especie = Lista()

file = open('Listas/jedis.txt', encoding="utf8")
lineas = file.readlines()
lineas.pop(0)
for linea in lineas:
    jedi = linea.split(';')
    jedi_data = {}
    jedi_data['name'] = jedi[0].title()
    jedi_data['rank'] = jedi[1].title()
    jedi_data['species'] = jedi[2]
    jedi_data['master'] = jedi[3].title().split('/')
    jedi_data['lightsaber_color'] = jedi[4].split('/')
    jedi_data['homeworld'] = jedi[5].title()
    jedi_data['birth_year'] = jedi[6]
    jedi_data['height'] = float(jedi[7].split('\n')[0])
    if len(jedi) > 8:
        jedi_data['to_darkside'] = jedi[8]
        jedi_data['come_lightside'] =jedi[9]
    lista_jedis.insertar(jedi_data, 'name')
    lista_especie.insertar(jedi_data, 'species')


def mostrar_elemento (lista, pos):
    jedi = lista.obtener_elemento(pos)
    print('• Nombre:', jedi['name'], ' | Rango:', jedi['rank'], ' | Especie:', jedi['species'], ' | Maestro(s):', jedi['master'])
    print ('  Color de sable de luz:', jedi['lightsaber_color'], ' | Planeta natal:', jedi['homeworld'], ' | Año de nacimiento:', jedi['birth_year'], ' | Altura:', jedi['height'])


print() 

# Punto a
print('Listado ordenado por nombre:')
for i in range(lista_jedis.tamanio()):
    mostrar_elemento(lista_jedis, i)

print()

print('Listado ordenado por especie:')
for i in range(lista_especie.tamanio()):
    mostrar_elemento(lista_especie, i)

# Punto b
print('Información de Ahsoka Tano y Kit Fisto')
pos = lista_jedis.busqueda('Ahsoka Tano', 'name')
if pos != -1:
    mostrar_elemento(lista_jedis, pos)

pos = lista_jedis.busqueda('Kit Fisto', 'name')
if pos != -1:
    mostrar_elemento(lista_jedis, pos)

# Punto c
print('Padawans de Luke Skywalker y Yoda:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if ('Luke Skywalker' in jedi['master'] or 'Yoda' in jedi['master']):
        print(jedi['name'], '- Master(s):', jedi['master'])
print()

# Punto d
print("Jedi de especie humana y twi'lek")
for i in range(lista_especie.tamanio()):
    jedi = lista_especie.obtener_elemento(i)
    if (jedi['species']=='human' or jedi['species'] == "twi'lek"):
        mostrar_elemento(lista_especie, i)

print()

# Punto e
print('Jedi que comienzan con A:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if jedi['name'][0]=='A':
        print(jedi['name'])
print()

# Punto f
print('Jedi que usaron sable de mas de un color:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if len(jedi['lightsaber_color'])>1:
        print(jedi['name'], ' - Colores:', jedi['lightsaber_color'])
print()

# Punto g
print('Jedis que usaron un sable de luz amarillo o violeta:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if 'yellow' in jedi['lightsaber_color'] or 'purple' in jedi['lightsaber_color']:
        print(jedi['name'])

print()

# Punto h
print('Padawans de Qui-Gon Jin y Mace Windu:')
for i in range (lista_jedis.tamanio()):
    jedi = lista_jedis.obtener_elemento(i)
    if ('Qui-Gon Jin' in jedi['master'] or 'Mace Windu' in jedi['master']):
        print(jedi['name'], '- Master(s):', jedi['master'])
print()
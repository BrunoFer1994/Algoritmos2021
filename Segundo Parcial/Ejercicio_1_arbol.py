from arbol import Arbol

# Punto 1 y 9: almacenar los datos de los distintos dinosaurios que hay en la isla / al menos 15 elementos
datos = [
    {'nombre':'Velociraptor', 'código': 89, 'ubicación': '7A'},
    {'nombre':'T-Rex', 'código': 539, 'ubicación': '7C'},
    {'nombre':'Diplodocus', 'código': 20211, 'ubicación': '9T'},
    {'nombre':'Triceratops', 'código': 4863, 'ubicación': '9E'},
    {'nombre':'Apatosaurio', 'código': 792, 'ubicación': '3M'},
    {'nombre':'Tecodontosaurio', 'código': 951, 'ubicación': '5R'},
    {'nombre':'Pterodáctilo', 'código': 861, 'ubicación': '4U'},
    {'nombre':'Sgimoloch', 'código': 8631, 'ubicación': '1H'},
    {'nombre':'Raptor', 'código': 71829, 'ubicación': '4X'},
    {'nombre':'Diplodocus', 'código': 71854, 'ubicación': '4E'},
    {'nombre':'Arqueopterix', 'código': 94333, 'ubicación': '8W'},
    {'nombre':'Gallimimo', 'código': 85621, 'ubicación': '4U'},
    {'nombre':'Amargasaurio', 'código': 9877, 'ubicación': '1H'},
    {'nombre':'Diplodocus', 'código': 36415, 'ubicación': '4X'},
    {'nombre':'Diplodocus', 'código': 21583, 'ubicación': '7Q'},
]

arbol_ordnombre = Arbol()
arbol_ordcodigo = Arbol()

# Punto 2: se deben almacenar los datos en dos arboles uno ordenado por nombre y otro por código;
for dinosaurio in datos:
    arbol_ordnombre = arbol_ordnombre.insertar_nodo(dinosaurio['nombre'], dinosaurio)

print('Nombre de los dinosaurios ordenados alfabeticamente:')
arbol_ordnombre.inorden()
print()

for codigos in datos:
    arbol_ordcodigo = arbol_ordcodigo.insertar_nodo(codigos['código'], codigos)

print('Dinosaurios ordenados por codigos:')
arbol_ordcodigo.inorden()
print()

# Punto 3: realizar un barrido en orden del árbol ordenado por nombre;
print('Barrido en orden del árbol ordenado por nombre:')
arbol_ordnombre.inorden_nombre()
print()

# Punto 4: mostrar toda la información del dinosaurio 00792
print('La informacion del dinosaurio 792 es: ')
pos = arbol_ordcodigo.busqueda(792)
if pos:
    print('Nombre: ', pos.datos['nombre'], ' - Código: ', pos.datos['código'], ' - Ubicación: ', pos.datos['ubicación'])
print()

# Punto 5: mostrar toda la información de todos los T-Rex que hay en la isla
print('Informacion sobre el T-Rex:')
arbol_ordnombre.mostrar_informacion('T-Rex')
print()

# Punto 6: modificar el nombre del dinosaurio en Sgimoloch en ambos arboles porque esta mal cargado, su nombre correcto es Stygimoloch;
print('Nombre del dinosaurio Sgimoloch actualizado: ')
buscado = 'Sgimoloch'
pos = arbol_ordnombre.busqueda(buscado)
if(pos):
    nuevo_nombre = 'Stygimoloch'
    nombre, datos = arbol_ordnombre.eliminar_nodo(buscado)
    datos['nombre'] = nuevo_nombre
    arbol_ordnombre = arbol_ordnombre.insertar_nodo(nuevo_nombre, datos)
arbol_ordnombre.inorden()
print()

# Punto 7: mostrar la ubicación de todos los Raptores que hay en la isla
print('La ubicacion de los Raptores son:')
arbol_ordnombre.informacion_raptores('Raptor')
print()

# Punto 8: contar cuantos Diplodocus hay en el parque
print('En el arbol hay', arbol_ordnombre.contar_nodos('Diplodocus'), 'Diplodocus.')
print()
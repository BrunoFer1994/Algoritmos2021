from lista import Lista
from random import randint

lista_vocales = Lista()
lista_num = Lista()
lista_par = Lista()
lista_impar = Lista()
lista_personas = Lista()
lista_uno = Lista()
lista_dos = Lista()

for i in range(5):
    lista_uno.insertar(i)
    lista_dos.insertar(randint(1,10))

print('lista uno')
lista_uno.barrido()
print()
print('lista dos')
lista_dos.barrido()
print()

for i in range(lista_dos.tamanio()):
    num = lista_dos.obtener_elemento(i)
    if(lista_uno.busqueda(num) == -1):
        lista_uno.insertar(num)

lista_uno.barrido()


for i in range(20):
    lista_num.insertar(randint(1,999))

# lista_num.barrido()
# while(not lista_num.lista_vacia()):
#     print(lista_num.eliminar(lista_num.obtener_elemento(0)))

for i in range(lista_num.tamanio()):
    num = lista_num.obtener_elemento(i)
    if(num % 2 == 0):
        lista_par.insertar(num)
    else:
        lista_impar.insertar(num)

print('lista par')
lista_par.barrido()
print()
print('lista impar')
lista_impar.barrido()



for i in range(50):
    vocal = chr(randint(65, 90))
    lista_vocales.insertar(vocal)

lista_vocales.barrido()

vocales = ['A', 'E', 'I', 'O', 'U']

for vocal in vocales:
    aux = lista_vocales.eliminar(vocal)
    while(aux is not None):
        aux = lista_vocales.eliminar(vocal)

# lista_vocales.barrido_eliminando(vocales)
print()
lista_vocales.barrido()

datos = [
    {'name':'juan','edad': 34, 'provincia' : 'chaco', 'dni': 32, 'autos': Lista()},
    {'name':'juan','edad': 80, 'provincia' : 'misiones', 'dni': 20, 'autos': Lista()},
    {'name':'maria','edad': 18, 'provincia' : 'entre rios', 'dni': 28, 'autos': Lista()},
    {'name':'julieta','edad': 18, 'provincia' : 'catamarca', 'dni': 45, 'autos': Lista()},
    {'name':'carlos','edad': 40, 'provincia' : 'entre rios', 'dni': 38, 'autos': Lista()},

]

for i in range(10):
    persona = {}
    persona['name'] = input('ingrese nombre ')
    persona['edad'] = int(input('ingrese edad '))
    # faltan campos
    lista_personas.insertar(persona, 'name')

for persona in datos:
    lista_personas.insertar(persona, 'name')

auto1 = {'modelo': 2020, 'marca': 'fiat', 'patente': 'abc123'}
auto2 = {'modelo': 2020, 'marca': 'ford', 'patente': 'abc456'}
auto3 = {'modelo': 2020, 'marca': 'ford', 'patente': 'abc789'}

pos = lista_personas.busqueda('maria', 'name', 28, 'dni')
if(pos != -1):
    lista_personas.obtener_elemento(pos)['autos'].insertar(auto1, 'marca')
    lista_personas.obtener_elemento(pos)['autos'].insertar(auto2, 'marca')
    lista_personas.obtener_elemento(pos)['autos'].insertar(auto3, 'marca')

pos_auto = lista_personas.obtener_elemento(pos)['autos'].busqueda('ford', 'marca', 'abc789', 'patente')
if(pos_auto != -1):
    lista_personas.obtener_elemento(pos)['autos'].obtener_elemento(pos_auto)['modelo'] = 2013

lista_personas.barrido_lista_autos()


print('elemento eliminado', lista_personas.eliminar('juan', 'name', 38, 'dni'))
print()
lista_personas.barrido()

print()
pos = lista_personas.busqueda(18, 'edad', 'catamarca', 'provincia')
print(lista_personas.obtener_elemento(pos))

for i in range(0, 10):
    lista_num.insertar(randint(0, 100))

lista_num.barrido()
print()
numero = int(input('ingrese valor a buscar '))
print(lista_num.busqueda(numero))


lista_num.modificar_elemento(pos, 43)
print()
numero = int(input('ingrese valor a eliminar '))
print(lista_num.eliminar(numero))
print()
lista_num.barrido()
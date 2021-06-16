from cola import Cola
from pila import Pila

class Notificaciones(object):

    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje

    def __str__(self):
        return self.hora + ' - ' + self.aplicacion + ' - ' + self.mensaje

cola = Cola()
pila = Pila()

smartphone = Notificaciones('18:00', 'Facebook', 'Te interesa mi auto?')
cola.arribo(smartphone)
smartphone = Notificaciones('10:00', 'Twitter', 'Rindiendo python')
cola.arribo(smartphone)
smartphone = Notificaciones('13:00', 'Instagram', 'Juan publico una foto')
cola.arribo(smartphone)
smartphone = Notificaciones('20:00', 'Instagram','A Maria le gusto tu foto')
cola.arribo(smartphone)
smartphone = Notificaciones('02:00', 'Twitter', 'No llegooo')
cola.arribo(smartphone)
smartphone = Notificaciones('12:00', 'Facebook', 'Te agregaron al grupo python 2021')
cola.arribo(smartphone)
smartphone = Notificaciones('23:00', 'Twitter','Ejercicio numero 2')
cola.arribo(smartphone)

print('Las notificaciones en el smartphone son: ')
for i in range(cola.tamanio()):
    print(cola.mover_final())
print('\n')

while(not cola.cola_vacia()):
    X = cola.atencion()

    # c
    if(X.aplicacion == 'Facebook'):
        cola.atencion()
        print('Las notificaciones de Facebook que se eliminaron de la cola pricipal son:\n', X.hora + ' - ' + X.aplicacion + ' - ' + X.mensaje)

    # d
    if(X.aplicacion == 'Twitter'):
        if 'python' in X.mensaje:
            print('Las notificaciones de twitter con "python" en el mensaje son:\n', X.hora + ' - ' + X.aplicacion + ' - ' + X.mensaje)
    # e
    if (X.aplicacion == 'Instagram'):
        pila.apilar(X)
        print('Las notificaciones de Instagram son:\n', X.hora + ' - ' + X.aplicacion + ' - ' + X.mensaje)
        pila.desapilar()
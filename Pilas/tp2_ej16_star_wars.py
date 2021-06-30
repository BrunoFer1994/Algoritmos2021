"""16. Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire strikes back” y la otra los del episodio VII “The force awakens”. 
Desarrollar un algoritmo que permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios."""



from pila import Pila
from random import randint


def buscar(personaje):
    x = False
    while (pila_aux1):
        d = pila_aux1.desapilar()
        if (personaje == d):
            x = True
        pila_aux2.apilar(d)

    while (pila_aux2):
        pila_aux1.apilar(pila_aux2.desapilar())
    
    return x

episodio_v = Pila()
personajes_v = ('LukeSkywalker', 'HanSolo','Chewbacca','PrincesaLeia')
episodio_vii = Pila()
personajes_vii = ('KyloRen','BB8','PrincesaLeia','LukeSkywalker')
mismos_actores = ()
pila_aux1 = Pila()
pila_aux2 = Pila()

# for i in range (0,3):
#     perosnajes1 = personajes_v[i]
#     personajes2 = personajes_vii[i]

#     personajes_v.apilar(perosnajes1)
#     personajes_vii.apilar(personajes2)

while (not personajes_v.pila_vacia()):
    aux = episodio_v.desapilar()
    while (not personajes_vii.pila_vacia()):
        aux2 = personajes_vii.desapilar()
        if (aux == aux2):
            mismos_actores.apilar(personajes_v.desapilar())
        aux.apilar(aux2)

    while (not aux.pila_vacia()):
        aux2.desapilar()
        personajes_vii.apilar(aux2)



# while(not ep5.pila_llena()):
#     x = desapilar(ep5)
#     while(not ep7.pila_llena()):
#         xaux = desapilar(ep7)
#         if(x == xaux):

#             print(x)
#         apilar(paux, xaux)
#     while(not pila_vacia(paux)):
#         xaux = desapilar(paux)
#         apilar(ep7, xaux)
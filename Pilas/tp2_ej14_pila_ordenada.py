"""14. Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden ordenados de forma creciente. Solo puede utilizar una pila auxiliar como estructura extra 
–no sepueden utilizar métodos de ordenamiento–."""


from pila import Pila

pila_principal = Pila()
pila_aux = Pila()
cantidad = int(0)

for i in range (0,100):
    elemento = str(input('Ingrese el elemento que desea apilar o "fin" para terminar: '))
    if (elemento != 'fin'):
        if pila_principal.pila_vacia() or (elemento >= pila_principal.elemento_cima()):
            pila_principal.apilar(elemento)
        else:
            while (not pila_principal.pila_vacia() and elemento < pila_principal.elemento_cima()):
                pila_aux.apilar(pila_principal.desapilar())
            pila_principal.apilar(elemento)
            while (not pila_aux.pila_vacia()):
                pila_principal.apilar(pila_aux.desapilar())
                if (elemento != 'fin'):
                    cantidad += 1
    else:
        break
        
print('\nLa pila ingresada y ordenada es: ')
pila_principal.print_pila()
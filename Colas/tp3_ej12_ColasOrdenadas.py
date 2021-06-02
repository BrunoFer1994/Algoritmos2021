"""12. Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una nueva cola. 
Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar, ni métodos de ordenamiento."""

from cola import Cola

cola1 = Cola()
cola2 = Cola()

cola1.arribo(1)
cola1.arribo(3)
cola1.arribo(5)
cola1.arribo(7)
cola2.arribo(2)
cola2.arribo(4)
cola2.arribo(6)
cola2.arribo(8)

print('La cola 1 ordenada es: ')
cola1.print_cola()
print('\n')
print('La cola 2 ordenada es: ')
cola2.print_cola()
print('\n')

cant = cola1.tamanio()
for i in range (0, cant):
    if(cola1.en_frente() < cola2.en_frente()):
        cola1.mover_final()
    else:
        while (cola1.en_frente() > cola2.en_frente()):
            dato = cola2.atencion()
            cola1.arribo(dato)
        cola1.mover_final()
while(not cola2.cola_vacia()):
    dato = cola2.atencion()
    cola1.arribo(dato)

print('Ambas colas concatenadas y ordenadas: ')
cola1.print_cola()
def sumaRec (numero):
    if(numero == 0 or numero == 1):
        return numero
    else:
        return numero + sumaRec(numero-1)

print(sumaRec(8))
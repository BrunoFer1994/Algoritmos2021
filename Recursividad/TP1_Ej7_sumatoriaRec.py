def sumatoriaRec (numero):
    if(numero == 1):
        return 1
    else:
        return 1/numero + sumatoriaRec(numero-1)

print(sumatoriaRec(3))
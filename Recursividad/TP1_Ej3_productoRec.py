def productoRec (numero1,numero2):
    if (numero2 == 1):
        return numero1
    else:
        return numero1 + productoRec(numero1,numero2 - 1)

print(productoRec(2,8))
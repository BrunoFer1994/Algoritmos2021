def producto (numero1,numero2):
    if (numero2 == 1):
        return numero1
    else:
        print(numero1,numero2)
        return numero1 + producto(numero1,numero2 - 1)

print(producto(2,3))
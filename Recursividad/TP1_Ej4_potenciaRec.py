def potenciaRec (base,exp):
    if (exp == 0):
        return 1
    else:
        return base * potenciaRec(base,exp - 1)

base = int(input("\nIngrese la base: "))
exp = int(input("\nIngrese el exponente: "))

print("La potencia entre " + str(base) + " y " + str(exp) + " es " + str(potenciaRec (base,exp)))
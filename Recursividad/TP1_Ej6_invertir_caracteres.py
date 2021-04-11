def invertir_caracteres(texto):
    if (len(texto) == 0):
        return texto
    else:
        return invertir_caracteres(texto[1:]) + texto[0]

print("secuencia invertida: " + str(invertir_caracteres('hola y chau')))
#! Estructuras de datos simples - Vectores y matrices

vector = [1,2,3,4,5]

for i in range(0,5):
    print(vector[i])


#matriz = [[1,1,1],[2,2,2][3,3,3]]

for numero in matriz:
    print(numero)


#! invertir cadena
def invertir_cadena(cadena):
    if(len(cadena) == 0):
        return ""
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])
print (invertir_cadena("hola mundo"))

#! ejercicio 11
print(791 // 10)


#cortar vector - slicing

print(matriz[1:4])
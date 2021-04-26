datos = [11, 3, 81, 7, 45, 20, 4, 5, 10, 25, 30, 22]

def quicksort(vector, inicio, fin):
    primero = inicio
    ultimo = fin -1
    pivote = fin
    while(primero < ultimo):
        while(vector[primero]<vector[pivote] and primero <= ultimo):
            primero += 1
        while(vector[ultimo]>vector[pivote] and ultimo >= primero):
            ultimo -= 1
        
        if(primero < ultimo):
            vector[primero], vector[ultimo] = vector[ultimo], vector[primero]
    if(vector[pivote]<vector[primero]):
        vector[primero], vector[pivote] = vector[pivote], vector[primero]

    if(inicio < primero):
        quicksort(vector, inicio, primero -1)
    if(fin > primero):
        quicksort(vector, primero + 1, fin)

def busqueda_binaria(vector, buscado, inicio, fin):
    if(inicio<= fin):
        medio = (inicio + fin) // 2
        if(vector[medio] == buscado):
            return medio
        elif(vector[medio] < buscado):
            return busqueda_binaria(vector, buscado, medio+1, fin)
        else:
            return busqueda_binaria(vector, buscado, inicio, medio-1)
    else:
        return "El numero ingresado no se encuentra el la lista."


quicksort(datos,0, len(datos)-1)
print(datos)
numero = float(input("Ingrese el numero que desea buscar el la lista Datos: "))
print("El numero ingresado esta en la posicion: ", busqueda_binaria(datos, numero, 0, len(datos)-1))
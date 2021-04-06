def sumatoria(numero):
    if(numero == 1):
        return 1
    else:
        return 1/numero + sumatoria(numero-1)

print(sumatoria(3))
def laberinto(matriz, x, y, caminos=[]):
    if(x >= 0 and x <= len(matriz) - 1) and (y >= 0 and y <= len(matriz[0]) - 1):
        if (matriz[x][y] == 2):
            caminos.append([x, y])
            print('Saliste del laberinto.')
            print(caminos)
            caminos.pop()
        elif(matriz[x][y] == 1):
            matriz[x][y] = 3
            caminos.append([x, y])
            laberinto(matriz, x, y+1, caminos)
            laberinto(matriz, x, y-1, caminos)
            laberinto(matriz, x-1, y, caminos)
            laberinto(matriz, x+1, y, caminos)
            caminos.pop()
            matriz[x][y] = 1

lab = [[1,1,1,1,1,1,1],
       [0,0,0,0,1,0,1],
       [1,1,1,0,1,0,1],
       [1,0,1,1,1,1,1],
       [1,0,0,0,0,0,0],
       [1,1,1,1,1,1,2]]

laberinto(lab, 0, 0, )
datos = [1,2,3,4,5,6,7,8,9]
mochila = ['pan', 'capa', 'sable de luz','otro']

def usar_fuerza(mochila,pos):
    if(pos < len(mochila)):
        if(mochila[pos] == 'sable de luz'):
            return pos
        else:
            return usar_fuerza(mochila,pos+1)
    else:
        return -1

print (usar_fuerza(mochila,2))




def barrido(vector):
    if(len(vector)>0):
        print (vector[0])
        barrido(vector[1:])

barrido (datos)
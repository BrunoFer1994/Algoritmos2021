mochila = ['Pan','Capa','Sable de luz','Otro']

def usar_fuerza(mochila, pos):
    if(pos < len(mochila) - 1):
        if(mochila[pos] == 'Sable de luz'):
            return pos
        else:
            return usar_fuerza(mochila, pos + 1)
    else:
        return -1

print(usar_fuerza(mochila,2))
def siguiente(life,pocicion):
    siguiente = []
    for f in range(len(life)):
        fila = []
        for c in range(len(life[0])):
            fila.append(disparo(life,f,c,pocicion))
        siguiente.append(fila)
    return siguiente

def disparo(life,f,c,pocicion):

    for x in range(len(pocicion)):

        fi=(pocicion[x][0])-1
        co=(pocicion[x][1])-1
        if f == fi and c == co:
            return '.'
    return life[f][c]


def pedro(mapa,posicionesDeDisparosDePrueba):
    list = []
    for x in range(1, len(mapa)):
        if len(mapa[x - 1]) != len(mapa[x]):
            return list
    lista = []
    lista = siguiente(mapa,posicionesDeDisparosDePrueba)
    posicionesDeBarcosVivos= []
    for f in range(len(lista)):
        li = ()
        for c in range(len(lista[0])):
            if lista[f][c]=='b':
                li = (f+1,c+1)
            if li!=[] and len(li)==2:
                posicionesDeBarcosVivos.append(li)
                li = []
    return posicionesDeBarcosVivos
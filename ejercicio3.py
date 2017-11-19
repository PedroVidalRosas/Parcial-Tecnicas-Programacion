def soloNombres(tupla):
    equipos = []
    for x in range(len(tupla)):
        equipos.append(tupla[x][0])
    lista=[]
    for x in sorted(set(equipos)):
        lista.append(x)
    return (lista[0])

def siSonIguales(tupla):
    lista = []
    lista = primerempaque(tupla)
    lista = segundoEmpaque(lista)
    for x in range(1,len(lista)):
        if lista[x-1][1]==lista[x][1]:
            continue
        else:
            return False
    return True

def primerempaque(tupla):
    lista = []
    for x in range(len(tupla)):
        listaAux = []
        for y in range(1, len(tupla[0]), 2):
            listaAux.append(tupla[x][y - 1])
            listaAux.append(tupla[x][y])

        lista.append(listaAux)
    return lista

def segundoEmpaque(lista):
    equipos = []
    for x in range(len(lista)):
        listaAux = []
        for y in range(0, len(lista[0])):
            listaAux = []
            if type(lista[x][y]) == int:
                listaAux.append(lista[x][y - 1])
                listaAux.append(lista[x][y])
            if listaAux != []:
                equipos.append(listaAux)

    return equipos

def calcularGanador(tupla):
    if tupla==[]:
        return ""
    lista =[]
    lista = primerempaque(tupla)
    lista=segundoEmpaque(lista)
    if siSonIguales(lista)==True:
        return soloNombres(lista)

    resul=0
    for x in range(len(lista)):

        for y in range(len(lista)):
            if lista[x][1]>lista[y][1]:
                resul=lista[x]

    resultado = resul[0]
    return resultado
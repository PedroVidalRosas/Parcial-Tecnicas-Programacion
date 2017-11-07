def soloNombres(tupla):
    k = []
    for x in range(len(tupla)):
        k.append(tupla[x][0])
    pedro=[]
    for x in sorted(set(k)):
        pedro.append(x)
    return (pedro[0])

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
        li = []
        for y in range(1, len(tupla[0]), 2):
            li.append(tupla[x][y - 1])
            li.append(tupla[x][y])

        lista.append(li)
    return lista

def segundoEmpaque(lista):
    p = []
    for x in range(len(lista)):
        c = []
        for y in range(0, len(lista[0])):
            c = []
            if type(lista[x][y]) == int:
                c.append(lista[x][y - 1])
                c.append(lista[x][y])
            if c != []:
                p.append(c)

    return p

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
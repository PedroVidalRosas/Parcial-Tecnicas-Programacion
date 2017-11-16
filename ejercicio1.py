def rotar(palabra):
    lista=[]
    try:
        palabraARotar=palabra.split(" ")
        if palabraARotar[0] == '' and palabraARotar[1] == '':
            return lista
    except:
        palabraARotar=0
    if type(palabra)==str and palabra != "":
        listaAuxiliar = list(palabra)
        lista.append(listaAuxiliar)
        for x in range(len(palabra)-1):
            p =lista[x]
            lista1=[]
            for y in range(1,len(palabra)):
                lista1.append(p[y])
            lista1.append(p[0])
            lista.append(lista1)
        listaRotada = []
        for x in range(len(lista)):
            listaRotada.append(''.join(lista[x]))
        return listaRotada
    else:
        return lista

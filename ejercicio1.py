def rotar(palabra):
    lista=[]
    try:
        pepe=palabra.split(" ")
        if pepe[0] == '' and pepe[1] == '':
            return lista
    except:
        pepe=0
    if type(palabra)==str and palabra != "":
        lista2 = list(palabra)
        lista.append(lista2)
        for x in range(len(palabra)-1):
            p =lista[x]
            lista1=[]
            for y in range(1,len(palabra)):
                lista1.append(p[y])
            lista1.append(p[0])
            lista.append(lista1)
        c = []
        for x in range(len(lista)):
            c.append(''.join(lista[x]))
        return c
    else:
        return lista

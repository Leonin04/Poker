def ComprobarMano(mesa,mano):
    if Poker(mesa,mano):
        return "Poker"
    elif Full(mesa,mano):
        return "Full"
    elif Color(mesa,mano):
        return "Color"
    elif Escalera(mesa,mano):
        return "Escalera"
    elif Trio(mesa,mano):
        return "Trio"
    elif DoblePareja(mesa,mano):
        return "Doble Pareja"
    elif Pareja(mesa,mano):
        return "Pareja"
    else:
        return "Carta Alta"
    
    
    pass

def ContarPareja(mesa,mano):
    parejas=0
    contar = mesa.cartas + mano.cartas
    for carta in contar:
        conteo=0
        for carta2 in contar:
            if carta.valor == carta2.valor and carta.figura == carta2.figura:
                conteo+=1
        if conteo == 2:
            parejas+=1
            contar.remove(carta)
    return parejas

def Pareja(mesa,mano):
    if ContarPareja(mesa,mano) == 1:
        return True
    else:
        return False
    
def DoblePareja(mesa,mano):
    if ContarPareja(mesa,mano) == 2:
        return True
    else:
        return False
    
def Trio(mesa,mano):
    for carta in mano.cartas:
        conteo=0
        for carta2 in mesa.cartas:
            if carta.valor == carta2.valor and carta.figura == carta2.figura:
                conteo+=1
        if conteo == 3:
            return True
    else:
        return False
    
def Escalera(mesa,mano):
    comprobarescalera = mesa.cartas + mano.cartas
    comprobarescalera.sort(key=lambda carta: carta.valor)
    if len(comprobarescalera) < 5:
        return False
    
    for i in range(len(comprobarescalera) - 4):
        if (comprobarescalera[i].valor == comprobarescalera[i+1].valor - 1 and
            comprobarescalera[i+1].valor == comprobarescalera[i+2].valor - 1 and
            comprobarescalera[i+2].valor == comprobarescalera[i+3].valor - 1 and
            comprobarescalera[i+3].valor == comprobarescalera[i+4].valor - 1):
            return True
    return False

def Color(mesa,mano):
    comprobarcolor = mesa.cartas + mano.cartas
    if len(comprobarcolor) < 5:
        return False
    
    palos = [0]*4
    for carta in comprobarcolor:
        palos[carta.palotoint()] += 1
    
    for count in palos:
        if count >= 5:
            return True
    return False

def Full(mesa,mano):
    if Trio(mesa,mano) and DoblePareja(mesa,mano):
        return True
    else:
        return False
    
def Poker(mesa,mano):
    for carta in mano.cartas:
        conteo=0
        for carta2 in mesa.cartas:
            if carta.valor == carta2.valor and carta.figura == carta2.figura:
                conteo+=1
        if conteo == 4:
            return True
    else:
        return False


orden = ['Poker','Full','Color','Escalera','Trio','Doble Pareja','Pareja','Carta Alta']

def CheckMano(mesa,mano):
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
    
def ComprobarGanador(mano1,mano2):
    if orden.index(mano1.getMano()) < orden.index(mano2.getMano()):
        return "Gana Jugador 1"
    elif orden.index(mano1.getMano()) > orden.index(mano2.getMano( )):
        return "Gana CPU"

def ContarPareja(mesa, mano):
    manita = (0,0,0)
    contar = mesa.cartas + mano.cartas

    for i in range(len(contar)):
        repeticiones = 1
        for j in range(i+1, len(contar)):
            if contar[i].valor == contar[j].valor and contar[i].figura == contar[j].figura:
                repeticiones += 1
        if repeticiones >= manita[0]:
            manita = (repeticiones, contar[i].valor, manita[2]+1)
    
    print(manita)
    return manita

def Pareja(mesa,mano):
    if ContarPareja(mesa,mano)[0] == 2:
        mano.setPuntuacion(ContarPareja(mesa,mano)[1]*2)
        return True
    else:
        return False
    
def DoblePareja(mesa,mano):
    if ContarPareja(mesa,mano) == 2:
        return True
    else:
        return False
    
def Trio(mesa,mano):
    if ContarPareja(mesa,mano)[0] == 3:
        mano.setPuntuacion(ContarPareja(mesa,mano)[1]*3)
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
    if ContarPareja(mesa,mano)[0] == 4:
        mano.setPuntuacion(ContarPareja(mesa,mano)[1]*4)
        return True
    else:
        return False


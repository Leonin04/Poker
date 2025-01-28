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
        mano.setPuntuacion(max([carta.valor for carta in mano.cartas]))
        return "Carta Alta"
    
def ComprobarGanador(mano1,mano2):
    if orden.index(mano1.getMano()) < orden.index(mano2.getMano()):
        return "Gana Jugador 1"
    elif orden.index(mano1.getMano()) > orden.index(mano2.getMano( )):
        return "Gana CPU"
    else:
        if mano1.getPuntuacion() > mano2.getPuntuacion():
            return "Gana Jugador 1"
        elif mano1.getPuntuacion() < mano2.getPuntuacion():
            return "Gana CPU"

def ContarPareja(mesa, mano):
    figura = []
    valor = []
    repeticiones = []
    cartas = mesa.cartas + mano.cartas
    for i in range(len(cartas)):
        contador = 1
        for j in range(i+1,len(cartas)):
            if figura.count(cartas[i].figura) == 0:
                if cartas[i].figura == cartas[j].figura:
                        figura.append(cartas[i].figura)
                        valor.append(cartas[i].valor)
                        repeticiones.append(1)
                        
            else:
                if cartas[i].figura == cartas[j].figura:
                    repeticiones[figura.index(cartas[i].figura)] += 1

    return figura,valor,repeticiones
                

def Pareja(mesa,mano):
    resultado = ContarPareja(mesa,mano)
    if len(resultado[0]) == 1 and resultado[2][0] == 2:
        mano.setPuntuacion(int(resultado[1][0])*2)
        return True
    else:
        return False
    
def DoblePareja(mesa,mano):
    resultado = ContarPareja(mesa,mano)
    if len(resultado[0]) == 2:
        if resultado[2][0] == resultado[2][1]:
            mano.setPuntuacion(int(resultado[1][0])*2 + int(resultado[1][1])*2)
            return True
    else:
        return False
    
def Trio(mesa,mano):
    resultado = ContarPareja(mesa,mano)
    if len(resultado[0]) == 1 and resultado[2][0] == 3:
        mano.setPuntuacion(int(resultado[1][0])*3)
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
            mano.setPuntuacion(comprobarescalera[i].valor+comprobarescalera[i+1].valor+comprobarescalera[i+2].valor+comprobarescalera[i+3].valor+comprobarescalera[i+4].valor)
            return True
    return False

def Color(mesa,mano):
    comprobarcolor = mesa.cartas + mano.cartas
    comprobarcolor.sort(key=lambda carta: carta.valor)
    if len(comprobarcolor) < 5:
        return False
    palos = [0]*4
    puntos =[0]*4
    for carta in comprobarcolor:
        palos[carta.palotoint()] += 1
        if palos[carta.palotoint()] <= 5:
            puntos[carta.palotoint()] += carta.valor
    
    for count in palos:
        if count >= 5:
            mano.setPuntuacion(puntos[palos.index(count)])
            return True
    return False

def Full(mesa,mano):
    puntuacion = 0
    resultado = ContarPareja(mesa,mano)
    if len(resultado[0]) >= 2:
        if resultado[2].count(3) == 1:
            puntuacion=resultado[1][resultado[2].index(3)]*3
            resultado[1].pop(resultado[2].index(3))
            puntuacion+=max(resultado[1])*2
            mano.setPuntuacion(puntuacion)
            return True
    else:
        return False
    
def Poker(mesa,mano):
    resultado = ContarPareja(mesa,mano)
    if len(resultado[0]) == 1 and resultado[2][0] == 4:
        mano.setPuntuacion(int(resultado[1][0])*4)
        return True
    else:
        return False


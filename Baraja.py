from Cartas import Carta

class Baraja:
    def __init__(self):
        self.palos = ['Picas', 'Corazones', 'Diamantes', 'Tréboles']
        self.cartas = []

        for palo in self.palos:
            for valor in range(2, 11):
                self.cartas.append(Carta(valor, palo))
            for figura in ['J', 'Q', 'K']:
                self.cartas.append(Carta(10, palo, True, figura))
            self.cartas.append(Carta(11, palo))

    def __getitem__(self, index):
        return self.cartas[index]
    
    def __len__(self):
        return len(self.cartas)
        
    def __str__(self):
        return "\n".join(str(carta) for carta in self.cartas)

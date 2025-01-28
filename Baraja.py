from Cartas import Carta

class Baraja:
    def __init__(self):
        self.palos = ['Picas', 'Corazones', 'Diamantes', 'Tréboles']
        self.cartas = []
        self.reiniciarBaraja()
        self.barajar()
       
    def reiniciarBaraja(self):
        self.cartas = []
        for palo in self.palos:
            for valor in range(2, 11):
                self.cartas.append(Carta(valor, palo, valor))
            for figura in ['J', 'Q', 'K']:
                self.cartas.append(Carta(10, palo, figura))
            self.cartas.append(Carta(11, palo, "As"))

    def barajar(self):
        import random
        random.shuffle(self.cartas)

    def sacarCarta(self):
        return self.cartas.pop()

    def __getitem__(self, index):
        return self.cartas[index]
    
    def __len__(self):
        return len(self.cartas)
        
    def __str__(self):
        return "\n".join(str(carta) for carta in self.cartas)

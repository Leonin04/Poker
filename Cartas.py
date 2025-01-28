class Carta:
    def __init__(self, valor, palo, figura=None):
        self.valor = valor
        self.palo = palo
        self.figura = figura
        

    def palotoint(self):
        if self.palo == "Picas":
            return 0
        elif self.palo == "Corazones":
            return 1
        elif self.palo == "Diamantes":
            return 2
        elif self.palo == "Tréboles":
            return 3

    def __str__(self):
        if self.figura:
            return f"{self.figura} de {self.palo}"
        if self.valor == 11:
            return f"As de {self.palo}"
        else:
            return f"{self.valor} de {self.palo}"

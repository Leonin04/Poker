class Carta:
    def __init__(self, valor, palo, esfigura=False, figura=None):
        self.valor = valor
        self.palo = palo
        self.figura = figura
        if esfigura:
            self.figura = figura

    def __str__(self):
        if self.figura:
            return f"{self.figura} de {self.palo}"
        if self.valor == 11:
            return f"As de {self.palo}"
        else:
            return f"{self.valor} de {self.palo}"

class Animal():
    def __init__(self, nome, peso, habitat):
        self.nome = nome
        self.peso = peso
        self.habitat = habitat

    def mover(self):
        print(self.nome + " animal move de forma genérica.")

    def comunicar(self):
        print(self.nome + " animal comunica de forma genérica.")

    def __str__(self):
        return "Animal [nome: %s, peso: %d, habitat: %s]" % (self.nome, self.peso, self.habitat)

class Cachorro(Animal):
    def __init__(self, nome, peso, habitat, raca):
        super(Cachorro, self).__init__(nome, peso, habitat)
        self.raca = raca

    def brincar(self):
        print("Cachorro brincando!")

    def vigiar(self):
        print("Cachorro vigiando.")

    def __str__(self):
        return "Cachorro [nome: %s, peso: %d, habitat: %s, raca: %s]" % (self.nome, self.peso, self.habitat, self.raca)


class Peixe(Animal):
    def __init__(self, nome, peso, habitat, tipoCauda):
        super(Peixe, self).__init__(nome, peso, habitat)
        self.cauda = Cauda(tipoCauda)

    def __str__(self):
        return "Peixe [nome: %s, peso: %d, habitat: %s, Cauda: %s]" % (self.nome, self.peso, self.habitat, self.cauda)

class Cauda():
    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return "Cauda [Cauda: %s]" % (self.tipo)
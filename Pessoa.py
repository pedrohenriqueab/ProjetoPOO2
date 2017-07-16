class Pessoa():
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def __str__(self):
        return "Pessoa [Nome: %s, Idade: %d, Genero: %s]" % (self.nome, self.idade, self.genero)
from Questao2.Pessoa import *
from datetime import *
class Cliente(Pessoa):
    def __init__(self, nome, idade, genero, nascimento):
        super(Pessoa, self).__init__(nome, idade, genero)
        self.nascimento = nascimento.strftime('%d/%m/%Y')

    def __str__(self):
        return "Cliente [Nome: %s, Idade: %d, Genero: %s, Nascimento: %x]" % (self.nome, self.idade, self.genero, self.nascimento)
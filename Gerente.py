from Questao2.Funcionario import *
class Gerente(Funcionario):
    def __init__(self, salario, matricula, nomeGerencia):
        super(Funcionario, self).__init__(salario, matricula)
        self.nomeGerencia = nomeGerencia

    def __str__(self):
        return "Gerente [Nome: %s, salario: %f, matricula: %d]" % (self.nomeGenrencia, self.salario, self.matricula)
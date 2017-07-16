from Questao2.Pessoa import *
class Funcionario(Pessoa):
    def __init__(self, nome, idade, genero, salario, matricula, aux, inss):
        super(Pessoa, self).__init__(nome, idade, genero)
        self.salario = salario
        self.matricula = matricula
        self.aux = aux
        self.inss = inss

    def calcularINSS(self):
        self.aux = self.salario / 0.11
        self.inss = self.salario - self.aux

    def __str__(self):
        return "Funcionario [Nome: %s, Idade: %d, Genero: %s, Salario: %f, Matricula: %d, INSS: %f]" % (self.nome, self.idade, self.genero, self.salario, self.matricula, self.inss)
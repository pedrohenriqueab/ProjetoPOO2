from Questao3.Pessoa import *
class Funcionario(Pessoa):
    def __init__(self, nome, endereco, tel, codigoSetor, salarioBase, imposto)
        super(Pessoa, self).__init__(nome, endereco, tel)
        self.codigoSetor = codigoSetor
        self.salarioBase = salarioBase
        self.imposto = imposto

    def calcularSalarioTotal(self):
        self.salarioTotal = (self.salarioBase - self.imposto)
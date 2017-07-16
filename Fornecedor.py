from Questao3.Pessoa import *
class Fornecedor(Pessoa):
    def __init__(self, nome, endereco, tel, valorCredito, valorDivida):
        super(Pessoa, self).__init__(nome, endereco, tel)
        self.valorCredito = valorCredito
        self.valorDivida = valorDivida
        self.aux = aux

    def obterSaldo(self):
        self.aux = (self.valorDivida - self.valorCredito)
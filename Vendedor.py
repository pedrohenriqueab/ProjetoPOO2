from Questao2.Funcionario import *
class Vendedor(Funcionario):
    def __init__(self, salario, matricula, valorVendas, nome, valor):
        super(Funcionario, self).__init__(salario, matricula)
        self.valorVendas = valorVendas
        self.vendas = Produto(nome, valor)

    class Produto():
        def __init__(self, nome, valor):
            self.nome = nome
            self.valor = valor
'''class Conta:#Criação da classe conta e seus atributos
    def __init__(self,conta,titular,valor):
        self._conta = conta
        self._titular = titular
        self._valor = valor

class TributavelMixin:#Criação de um Mixin e seu metodo
    def get_valor_imposto(self):
        pass

class ContaCorrente(Conta,TributavelMixin):#Criação de classe ContaCorrente que herda atributos de Conta e metodo do Tributavelmixin
    pass
    def get_valor_imposto(self):#Sobrescrevendo o metodo get_valor_imposto (Polimorfismo)
        return self._valor * 0.01
    
class SeguroDeVida(TributavelMixin):#Criação da classe SeguroDeVida e seus atributos que herda metodo do Tributavelmixin
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):#Sobrescrevendo o metodo get_valor_imposto (Polimorfismo)
        return 50 + self._valor * 0.05
    
class ManipuladorDeTributaveis:#Criação de classe ManipuladordeTributaveis
    pass

    def calcula_impostos(self, lista_tributaveis):#recebe uma lista com os tributaveis (Conta corrente e seguro de vida) percorre a lista e armazena na variavel total a soma de todos os valores de imposto, depois retorna total
        total = 0
        for t in lista_tributaveis:
            total += t.get_valor_imposto()
        return total 
    
cc1 = ContaCorrente('123-4', 'João', 1000.0)
cc2 = ContaCorrente('123-4', 'José', 1000.0)
seguro1 = SeguroDeVida(100.0, 'José', '345-77')
seguro2 = SeguroDeVida(200.0, 'Maria', '237-98')
#instanciando objetos apartir das classes seguro de vida e contacorrente
lista_tributaveis = []
lista_tributaveis.append(cc1)
lista_tributaveis.append(cc2)
lista_tributaveis.append(seguro1)
lista_tributaveis.append(seguro2)
#criando lista vazia e posteriormente colocando meus objetos dentro dela
manipulador = ManipuladorDeTributaveis()#instanciando objeto apartir da classe manipulador de tributaveis
print(manipulador.calcula_impostos(lista_tributaveis))#printando a soma de todos os impostos dos meus objetos '''

import abc
class Conta:
    def __init__(self,conta,titular,valor):
        self._conta = conta
        self._titular = titular
        self._valor = valor

class Tributavel(abc.ABC):
    """ Classe que contém operações de um objeto autenticável

    As subclasses concretas devem sobrescrever o método get_valor_imposto.
    """
    @abc.abstractmethod #aplica taxa de imposto sobre um determinado valor do objeto 
    def get_valor_imposto(self,valor):
        pass

class ContaCorrente(Conta):
    pass

    def get_valor_imposto(self):
        return self._valor * 0.01
    
class SeguroDeVida:
    pass

    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05

class ContaInvestimento(Conta):

    def atualiza(self, taxa):
        self._valor += self._valor * taxa * 5

    def get_valor_imposto(self):
        return self._valor * 0.03


class ContaPoupanca:
    def __init__(self,conta,nome):
        self.conta = conta
        self.nome = nome
    def __str__(self):
        return f'Conta Poupança {self.conta}'
class ManipuladorDeTributaveis:
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            if (isinstance(t, Tributavel)): #verifica se e tributavel
                total += t.get_valor_imposto()
            else:
                print(t.__str__(), "não é um tributável")    
        return total   
    
'''Conta Corrente e Seguro de vida agora nao utiliza herança multipla, nesse momento Tributavel funciona como uma interface  indicando quais métodos essas classes precisam ter (Ele indica quais métodos uma classe precisa ter para ser considerada tributável.)'''
Tributavel.register(ContaCorrente)
Tributavel.register(SeguroDeVida)
Tributavel.register(ContaInvestimento)

Contacorrente = ContaCorrente('123-4', 'João', 1000.0)
seguro = SeguroDeVida(100.0, 'José', '345-77')
contapoupanca = ContaPoupanca('123-6', 'Maria')
containvestimento = ContaInvestimento('123-7','Luciene',120)

list = []
list.append(Contacorrente)
list.append(seguro)
list.append(contapoupanca)
list.append(containvestimento)

print(f'Valor de imposto de conta corrente: {Contacorrente.get_valor_imposto()}')
print(f'Valor de imposto de Seguro: {seguro.get_valor_imposto()}')
print(f'Valor de imposto de Seguro: {containvestimento.get_valor_imposto():.2}')
print("*" * 40)
i = ManipuladorDeTributaveis()
print(f'Total de impostos acumulado:{i.calcula_impostos(list)}')
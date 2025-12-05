#1 
class A:
    def metodo(self):
        print("metodo de A")


class B(A):
    def metodo(self):
        print("metodo de B")
        super().metodo()


class C(A):
    def metodo(self):
        print("metodo de C")
        super().metodo()


class D(B, C):
    def metodo(self):
        print("metodo de D")
        super().metodo()
d = D()
d.metodo()



#2

from abc import ABC, abstractmethod

# Interface para um atacante
class Atacante(ABC):
    @abstractmethod
    def chutar_ao_gol(self):
        pass

# Interface para um defensor
class Defensor(ABC):
    @abstractmethod
    def bloquear_chute(self):
        pass

# Interface para um meio-campista
class MeioCampista(ABC):
    @abstractmethod
    def dar_assistencia(self):
        pass
class Goleiro (ABC):
    @abstractmethod
    def defender_penalti(self):
        pass
class Jogador1(Atacante, MeioCampista):
    def chutar_ao_gol(self):
        print("Jogador1 chutou forte no gol!")

    def dar_assistencia(self):
        print("Jogador1 deu uma bela assistência!")

class Jogador2(Defensor, MeioCampista):
    def bloquear_chute(self):
        print("Jogador2 bloqueou o chute!")

    def dar_assistencia(self):
        print("Jogador2 fez um passe incrível!")
class Jogador3(Goleiro,Defensor):
    def bloquear_chute(self):
        print("Jogador3 bloqueou o chute")
    def defender_penalti(self):
        print("Jogador3 defendeu o penalti")


j1 = Jogador1()
j1.chutar_ao_gol()
j1.dar_assistencia()

j2 = Jogador2()
j2.bloquear_chute()
j2.dar_assistencia()

j3 = Jogador3()
j3.bloquear_chute()
j3.defender_penalti()




#3 
class AutenticacaoMixin:
    def verificar_senha(self, senha_digitada):
        if senha_digitada == self.senha:
            print("senha correta!")
        else:
            print("senha incorreta!")


class Usuario(AutenticacaoMixin):
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
x = Usuario('ze',1234)
x.verificar_senha(78)
#4
class Veiculo:
    def mover(self):
        print("Movendo-se.....")

class MotorizadoMixin:
    def ligar_motor(self):
        print("Ligando.....")
class EletricoMixin:
    def carregar_bateria(self):
        print("Carregando.....")
    
class Carro(MotorizadoMixin,Veiculo):
    pass

class CarroEletrico(EletricoMixin,Carro):
    pass

class Bicicleta(Veiculo):
    pass
    


tesla = CarroEletrico()
tesla.ligar_motor()
tesla.carregar_bateria()
tesla.mover()

bike = Bicicleta()
bike.mover()


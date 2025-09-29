''' Questāo 1 – Coleção de Figurinhas
1. Crie a classe Figurinha com os atributos numero e tema (ex.: “Mascote”, “Estádio”).
Método: mostrar() devolve uma frase como: "Figurinha 7 – Mascote" .
2. Crie a classe Pacotinho , que guarda várias Figurinha (use uma lista).
Métodos:
adicionar(figurinha)
listar() (exibe todas as figurinhas)
3. Crie a classe MinhaColecao com uma lista de Figurinha que o aluno já possui.
Métodos:
colar(figurinha) (move do pacotinho para a coleção)
faltantes() (retorna quantas figurinhas ainda não foram coladas se o álbum tem 10 números).'''






class Figurinha:
    def __init__(self,numero,tema):
        self.numero = numero
        self.tema = tema
    def mostrar(self):
        print(f"Figurinha {self.numero} - {self.tema}")

class Pacotinho:
    def __init__(self):
        self.lista = []  # Cria um vetor vazia para a as figurinhas

    def adicionar(self, figurinha):
        self.lista.append(figurinha)  # Adiciona uma figurinha à lista

    def listar(self):
        for n in self.lista:
            n.mostrar()

class Minhacolecao:
    def __init__(self):
        self.colecao = [] # cria um nono vetor para trazer as fig do pacote

    def colar(self, lista): #preenche o novo vetor
        for figurinha in lista: 
            self.colecao.append(figurinha) 

    def faltantes(self): 
     qntd = len(self.colecao)   #qntd vai receber o tamanho do vetor,ou seja a quantidade d figurinhas
     if qntd == 10:
        print("Sua coleção está completa!") 
     elif qntd == 0:
        print("Infelizmente você não tem nenhuma figurinha") 
     elif qntd > 10:
          print("Você tem figurinhas repetidas!")
     else:
        print(f"Faltam {10 - qntd} figurinhas para completar a coleção.")
        
# Exemplo de uso:
# Teste
f1 = Figurinha(1, "Brasil")
f2 = Figurinha(2, "Mascote")
f3 = Figurinha(3, "Estádio")

pacote = Pacotinho()
pacote.adicionar(f1)
pacote.adicionar(f2)
pacote.adicionar(f3)

print("Figurinhas no pacotinho:")
pacote.listar()

colecao = Minhacolecao()
colecao.colar(pacote.lista)

print("Situação da coleção:")
colecao.faltantes()





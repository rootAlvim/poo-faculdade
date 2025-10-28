'''Atividade Abastraçāo
Questāo 1 – Coleção de Figurinhas
1. Crie a classe Figurinha com os atributos numero e tema (ex.: “Mascote”, “Estádio”).
Método: mostrar() devolve uma frase como: "Figurinha 7 – Mascote" .
2. Crie a classe Pacotinho , que guarda várias Figurinha (use uma lista).
Métodos:
adicionar(figurinha)
listar() (exibe todas as figurinhas)
3. Crie a classe MinhaColecao com uma lista de Figurinha que o aluno já possui.
Métodos:
colar(figurinha) (move do pacotinho para a coleção)
faltantes() (retorna quantas figurinhas ainda não foram coladas se o álbum tem 10 números).

Questāo 2 – Sala de Aula Virtual
1. Classe Aluno com nome e nota .
Método: foi_aprovado() retorna True se a nota ≥ 6.
2. Classe Professor com nome e lista de Aluno da turma.
Métodos:
adicionar_aluno(aluno)
media_da_turma()
aprovados() (lista apenas quem passou).
3. Classe Escola que guarda vários Professor .
Método: relatorio_geral() mostra, para cada professor, quantos alunos e média da turma.

Como testar cada desafio
1. Crie um arquivo main.py .
2. Instancie os objetos conforme o enunciado.
3. Chame os métodos e use print() para ver se tudo funciona.
4. Tente casos diferentes: listas vazias, nomes repetidos, etc.
Boa programação!'''
#Album de figurinha
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
#Sala de aula virtual
class Escola:
    def __init__(self):
        self.professores = []

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def relatorio_geral(self):
        print("------------|Relatório Geral da Escola|--------------------------")
        for prof in self.professores:
            print(f"\nProfessor {prof.nome}")
            print(f"Quantidade de alunos: {len(prof.lista_alunos)} e a media da turma foi: {prof.media_da_turma()}")
            print("-" * 65)


class Aluno:
    def __init__(self,nome,nota):
        self.nome = nome 
        self.nota = nota
    def foi_aprovado(self):
        if self.nota >= 6:
            print(f"Aluno {self.nome} foi Aprovado")
        else:
            print(f"Aluno {self.nome} foi Reprovado")

class Professor:
    def __init__(self,nome):
        self.nome = nome
        self.lista_alunos = []

    def adicionar_aluno(self,aluno):
        self.lista_alunos.append(aluno)
        
     
    def media_da_turma(self):
        print("-------|Média da Turma|------------------------------------------")
        md = 0
        for i in self.lista_alunos:
            md += i.nota
        return md / len(self.lista_alunos)


    def aprovados(self):
         print("---------|Lista de Aprovados|---------")
         for n in self.lista_alunos:
             if n.nota >= 6:
                print(f"{n.nome}")

       

a = Aluno("Aluisio", 5)
b = Aluno("Demetrios", 8)
c = Aluno("Alvim", 9)
d = Aluno("Maria",7)
e = Aluno("Mario",4)

professor1 = Professor("carlos")
professor1.adicionar_aluno(a)
professor1.adicionar_aluno(b)
professor1.adicionar_aluno(c)

professor2 = Professor("junior")
professor2.adicionar_aluno(d)
professor2.adicionar_aluno(e)

escola = Escola()
escola.adicionar_professor(professor1)
escola.adicionar_professor(professor2)

escola.relatorio_geral()
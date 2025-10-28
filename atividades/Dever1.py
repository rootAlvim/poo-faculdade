'''Classe Pessoa: Crie uma classe que modele uma pessoa:

• Atributos: nome, idade, peso e altura

• Métodos: Envelhecer, engordar, emagrecer, crescer.

• Obs: Por padrão, a cada ano que a pessoa envelhece, sendo a
idade dela menor que 21 anos, ela deve crescer 0,5 cm.

• O construtor pode possuir ou não parâmetros.'''
class Pessoa:
    def __init__(self,nome,idade,peso,altura):
          self.nome = nome
          self.idade = idade
          self.peso = peso
          self.altura = altura # Atributos
    def envelhecer(self,qntd):
         self.idade += qntd
         print(f"Agora sua idade e:{self.idade} ")
    def engordar(self,qntd):
        self.peso += qntd
        print(f"seu peso agora e {self.peso}")
    def emagrecer (self,qntd):
        self.peso -= qntd
        print(f"seu peso agora e {self.peso}")
    def crescer (self,qntd):
       if self.idade > 25:
            self.altura += 0.5
            print(f"Sua altura agora é: {self.altura}")
       else:
            self.altura += qntd
            print(f"Sua altura agora é: {self.altura}")


nm = str(input("Digite seu nome: "))
id = int(input(f"{nm} digite sua idade: "))
ps = float(input("Agora me diga seu peso em kg: "))
al = float(input("Por ultimo digite sua altura: "))
p1 = Pessoa(nm,id,ps,al)
print("=============== MENU ===============")
print("1 - Envelhecer")
print("2 - Engordar")
print("3 - Emagrecer")
print("4 - Crescer")

opcao = int(input(f"Escolha uma opção (1-4): "))
if opcao == 1:
     qntd = int(input("Quanto anos deseja envelhecer? "))
     p1.envelhecer(qntd)
elif opcao == 2:
     qntd = float(input("Quanto quilos deseja engordar? "))
     p1.engordar(qntd)
elif opcao == 3:
     qntd = float(input("Quanto quilos deseja emagrecer? "))
     p1.emagrecer(qntd)
elif opcao == 4:
    if id >= 21:
         print("Você so pode crescer 0.5cm!")
    else:
         qntd = float(input("Digite quanto cm quer crescer: "))
         p1.crescer(qntd)
'''total_andares
6 pass

Implemente tamb ́em os m ́etodos get total andares(), set total andares(), get capacidade(),
set capacidade(), get pessoas presentes(), set pessoas presentes() com valida ̧c ̃oes
similares.

Testes
Implemente os testes que simule cen ́arios reais e de erro, como no exemplo:

1 elevador = Elevador()
2 elevador.inicializar(3, 5)
3
4 # Testar entrar at ́e lotar
5 elevador.entrar()
6 elevador.entrar()
7 elevador.entrar()
8 elevador.entrar() # Deve exibir mensagem de erro

3

IFRN - Prof. Demetrios POO - Encapsulamento

9
10 # Testar subir at ́e o limite
11 elevador.subir()
12 elevador.subir()
13 elevador.subir()
14 elevador.subir()
15 elevador.subir() # Deve exibir erro
16
17 # Testar sair at ́e ficar vazio
18 elevador.sair()
19 elevador.sair()
20 elevador.sair()
21 elevador.sair() # Deve exibir erro
22
23 # Mostrar estado atual com getters
24 print("Andar:", elevador.get_andar_atual())
25 print("Pessoas:", elevador.get_pessoas_presentes())
26
27 # Testar setters com valores inv ́alidos
28 elevador.set_capacidade(0) # Erro
29 elevador.set_total_andares(-1) # Erro
30 elevador.set_pessoas_presentes(10) # Erro'''
class Elevador:
    def __init__(self,andar_atual,total_andares,capacidade,pessoas_presentes):
        self.__andar_atual = andar_atual
        self.__total_andares = total_andares
        self.__capacidade = capacidade
        self.__pessoas_presentes = pessoas_presentes

    def inicializar(self, capacidade: int, total_andares: int) -> None:
        self.set_capacidade(capacidade)
        self.set_total_andares(total_andares)
    # Seter e gets
    def get_total_andares(self) -> int:
        return self.__total_andares
    
    def set_total_andares(self, total):
        if total > 0:
            self.__total_andares = total
        else:
            print("Erro")

    def get_capacidade(self) -> int:
        return self.__capacidade


    def set_capacidade(self, capacidade):
        if capacidade > 0:
            self.__capacidade = capacidade
        else:
            print("Erro")

    def get_pessoas_presentes(self) -> int:
        return self.__pessoas_presentes

    def set_pessoas_presentes(self, pessoas: int) -> None:
        if 0 <= pessoas <= self.__capacidade:
            self.__pessoas_presentes = pessoas
        else:
            print("Erro")
    def get_andar_atual(self) -> int:
        return self.__andar_atual
    
    def set_andar_atual(self, novo_andar: int) -> None:
        if 0 <= novo_andar <= self.__total_andares:
            self.__andar_atual = novo_andar
    def entrar(self) -> None:
        if self.__tem_espaco():
            self.__pessoas_presentes += 1
            print(f"Mais uma pessoa entrou")
        else:
            print(f"Elevador esta cheio!")


    def sair(self) -> None:
        if self.__tem_gente():
            self.__pessoas_presentes -= 1

        
    def subir(self) -> None:
        if self.__pode_subir():
            self.__andar_atual += 1
            print(f"Subiu 1 andar!")
            print(f"Estamos no {self.__andar_atual}º andar")
        else:
            print(f"Erro!")

    
    def descer(self) -> None:
        if self.__pode_descer():
            self.__andar_atual -= 1
            print(f"Desceu 1 andar!")
            print(f"Estamos no {self.__andar_atual}º andar")
        else:
            print(f"Erro!")

    def __tem_espaco(self) -> bool:
        return self.__pessoas_presentes < self.__capacidade
    
    def __tem_gente(self) -> bool:
        return self.__pessoas_presentes > 0

    def __pode_subir(self) -> bool:
        return self.__andar_atual < self.__total_andares

    def __pode_descer(self) -> bool:
        return self.__andar_atual > 0



    # Cria o elevador no terreo 5 andar  capacidade  pra 3 pessoas sem nimguem dentro vazio
elevador = Elevador(0, 5, 3, 0)
elevador.inicializar(3, 5)
elevador.entrar()
elevador.entrar()
elevador.entrar()
elevador.entrar() # erro pois a capacodade de pessoas no elevador e 3
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir() # erro so possui 5 andares
elevador.sair()
elevador.sair()
elevador.sair()
print(f"Andar: {elevador.get_andar_atual()}º")
print("Pessoas:", elevador.get_pessoas_presentes())
elevador.set_capacidade(0) # Erro
elevador.set_total_andares(-1) # Erro
elevador.set_pessoas_presentes(10) # Erro
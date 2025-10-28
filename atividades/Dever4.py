class Bomba_de_combustivel:
    def __init__(self,tipo_combustivel,valor_litro,quantidade_combustivel):
        self.__tipo_combustivel = tipo_combustivel
        self.__valor_litro = valor_litro
        self.__quantidade_combustivel = quantidade_combustivel

    def AbastecerPorValor(self,valor_abastecido):
        if valor_abastecido > self.__quantidade_combustivel:
            print(f"Quantidade de gasolina insuficiente para o abastecimento")
        else:
            litros = valor_abastecido/self.__valor_litro
            print("Abastecendo......")
            print(f"No total foram {litros} litros de {self.__tipo_combustivel}")
            self.__quantidade_combustivel -= litros

    def AbastecerPorLitro(self,litros):
        if litros > self.__quantidade_combustivel:
            print(f"Quantidade de gasolina insuficiente para o abastecimento")
        else:
            valor_pago = self.__valor_litro * litros
            print("Abastecendo......")
            print(f"No total foi {valor_pago}R$ de {self.__tipo_combustivel}")
            self.__quantidade_combustivel -= litros

    def AlterarValor(self,valor):
        self.__valor_litro = valor
        print(f"Valor do combustível alterado com sucesso!")
        print(f"Valor atual: {self.__valor_litro}")

    def AlterarCombustivel(self,tipo_combustivel):
        self.__tipo_combustivel = tipo_combustivel
        print(f"Combustível alterado com sucesso!")
        print(f"Combustível atual: {self.__tipo_combustivel}")

    def AlterarQuantidadeCombustivel(self,qntd_combustivel):
        self.__quantidade_combustivel = qntd_combustivel
        print(f"Quantidade alterada com sucesso!")
        print(f"A quantidade de {self.__tipo_combustivel} disponível e {self.__quantidade_combustivel}")


    def AbastecerVeiculo(self, veiculo, litros):
        capacidade_disponivel = veiculo.get_capacidade_tanque() - veiculo.get_qntd_combustivel()

        if veiculo.get_tipo_combustivel() != self.__tipo_combustivel:
            print("Tipo de combustível incompatível com o seu!")
        elif litros > self.__quantidade_combustivel:
            print("A bomba não tem combustível suficiente.")
            
        elif litros > capacidade_disponivel:
            print(f"O tanque só cabe mais {capacidade_disponivel:} litros.")
            litros = capacidade_disponivel  
        valor_pago = litros * self.__valor_litro
        self.__quantidade_combustivel -= litros
        veiculo.set_qntd_combustivel(veiculo.get_qntd_combustivel() + litros)

        print(f"Foram colocados {litros:.2f} litros de {self.__tipo_combustivel}.")
        print(f"Valor pago: R$ {valor_pago:.2f}")
        print(f"Combustível restante na bomba: {self.__quantidade_combustivel} litros.")
        print(f"Combustível no veículo: {veiculo.get_qntd_combustivel()} litros.")


class Veiculo:
    def __init__(self, tipo_combustivel, capacidade_tanque,qntd_combustivel):
        self.__tipo_combustivel = tipo_combustivel
        self.__capacidade_tanque = capacidade_tanque
        self.__qntd_combustivel = qntd_combustivel
    #get pega o valor
    def get_tipo_combustivel(self):
        return self.__tipo_combustivel

    def get_capacidade_tanque(self):
        return self.__capacidade_tanque

    def get_qntd_combustivel(self):
        return self.__qntd_combustivel

    # Set altera o valor
    def set_tipo_combustivel(self, novo_tipo):
        self.__tipo_combustivel = novo_tipo

    def set_capacidade_tanque(self, nova_capacidade):
        self.__capacidade_tanque = nova_capacidade

    def set_qntd_combustivel(self, novo_consumo):
        self.__qntd_combustivel = novo_consumo
    


#testes:
b1 = Bomba_de_combustivel('Gasolina', 12, 120)
carro = Veiculo('Gasolina', 50, 10)
b1.AbastecerVeiculo(carro, 30)
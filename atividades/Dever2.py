'''Crie um método transferir um valor para
um desAno.
• Acrescente o atributo codigo_Apo e
nome_Apo. 01 para “conta corrente” e 02
para “poupança”.
Faça um programa que receba as
informações do terminal para criar duas
contas e que faça uma transferência entre
contas.'''
class Conta:
     def __init__(self,numero,titular,saldo,limite,nome_tipo,codigo_tipo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.codigo_tipo =  codigo_tipo     
        self.nome_tipo = nome_tipo

     def deposita(self,valor): #Metodo para deposito
        if valor > 300:
           print("Limite insulficiente")
        else:
           self.saldo += valor

     def saca(self,valor): #Metodo para saque
        if self.saldo <= 0 or valor > self.saldo :
            print("Saldo insuficiente")
        else:     
         print(f"Você sacou {valor}")
         self.saldo -= valor
         
     def extrato(self): #Metodo para extrato
         print("numero: {} \nsaldo: {}".format(self.numero,self.saldo))
         print("nome: {} \nlimite: {} ".format(self.titular,self.limite))

     def transferencia(self,valor,conta2): #Metodo para transferencia
           if self.saldo <= 0 or valor > self.saldo:
            print("Saldo insuficiente")
           else:
            print("Transferencia realizada com sucesso!")
            self.saldo -= valor
            conta2.saldo += valor

             

conta2 = Conta(12,"ze",0,300,0,0) #conta criada para transferir o dinheiro da conta principal

print("=============== Bem-vindo ao BB ===============")
tit = str(input("Digite seu nome: "))
num = int(input("Digite o nº de sua conta: "))

print("Escolha o tipo de conta:")
print("1 - Conta Corrente")
print("2 - Conta Poupança")

while True:
    tipo = input("Digite 1 ou 2: ")
    if tipo == "1":
        codigo_Apo = "01"
        nome_Apo = "conta corrente"
        break
    elif tipo == "2":
        codigo_Apo = "02"
        nome_Apo = "poupança"
        break
    else:
        print("Opção inválida. Digite 1 ou 2.")

valor = Conta(num, tit, 0, 300,codigo_Apo, nome_Apo)

print("Cadrasto realizado com sucesso, por padrão seu limite para deposito/saque é 300$")

while True:
     print("           1-Realizar deposito                 ")
     print("           2-Realizar saque                    ")
     print("           3-Ver extrato                       ")
     print("           4-Realizar Transferência            ")
     print("           5-sair                              ")

     opc = int(input("Escolha uma opção: "))
     if opc == 1:
          depos = float(input("Digite o valor para deposito: "))
          valor.deposita(depos)
     elif opc == 2:
          sac = float(input("Digite o valor de saque: "))
          valor.saca(sac)
     elif opc == 3:
          valor.extrato()
     elif opc == 4:
         valor_transferencia = float(input("Digite o valor para transferir: "))
         valor.transferencia(valor_transferencia, conta2)
     elif opc == 5:
        print("Saindo do sistema. Obrigado!")
        break
     else:
        print("Opção inválida. Tente novamente.")

conta2.extrato() #extrato da segunda conta
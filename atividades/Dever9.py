'''lis = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
maior = 0
for n in lis:
    if n > maior:
         maior = n
print(maior)'''

'''list = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
menor = 100
for n in list:
    if n < menor:
        menor = n
print(menor)'''

'''list = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
for n in list:
    if n % 2 == 0:
        print(n,end=' ')'''
'''        
list = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
sum = 0
for n in list:
    sum = sum + n
md = (sum / (len(list)))
print(f'{md:.2f}')
'''
'''list = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
sum = 0
for n in list:
    if n < 0:
        sum = sum + n
print(sum)
print('*********************************')
print('***Bem vindo ao jogo da Forca!***')
print('*********************************') 

palavra_secreta = 'banana'
letras_acertadas = ['_', '_', '_', '_', '_', '_']

enforcou = False
acertou = False
erros = 0

print(letras_acertadas)

while(not enforcou and not acertou):

    chute = input("Qual letra? ")

    if(chute in palavra_secreta):
        posicao = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra
            posicao += 1
    else:
        erros += 1

    enforcou = erros == 6
    acertou = '_' not in letras_acertadas            
    print(letras_acertadas)

if(acertou):
    print('Você ganhou!!')
else:
    print('Você perdeu!!')

print('Fim do jogo')

num = [2,5,9,1]
num.append(7)
num.sort()
print(f'Tamanho da lista: {len(num)}')
print(num)

var = [] 
maior = 0 
menor = 1000000


for m in range(5):
    x = int(input('Valor: '))
    var.append(x)
i1 = 0
i2 = 0
for p,m in enumerate(var):
    if m > maior:
        maior = m
        i1 = p
    if m < menor:
        menor = m
        i2 = p
print(f'{maior} {i1} {menor}{i2}')'''
#Dicionario
dados = {
    'Nome': 'Pedro'
    
}
dados['Sexo'] = 'M'

print(dados.values())
print(dados.keys())
print(dados.items())
for k , v in dados.items():
    print(f'{k}: {v}')
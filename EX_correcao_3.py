#01 - Carregue os itens e seus respectivos preços de um arquivo txt para um Dictionary

#Abrir o arquivo
# no meu projeto os arquivos python estou gravando em C:\POO\PYTHON
# os arquivos de dados estou gravando em C:\POO\PYTHON\DATA
# para acessar o arquivo a partir da raiz do meu projeto (pasta aberta no VS Code) -> C:\POO.
# Posso usar o caminho relativo, dessa forma  
arquivo = open('python\\data\\lista_precos.csv', encoding='ANSI')

#Criar um dictionary
produtos = dict()

#Carregar o arquivo para o dictionary
#Primeiro, vamos VARRER O ARQUIVO a linha 
# cada linha no arquivo possui um código, uma descrição e um preço
for linha in arquivo:
    #elimina a quebra de linha (\n) no final
    #quebra os campos por ; adicionando em uma lista pra facilitar a manipulação
    campos = linha.strip().split(';')
    #adiciona (ou edita) o item no dicionario, atribuindo uma lista como valor
    produtos[campos[0]] = [campos[1],campos[2]]



# 2 Crie um programa para consultar preços a partir do nome do produto (parcial)
while True:
    try:
        codigo = input("Digite o código do produto:")
        descricao = produtos[codigo][1]
        preco = produtos[codigo][0]
        break
    except:
        print('Produto não encontrado, digite novamente')

print('O produto {} com código {} custa R${}'.format(produtos[codigo][1], codigo, produtos[codigo][0]))

codigo = input('Digite o codigo:')
if codigo in produtos:
    print('O produto {} com código {} custa R${}'.format(produtos[codigo][1], codigo, produtos[codigo][0]))
else:
    print('O produto {} não foi encontrado.'.format(codigo))


# 3 Crie um programa para fazer um pedido. O usuário deve
#procurar pelo produto e informar sua quantidade. No fim o
#programa deve totalizar o pedido e mostrar a lista de produtos
#comprados, suas quantidades, seus preços e o preço total.

#exe 3 falta correcao 

arquivo = open('C:\\Users\\Jk_cu\\Downloads\\lista_precos.csv','r')

produtos = dict()

for linha in arquivo:
    campos = linha.strip().split(';')
    produtos[campos[0]] = [campos[1],campos[2]]

print(produtos)  #-----  1 parte de cima pra carregar os arquivo 


quantidade_produto = []

while True:
    try:
        codigo = input("Digite o código do produto:")
        descricao = produtos[codigo][1]
        preco = produtos[codigo][0]
        quantidade_produto.append(input('Quantidade:'))
        break   # obs 
    except:
        print('Produto não encontrado, digite novamente')

print('O produto {} com código {} custa R${}'.format(produtos[codigo][1], codigo, produtos[codigo][0]))

codigo = input('Digite o codigo:')
if codigo in produtos:
    print('O produto {} com código {} custa R${}'.format(produtos[codigo][1], codigo, produtos[codigo][0]))
else:
    print('O produto {} não foi encontrado.'.format(codigo))  
# ---------------------------------------------------------------------- 3 outra parte


#ljust(15)

try:
    quantidade_produto = []
    codigo_produto = dict()
    op = 'S' 
    while (op != 's'):
        print() 
        print('Menu'.center(50))
        print('[C] para continuar'.rjust(50))
        print('[S] para sair'.rjust(45))
        
        codigo = str(input("Digite seu produto:"))
        codigo_produto[codigo] = + 1   # obs 
        quantidade_produto.append(int(input('Quantidade:')))
        
        op = input('Opção []: ')
        if op == 's':
            break
        elif op =='c':
            continue    
        else:
            print(' ? Opção invalida !')    

    print('Seus produtos:',codigo_produto)
    print('Quantidade de produtos:',quantidade_produto)
    print('Quantidade de produtos:',sum(quantidade_produto))
    

except:
    print('! Error ?'.center(50))    

finally:
    print('...Processo Finalizado...'.center(50))    














# outros exercicios --- parte ------------------------------------------------------------------

#Crie um dictionary vazio com o nome Produtos
Produtos = dict()

#Adicione 10 produtos a esse dictionary, usando os números de 1 a 10 como chave.
for i in range(10):
    Produtos['Produto{}'.format(i)] = round(i * 1.2, 2)

#Imprima o item com chave 5.
print(Produtos['Produto5'])
#Altere o valor do item com chave 9.
Produtos['Produto9'] = 15.90
#Qual o tamanho do dictionary?
tamanho = len(Produtos)
#Adicione um novo produto ao dictionary
Produtos['Abacaxi'] = 0.99
#Imprima uma lista com todos os valores do dictionary
for produto, preco in Produtos.items():
    print('O produto {} custa R$ {:.2f}'.format(produto, preco))
#Conte o número de ocorrências de cada letra na palavra ‘ANTICONSTITUCIONALISSIMAMENTE’ e imprima na tela.
palavra = 'ANTICONSTITUCIONALISSIMAMENTE'
letras = dict()
for letra in palavra:
    letras[letra] = letras.get(letra,0) + 1

for letra, contagem in letras.items():
    print('A letra {} aparece {} vezes'.format(letra, contagem))

#Faça um gráfico de barras para mostrar a distribuição das ocorrências das letras no arquivo LOREM.TXT.
import matplotlib.pyplot as plt
import os

file = open('python\\lorem.txt')

import string
letras.clear()
for linha in file:
    linha = linha.translate(str.maketrans('','', string.punctuation))
    linha = linha.strip()
    for letra in linha:
        letras[letra] = letras.get(letra,0) + 1

del letras[' ']

plt.plot(letras.keys(), letras.values())
plt.ylabel('Número de ocorrências')
plt.xlabel('Letras')
plt.title('Distribuição das letras no arquivo')
plt.show()



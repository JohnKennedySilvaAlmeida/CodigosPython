# 1 Crie um dictionary vazio com o nome Produtos

Produtos = dict()
#print(Produtos)

#  2 Adicione 10 produtos a esse dictionary, usando os números de 1 a 10 como chave.

Produtos = {'1':'managa','2':'banana','3':'coca','4':'morango','5':'Queijo','6':'arroz','7':'carne','8':'suco','9':'açai','10':'bolo'}
#print(Produtos)

try:  

    Produto_cod = dict()
    # nome_prduto = ''

    for conteudo in range(1,11):
        nome_prduto = str(input('Digite o Produto:'))
        Produto_cod[conteudo] = nome_prduto
        
    print(Produto_cod)

    Produto_cod.clear()

except:
    print('! Error !') 
    

# 3 Imprima o item com chave 5.

print(Produtos['5'])

#[5] ou 

# 4 Altere o valor do item com chave 9.

Produtos['9'] = 'Ovo'
#print(Produtos)

#[9] ou 

# 5 Qual o tamanho do dictionary?

print('Tamanho',len(Produtos))

# 6 Adicione um novo produto ao dictionary

Produtos['11'] = 'Leite d vaca'
print(Produtos)

# 7 Imprima uma lista com todos os valores do dictionary

#print(Produtos.values()) fim - nome 
#print(Produtos.keys()) inicio - cod     

print(Produtos.items())                    #obs  keysc vawes LL

# 8 Conte o número de ocorrências de cada letra na palavra
#‘ANTICONSTITUCIONALISSIMAMENTE’ e imprima na
#tela.
palavra = 'ANTICONSTITUCIONALISSIMAMENTE'
d = dict()

for letra in palavra:
    d[letra] = d.get(letra, 0) + 1 

print(d)

# 9 Faça um gráfico de barras para mostrar a distribuição das
#ocorrências das letras no arquivo LOREM.TXT.
            
import matplotlib.pyplot as plt          # d - grafico 

plt.bar(d.keys(), d.values())
plt.show()


#frase = ('''Vamos contar quantas vezes cada letra aparece nessa string jjjjjjjjj kkkkkkkk 
#wertyuiolkjhgfdsxcvb aaaaaa ssssss qqqqqqqq eeeeeee ttttttttttt ddddddddd çççççç kkkkkkk jjjjj hhhh ggg n
#zxzxzsas sdsf qwqw erer df fglkbokfg 11223 456 789 n''')

#arq_abre = open('mailbox_123.txt', 'r')  pytohn jk
#palavras = arq_abre.read() nao precisa 

#print(palavras)                               falta melhorar ????

#d = dict()

#import matplotlib.pyplot as plt

#plt.bar(d.keys(), d.values())
#plt.show()

#palavras

#---------------------------------------------------------------------------------------------------










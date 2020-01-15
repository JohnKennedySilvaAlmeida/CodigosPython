# Exercícios
# 01
produtos = []

# 02
# adicionando números na lista de produtos
#for i in range(10):
#    produtos.append(i)

#adicionando produtos de uma lista em outra com append
lista = ['mamão', 'banana', 'maça', 'coco', 'melão', 'melancia', 'manga', 'mingau', 'laranja', 'maracuja', 'jaca']
for item in lista:
    produtos.append(item)

#adicionando a partir de entrada de teclado
#for i in range(10):
    #produtos.append(input('Digite o produto:'))

print(produtos)

# 03
lista_mil = []
for i in range(1,1001):
    lista_mil.append(i)
   
contador = 1
while contador <= 1000:
    lista_mil.append(contador)
    contador += 1

print(lista_mil)

# 04
lista_mil.sort(reverse=True)
print(lista_mil)

# 05
lista_mil.remove(100)
lista_mil.remove(300)
lista_mil.remove(500)

lista_para_deletar = [100,300,500]
for item in lista_para_deletar:
    lista_mil.remove(item)

# 06
# Retornar os 3 maiores valores de uma lista qualquer
def maior(lista_parametro):
    maiores = []

    lista_parametro.sort(reverse=True)
    for i in range(3):
        maiores.append(lista_parametro[i])
    
    return maiores

print(maior(produtos))

# 07
# Crie uma lista com valores 
lista_doida = ['xxxx', 1, 1.5, 'a', True]

# 08
print(*lista_doida, sep='\n')

for item in lista_doida:
    print('{}\n'.format(item))

# 09
i = lista_doida.index('a')

# 10

for item in produtos:
    if item.count('a') > 0:
        produtos.remove(item) 

print(produtos)

# 01
numeros = [11, 12, 15, 19, 32, 44, 76, 99]

for i in range(len(numeros)):
    if numeros[i] > 50: numeros[i] = numeros[i] * 2
    else: numeros[i] = numeros[i] * 7

for numero in numeros:
    if numero > 50:
        numero = numero * 2
    else:
        numero = numero * 7

# 03  último item da lista

ultimo = numeros[len(numeros)-1]

maior_valor = max(numeros)

numeros.sort()
maior_valor = numeros[len(numeros)-1]

numeros.sort(reverse=True)
maior_valor = numeros[0]

menor_valor = min(numeros)

numeros.sort()
menor_valor = numeros[0]

numeros.sort(reverse=True)
menor_valor = numeros[len(numeros)-1]

print("O número {} é o último da lista".format(ultimo))

# 4
nova_lista = numeros[1:4]

#5
numeros[5] = 100

#6 
file = open('c:\\temp\\mbox.txt')
conteudo = file.read()
palavras = conteudo.split()

conta = len(palavras)

# 8 Elimine da lista palavras todos os itens que possuem a palavra “java”.
#for palavra in palavras:
#    if palavra.count('java') > 0:
#        palavras.remove(palavra)

#Crie uma nova lista com os primeiros 20 itens da lista Palavras, 
# ordenados em ordem alfabética.

nova_lista = []
for i in range(20):
    nova_lista.append(palavras[i])

nova_lista.sort()

# Crie uma nova lista com os itens da lista Palavras 
# que são um endereço de e-mail.

lista_email = []
for palavra in palavras:
    if palavra.count('@') > 0:
        lista_email.append(palavra)

print(lista_email)
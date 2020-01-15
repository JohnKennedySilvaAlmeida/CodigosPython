#listas comuns
lista_vazia = []
numeros = [10, 20, 30, 40]
produtos = ['feijão', 'arroz', 'leite', 'sal', 'farinha']

#listas com valores diversos
lista_qualquer = ['spam', 2.0, 5]

#listas de listas
clientes = [['José', '02912206102'], ['João', '01234567890'], ['Antonieta', '098765432345']]
print(clientes)

#contando valores de uma lista
tamanho = len(lista_vazia)
tamanho = len(numeros)

#acessando valores de uma lista
produto = produtos[0]
print('O  primeiro produto da lista é {}'.format(produto))

#alterar o valor de um item da lista
produtos[0] = 'Melancia'
print(produtos)

#se tentar acessar um item que não existe...
#produto = produtos[10]

#verificar se um item está na lista
if "leite" in produtos:
    print("leite está na lista")

#passar por todos os itens da lista
for produto in produtos:
    print(produto)

for i in range(len(produtos))>
    print(produtos[i])

#alterar todos os valores de uma lista
print(numeros)
for i in range(len(numeros)):
    numeros[i] = numeros[i] * 2 
print(numeros)

#concatenando listas
nova_lista = produtos + numeros
print(nova_lista)

nova_lista = produtos * 2 
print(nova_lista)

#pegando parte da lista
print(produtos[1:3])
print(produtos[:4])
print(produtos[4:])
produtos[1:3] = ['banana', 'maçã'] 

#adicionando itens na lista
numeros.append(50, 60, 70)
print(numeros)
novos_numeros = [80,90]
numeros.extend(novos_numeros)
print(numeros)

#ordenação
numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)

#eliminar elementos de uma lista
numero = numeros.pop()  #elimina o último elemento
numero = numeros.pop(1) #elimina o elemento #1
del numeros(1)          #elimina o elemento #1
numeros.remove(80)
print(numeros)

#funções úteis
tamanho = len(numeros)
maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
#transformar uma string em uma lista de caracteres
string = 'qualquer coisa'
lista_de_caracteres = list(string)
lista_de_palavras = string.split()

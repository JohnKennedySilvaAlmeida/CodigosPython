# um dictionary é um tipo especial de lista.
# a função DICT() serve para criar um dictionary vazio
dictionary = dict()
print(dictionary)

#um dictionary simples, com um item
dictionary = {'primeiro':'maçã'}
print(dictionary)

#uma lista equivalente ao dictionary anterior
lista = ['maçã']
lista.append(True)
lista.append(1000)
lista.append(10.0)
lista.append([10, 20, 30])

print(lista)

#em uma lista comum, o indexador é um inteiro sequencial, iniciando de zero
lista_frutas = ['maça', 'banana', 'laranja', 'melancia']
#para acessar um item em uma lista comum, basta usar o seu índice
print(lista_frutas)
print(lista_frutas[1])

#em um dictionary, nós especificamos o indexador
dic_frutas = {'ma':'maça', 'b':'banana', 'l':'laranja', 'me':'melancia'}
print(dic_frutas)
print(dic_frutas['me'])

#dessa forma, o dictionary acaba sendo uma lista onde cada item é componto pelo indexador e pelo valor
#também chamados de chave / valor
dictionary = {'chave':'valor', 'chave2':'valor2', 'chave3':'valor3'}

#para manipular um item em um dictionary basta especificar sua chave. 
#se já existe a chave, o valor pode ser alterado
dic_frutas['me'] = 'melãozinho'
#se não existe a chave, será adicionado o par chave / valor no dictionary
dic_frutas['ca'] = 'cacauê'
print(dic_frutas)
#dá para inserir ou atualizar itens com o método UPDATE
dic_frutas.update({'ca':'caqui'})

#eliminar itens do dictionary
del dic_frutas['me']
dic_frutas.pop('ca')    
novas_frutas = dic_frutas.copy()
novas_frutas.clear()      #elimina todos os elementos

# a ordem em que os valores aparecem no dictionary não importa

# para saber o número de itens de um dictionary
tamanho = len(dic_frutas) #são contados os conjuntos chave / valor
print(tamanho)

#o operador IN procura a variável nas chaves
#é muito rápido por que usa hash table - enquanto as listas simples fazem busca sequencial
var = 'melão' in dic_frutas
print(var)
var = 'me' in dic_frutas
print(var)

#médodos úteis
# VALUES
print(dic_frutas.values())
# KEYS
print(dic_frutas.keys())
# ITEMS

for key, value in dic_frutas.items():
    print('A chave {} está relacionada ao valor {}'.format(key, value))

#para procurar com IN nos valores de um dictionary, precisa extraí-los para outra lista
frutas = list(dic_frutas.values())
var = 'melão' in frutas
print(var)

#pegar o valor de um item a partir de seu índice
print(dic_frutas.get('me', 'não encontrado'))

#contar palavras em um arquivo, em uma lista, em uma string
palavra = 'paralelepípedo'
d = dict()
for letra in palavra:
    if letra not in d:
        d[letra] = 1
    else:
        d[letra] = d[letra] + 1
print(d)

d.clear()
#GET retorna o valor correspondente, ou o valor default (aqui, zero)
for letra in palavra:
    d[letra] = d.get(letra, 0) + 1 

print(d)


import matplotlib.pyplot as plt

plt.bar(d.keys(), d.values())
plt.show()

frase = 'Vamos contar quantas vezes cada letra aparece nessa string'
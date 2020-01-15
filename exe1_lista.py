# 1 - crie um lista vazia o nome produtos.

produtos = []

# 2 - acione 10 produtos quaiquer a essa lista com o comando append.
print('2 exe')

produtos.append('manga')
produtos.append('jaca')
produtos.append('goiaba')
produtos.append('arroz')
produtos.append('feijao')
produtos.append('presunto')
produtos.append('carne')
produtos.append('cerveja')
produtos.append('morango')

print(produtos)
print()

 #adicionando números na lista de produtos
 #for i in range(10):
      #produtos.append(i)


#adicionando a partir de entrada de teclado
#for i in range(10):
    #produtos.append(input('Digite o produto:'))
#print(produtos)


# 3 - crie uma lista chmada list_mil com numero de 1 a 1000.
print('3 exe')
#lista = list(range(10)) outra forma d fazer uma lista de 1 ate ....
#lista = range(10)

list_mil = []

for i in range(1,101):
    #print(i)
    list_mil.append(i)
print(list_mil)

# 4 - ordene a list_ mil em ordem inversa..
print()
print('4 exe')

list_mil.sort(reverse = True)
print(list_mil)

# 5 - Elimine os numeros 10,30,50 da list-mil..
print()
print('5 exe')

list_mil.sort()

list_mil.remove(10)
list_mil.remove(30)
list_mil.remove(50)
print(list_mil)

#outro exemplo 
# lista_deletar = [100,200,300]
#for item in lista_deletar:
#    lista_deletar.remove(item)


# 6 - faca uma funcao para receber uma lista e retorna os maiores 3 valores da lista.
print()
print('6 exe')

lista_teste = [1,2,3,4,5,6,7,8,9,10]   # falta a funcao-----------------------------
lista_teste.sort(reverse = True)
print(lista_teste [0:3])

def Maior_3():
    lista_teste.sort(reverse = True) # procedimento sm parametros
    print(lista_teste [0:3])
Maior_3() 
# ------------------------------- correção ====================================
def maior(l_paramentro):
    maiores = []

    l_paramentro.sort(recerse = True)

    for i in range(4):
         maiores.append(l_paramentro[i])
  
    return maiores

print(maior(lista_teste))     

#print(max(lista_teste))   #motra os maiores

# 7 - crie uma lista com valores d tipo d string, boolena,inteiro e decimal..
print()
print('7 exe')

lis_tes = ['a','b',8,9,'jk',1.25,True,False]
print(lis_tes)


# 8 - imprima cada valor da lista anteiro em uma linha diferente..
print()
print('8 exe')

print('{}\n''{}\n''{}\n''{}\n''{}\n''{}\n''{}\n''{}\n'.format(*lis_tes))

print(*lis_tes, sep = '\n')   #juntar tudo e separa tudo '' ou '\n'

''.join(lis_tes) # so funciona com numero ou string
print(lis_tes)

for conta in lis_tes:
    print(conta)
    print('\n') # ou um print so com .format()

# 9 - procure um intem em uma lista anterior com o metodo index..
print()
print('9 exe')

achar = lis_tes.index('jk')
print(lis_tes[achar])

lis_tes.index('jk') # outra forma 

i = lis_tes.index('jk')
i1 = lis_tes.index('jk',i + 1)

#10 - elimine da lista produtos todos os produtos que comtem 'a' no nome ...
print()
print('10 exeeeee')   # falta ?? ------------------------------

#produtos.remove('a')
for item in produtos:
    if ('a' in produtos):
        produtos.remove(item)

# outra forma

for item in produtos:
    if item.count('a') > 0:
       produtos.remove(item)         





    





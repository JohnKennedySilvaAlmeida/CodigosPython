#lista = [1,2,3,4,5,11,25,13,14]

#print(lista)

#print(lista[0])



#lista.count() contar

#lista.sort() sequencia

#print('Nao ordenada {}'.format(lista))


#nome = 'john'
#print(nome)

#outro_nome = nome
#print(outro_nome)

#outro_nome = 'lula'
#print(nome)

#if nome == outro_nome:
 #   print('sao iguais')
#else:
 #   print('diferentes')


valor = [10,30,20,11]        
produtos = ['arroz','leite','banana','oleo']

print(produtos)
produtos.append('manga')
print(produtos)

produtos.insert(2,'goiaba')
print(produtos)

produtos[3] = 'jaca'
print(produtos)

i = produtos.index('arroz')
print(produtos[i])

try:
    i = produtos.index('morango')
    print(produtos[i])
except ValueError:
    print('nao existe essa fruta')


n = [1,2,3]
print(sum(n))

print(max(n))
print(min(n))

print(sum(n))
print(len(n))

print(sorted(n))
n.sort()
 
n1 = ['a','lula','morango','banana']
for produt in n1:
    print(produt)
    if produt =='banana':
       n1.remove(produt)

# parte d lista

#print(n1[1:2])

#print(n1[1:4])

# n1 = [1,2,3,4,5,6,7,8]
# n1[1] = 20    altera a lista pela posição  
# n1[1:2] = [20,33]

# n1.sort()
# n1.sort(reverse = True)  
# 


nomes = 'john'
lista_caracteres = list(nomes)
print(lista_caracteres)









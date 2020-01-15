#uma lista indexada
tupla = ('banana', 'maça', 'laranja', 'manga')
print(type(tupla))

#uma tupla simples
t = ('a', 'b', 'b', 'c')
print(t)
print(type(t))

#uma tupla vazia - função TUPLE, sem parâmetros
t2 = tuple()
print(t2)

#se o parâmetro for uma sequencia, cada item será um elemento na nova tupla
t3 = tuple('Uma string é uma sequencia de caracteres'.strip())
print(t3)

#muito parecida com uma lista
print('O primeiro elemento da tupla é {}'.format(t3[0]))
print('O útlimo elemento da tupla é {}'.format(t3[-1]))
print(t3[1:5])
print(t3.index('r'))

#mas se tentar alterar um dos elementos... 
#t3[0] = 'C'

#embora não seja possível alterar um elemento, é possível substituir o elemento
#substituindo o primeiro elemento da tupla
t3 = ('C',) + t3[1:]
print(t3)

#substituindo o 5o elemento da tupla
t3 = t3[:3] + ('X',) + t3[4:]
print(t3)

#é possível comparar tuplas
print(t3 == t2) #são comparados os valores individualmente. só retornará true se todos os elementos atenderem a condição
print(t3 > t2) 
print(t2 > t)

texto = 'ordenando uma lista de palavras pelo seu tamanho'
palavras = texto.split()

#criar uma lista de tuplas para indexar e ordenar
lista = list()
for palavra in palavras:
    lista.append((len(palavra), palavra)) #estamos adicionando uma tupla na lista!

print(lista)
lista.sort(reverse=True) #cada elemento é uma tupla, ordena pelo inteiro, depois pela palavra (desempate)
print(lista)

#eliminar os valores numéricos guardando apenas o texto
resultado = list()
for tamanho, palavra in lista:
    resultado.append(palavra)

print(resultado)

#o método ITEMS do dictionary na verdade retorna uma lista de tuplas
d = {1: 'python', 2:'java', 3:'ruby', 4:'perl'}
lista = list(d.items())
    
lista.sort() #está ordenando pela chave

lista.clear()
#se quiser ordenar pelo valor... podemo usar outra lista
for chave, valor in d.items():
    lista.append((valor, chave))

lista.sort()

#para adicionar uma tupla (imutável) como chave em um dicionario
contatos = dict()
contatos['waldemar', 'roberti'] = '4799737070'
contatos['joão', 'estevão'] = '4799738080'
for nome, telefone in contatos.items():
    print('Nome {} {}, telefone {}'.format(nome[0], nome[1], telefone))



 #   --------------------------------------------------------------
 # PORVA
 
 
 #'''numeros = [10,20,30,40,50]

#for i in range(len(numeros)):
   # if numeros[i] > 20: numeros[i] = numeros[i]*2
   # else: numeros[i] = numeros[i]*3

#print(numeros)    


#t = tuple()

#t = (1,2,3,4,5)

#print(t)'''

#import string

#arquivo = open ('C:\\Users\\Jk_cu\\lorem1.txt','r')
#dic_letras = dict()

#for linha in arquivo:
   # linha = linha.upper().translate(str.maketrans('','',string.punctuation))
    #lista_letras = linha.split()

    #for letra in lista_letras:
        #dic_letras[letra] = dic_letras[letra] + 1 erro
        #dic_letras[letra] = dic_letras.get(letra,0)+1

#lista_ordem = []

#for letra,ocorrencia in dic_letras.items():
   # lista_ordem.append((ocorrencia,letra))
#lista_ordem.sort(reverse=True)
#result = lista_ordem[:5]

#for ocorrencia, letra in result:
    #print('a letra {} aparace {} x no arquivo'.format(letra,ocorrencia) )   

data = [(0, 1), (2, 3), (4, -5), (6, -3)]
data.sort(key=lambda x: x[1])

d = ([{'a':'1','b':'2'}],[{'z':'12','y':'22'}])
print(d)

     




   


import json

def criandoJson(lista): # funcao / criar 
    with open('teste.json', 'w') as abrir:
        json.dump(lista, abrir)

def carregarJson(): # funcao / carregar 
    with open('teste.json', 'r') as abrir:
        return json.load(abrir)

try: # erros

    print('-= Digite Somente 2 Nomes (Lista) -='.center(100)) # - menu 1
    nomes = [] # inicio - lista 

    for conteudo1  in range (2): # for 1
        nomes.append(input("Digite seu Nome:"))
    criandoJson(nomes) # criando Json / lista- nomes  - obs !


    print('-= Digite Somente 2 Nomes (Dicionario) -='.center(100)) # - menu 2
    nome = {} # dict - inicio 

    for conteudo2 in range (2): # for 2
        novo_nome = (input('Digite seu nome:'))
        nome[conteudo2] = novo_nome


    print()
    print(json.dumps(nome)) # obs - funcao / json
    print('-='*14)
    print(carregarJson()) # obs - funçao / json
    print()

except:
    print('Erro...'.center(100))    
finally:
    print('Finalizado...')   









''' outra forma  - obs ?

import json

def criandoJson(lista):
    with open('teste.json', 'w') as abrir:
        json.dump(lista, abrir)

def carregarJson(carregarr):
    with open('teste.json', 'r') as abrir:
        return json.load(abrir)

nomes = ['john','kennedy']

criandoJson(nomes)

dicionario = {'nome': 'johnn', 'sobrenome': 'kennedyy'}

print(json.dumps(dicioanario))
print(carregarJson('teste.json')) '''


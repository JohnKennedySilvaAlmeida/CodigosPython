#1 Carregue um arquivo texto
#conte as palavras do arquivo usando dictionary
#imprima as 10 palavras que mais aparecem no arquivo (aquelas
#que tem a contagem maior) usando tuplas.

import string
import matplotlib.pyplot as plt

def myfunction(caminho):
    file = open (caminho, encoding='ANSI')
    palavras = dict()
    for linha in file:
        linha = linha.upper().translate(str.maketrans('','',string.punctuation)) 
        lista_palavra = linha.split()
        for palavra in lista_palavra:
            palavras[palavra] = palavras.get(palavra,0)+1
   
    lista = []
    for palavra , contador in palavras.items():
        lista.append((contador,palavra))
    lista.sort(reverse=True)

    result = lista[:10]
    chavelista = []
    valorlista = []
    for chave,valor in result:
        chavelista.append(chave)
        valorlista.append(valor)
    print(result)

    plt.bar(valorlista,chavelista)
    plt.show()
    return result 
myfunction("C:\\Users\\Jk_cu\\Downloads\\lazaro.txt")   


# 2 Escreva um programa que leia um arquivo e imprima as letras
#em ordem decrescente de frequência – as letras com maior
#ocorrência primeiro. Considere:
#Converter tudo para lowercase
#Eliminar espaços, dígitos e pontuação
#Teste em vários arquivos diferentes – veja como os resultados variam.
#Compare os resultados de um arquivo com o de outro arquivo.
#Compare os resultados que você conseguir com a tabela disponível na
#Wikipedia - https://pt.wikipedia.org/wiki/Frequência_de_letras

import string
import matplotlib.pyplot as plt

def mycontaletra(caminho):
    file = open (caminho, encoding='ANSI')
    conta_letra = dict()
    for linha in file:
        linha = linha.lower().translate(str.maketrans('','',string.punctuation+''+string.digits)).strip() 
        for letra in linha:
            conta_letra[letra] = conta_letra.get(letra,0)+1
    
    return conta_letra   

def grafico(caminho):
    conta_letra = mycontaletra(caminho)
    conta_lim = []
    for key , value in conta_letra.items():
        if value < 500 :
            conta_lim.append(key)

    for item in conta_lim:
        del conta_letra[item]   

    plt.bar(conta_letra.keys(), conta_letra.values())   
    plt.show()

mycontaletra('C:\\Users\\Jk_cu\\Downloads\\lazaro.txt')
grafico('C:\\Users\\Jk_cu\\Downloads\\lazaro.txt')          
   

# obs ================================================================== ex 1 correcao 

'''import Ex07Solucao3 as ex
import matplotlib.pyplot as plt

dictionary = ex.carregarArquivo('python\\data\\A alma do lazaro.txt')

lista = []
for palavra, contador in dictionary.items():
    lista.append((contador, palavra))

lista.sort(reverse=True)

result = lista[:10]
keylist = []
valuelist = []
for contador, palavra in result:
    keylist.append(palavra)
    valuelist.append(contador)

plt.bar(keylist, valuelist)
fig, ax = plt.bar(keylist, valuelist)

plt.show()'''













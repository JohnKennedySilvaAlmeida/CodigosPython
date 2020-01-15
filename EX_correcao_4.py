import string

file = open ('C:\\Users\\Jk_cu\\Downloads\\lazaro.txt', encoding='ANSI')

import string
import matplotlib.pyplot as plt

def carregarArquivo():
    #01 questao -------------------------------------------------------------------
    file = open("python\\data\\A alma do lazaro.txt", encoding="ANSI")
    palavras = dict() #vazio
    #para cada linha no arquivo 
    for linha in file:
        linha = linha.upper().translate(str.maketrans('', '', string.punctuation+' '))
        lista_palavras = linha.split()
        #para cada palavra na linha
        for palavra in lista_palavras:
            palavras[palavra] = palavras.get(palavra,0) + 1

    return palavras

def maiorPalavra(palavras):
    #02 quesstao ===========================================
    maior_valor = 0
    maior_palavra = ''
    for palavra, valor in palavras.items():
        if valor > maior_valor:
            maior_valor = valor
            maior_palavra = palavra

    print('A palavra que mais aparece no texto é {} {} vezes'.format(
        maior_palavra, maior_valor))
    return palavras

def imprimirGrafico():
    palavras = carregarArquivo()
    palavras = maiorPalavra(palavras)
    #03 questao ===========================================
    eliminar = []
    for key, value in palavras.items():
        if value < 50:
            eliminar.append(key)
    
    for item in eliminar:
        del palavras[item]

    plt.bar(palavras.keys(), palavras.values())
    plt.show()  
    
imprimirGrafico()


#================================ outra parte do ex 4 e 5 

import string
import matplotlib.pyplot as plt

def carregarArquivo(caminho):
    file = open(caminho, encoding="ANSI")
    letras = dict() #vazio
    #para cada linha no arquivo 
    for linha in file:
        linha = linha.lower().translate(str.maketrans('', '', string.punctuation+' '+string.digits))
        #para cada letra na string
        for letra in linha:
            letras[letra] = letras.get(letra,0) + 1

    return letras

def imprimirGrafico(caminho):
    letras = carregarArquivo(caminho)
    eliminar = []
    for key, value in letras.items():
        if value < 500:
            eliminar.append(key)
    
    for item in eliminar:
        del letras[item]

    plt.bar(letras.keys(), letras.values())
    plt.show()  
    
imprimirGrafico("python\\data\\A alma do lazaro.txt")
imprimirGrafico("python\\data\\O banqueiro anarquista.txt")
imprimirGrafico("python\\data\\Papeis Avulsos.txt")
  


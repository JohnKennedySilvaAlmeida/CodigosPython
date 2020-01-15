# 1 Carregue um arquivo texto e conte as palavras do arquivo, usando dictionary.
import string

file = open ('C:\\Users\\Jk_cu\\Downloads\\lazaro.txt', encoding='ANSI')

dic_palavras = dict()

for linha  in file:
    linha = linha.upper().translate(str.maketrans('','',string.punctuation))      #obs !         
    lista_palavras = linha.split()

    for palavra in lista_palavras:
        dic_palavras[palavra] = dic_palavras.get(palavra,0)+1

print(dic_palavras)   

#2 Imprima a palavra que mais aparece no arquivo (aquela que tem a contagem maior).

maior_valor = 0
maior_palavra =""

for palavra, valor in dic_palavras.items():
    if valor > maior_valor:
        maior_valor = valor
        maior_palavra = palavra

print(f'A palavra {maior_palavra} aparece {maior_valor}')        


# 3 Gere um gráfico mostrando o número de vezes que cada palavra apareceu no arquivo (com matplotlib)

# 4 Carregue um arquivo texto e conte as letras que aparecem no arquivo. Considere:
#Converter tudo para lowercase
#Eliminar espaços, números, pontuação
#Teste com vários arquivos diferentes – veja como os resultados variam,
#compare os resultados de um arquivo com o de outro arquivo. As letras que
#mais se repetem são as mesmas?

# 5 Gere um gráfico de pizza usando as letras e sua respectiva contagem (com matplotlib)




#com funcoes 
#Carregue um arquivo texto e conte as palavras do arquivo, usando dictionary.
# 1
import  matplotlib.pyplot as plt
import string
def AbrirArquivo():
    file = open('C:\\Users\\Marcos\\Desktop\\O Banqueiro Anarquista.txt ')
    Dictionary = dict()
    for linha in file:
        linha = linha.upper().translate(str.maketrans('','', string.punctuation))
        Lista_Palavra = linha.split()
        for Palavra in Lista_Palavra:
            Dictionary[Palavra] = Dictionary.get(Palavra,0) +1

    return Dictionary
# 2
def MaiorPalavra():
    Maior_Valor = 0
    Maior_Palavra = ''
    for Palavra, valor in Dictionary.items():
        if valor > Maior_Valor:
            Maior_Valor = valor
            Maior_Palavra = Palavra
    print(f'A Palavra que mais aparece no Texto è: ({Maior_Palavra}) em {Maior_Valor} Vezes')

# 3
def ImprimirGrafico():
    Dictionary = AbrirArquivo()
    eliminar = []
    for key, value in Dictionary.items():
        if value < 50:
            eliminar.append(key)
    for item in eliminar:
        del Dictionary[item]
    plt.bar(Dictionary.keys(), Dictionary.values())
    plt.show()


ImprimirGrafico()

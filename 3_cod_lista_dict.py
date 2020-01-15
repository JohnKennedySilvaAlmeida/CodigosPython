dicionario = dict()
print(dicionario)

dicionario = {'chave':'valor'} #dict
print(len(dicionario))

listaa = ['valor']
print(len(listaa))# lista 

dicionario = {'cod00':'arroz','cod01':'fejao','cod02':'oleo'} # 3 elementos  e posicao começa do 0 
dicionario['cod00'] = 'catuaba'
print(dicionario)

icionario = {'cod00':'arroz','cod01':'fejao','cod02':'oleo'} # 3 elementos  e posicao começa do 0 
dicionario['cod02'] = 'brigadeiroS' #torcar pelo codigo
print(dicionario)

dicionario['cod09'] = 'Tangerina' # adiconar 
print(dicionario)

dicionario.get('cod00')

produto = {'001':'coca cola 350ml'} # [] ?
produto_cupom = {'001':produto}                        

produto = {'coca cola 350ml',15.88} # [] ?        Dict
produto_cupom['001'] = produto 

produto_cupom['001'][0] # mostra descricao d produto
produto_cupom['001'][1]

l = {'1':'coco','2':'aabacaxi'}
l.append = (True)
l.append = (1000) # ()
l.append = (10.5)
l.append = ([10,5,33])


#del xxx [] exclui 
#xx.pop() exclui
# xx = x.copy() copiar 
#xx.clear() eclui tudo

# dic_
#xx = xx.values()
#sort.xx
#xx = xx.keys()

#for key ,value in dic_frutas.items():              # pesquisa 
  #  print(key,value)

# if "goiaba" in dicionario:         # pesquisaa           a = 'ad' in xx{}


            #set
#dic_frutas.get('a','nao encontrado')        # busca pelo indece
#dic_frutas['a']


 
# palavra = 'asdsafsdgagafg'             contar palavras numa  lista e criar lista {} []
# d= dict()      # {}

#for letra in palavra:
   # if letra not in d:
        #d[letra] = 1
    #else:
       # d[letra] = d [letra] + 1

#print(d)

#d.clear()
# outra forma ------------------------------- de fazer 

#for letra in palavra:
       # d[letra] = d.get(letra,0) + 1

#print(d)

#d.clear()


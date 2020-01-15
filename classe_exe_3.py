# get retorna - pega 
# set atribuir - um valor 

# self.setPressao(pressa)    init   exemplo
 
class Pessoa(object):
    
    def __init__(self, nome, idade, salario):
        self.__nome = nome
        self.__idade = idade
        self.__salario = salario

    def nomeGet(self):
        return self.__nome

    def nomeSet(self, nome):
        self.__nome = nome

    def idadeGet(self):
        return self.__idade

    def idadeSet(self, idade):
        self.__idade = idade

    def salarioGet(self):
        return self.__salario

    def salarioSet(self, salario):
        self.__salario = salario

#ex -----------------==================----------------------
class Cliente:
    def __init__(self,nome,email,telefone,credito):
        self.__email = email
        self.__telefone = telefone
        self.nome = nome
        self.credito = credito


    @property
    def credito(self): return self.__credito

    @credito.setter
    def credito(self,Novocredito): self.__credito = Novocredito

    @property
    def nome(self): return self.__nome

    @nome.setter
    def nome(self,novoNome): self.__nome = novoNome



# exemplos get e set ============================================================================

# construtor 
class Automovel:
    def __init__(self, marcha, embreagem, pneus,nome):
        self.setMarcha(marcha)
        self.setEmbreagem(embreagem)
        self.setPneus(pneus)
        self.setkmRodado(self.Carregar('c\\ex\\meeuu.txt')) #obs   #exemplo 
        self.setNome(nome)

    def setNome(self,novoNome): self.__nome = novoNome

    def getNome(self): return self.__nome         

    def setMarcha(self,novaMarcha): self.__marcha = novaMarcha

    def getMarcha(self): return self.__marcha

    def setEmbreagem(self,novaEmbreagem): self.__embreagem = novaEmbreagem

    def getEmbreagem(self): return self.__embreagem

    def setPneus(self,novosPenus): self.__pneus = novosPenus

    def getPeneus(self): return self.__pneus

    def setkmRodado(self,novokmRodado): self.__kmRodado += novokmRodado

    def getkmRodado(self):
         # print(f'O automovel já rodou {self.kmRodado} km ...')  
        return self.__kmRodado # ou self.getkmRodado ?
         # falt acabar ess parte 
    
    def Carregar(self,caminho):
        arquivo = open(caminho)     # abri arquivo 
        return int(arquivo.read())

    def Salvar(self,caminho):
        arquivo = open(caminho,'w')
        arquivo.write(str(self.getkmRodado))
        arquivo.close()

    def Ligar(self):
        posicao = self.getMarcha().getPosicao()
        if posicao > 0: self.getEmbreagem().pressionado()
        print('Carro ligado')   

    def AumentarMarcahar(self):
        posicao = self.getMarcha().getPosicao()   
        if posicao < 5: 
            self.getEmbreagem().pressionado()
            novaMarcha = posicao + 1
            self.getMarcha().posicao(novaMarcha)

    def ReduzirMarchar(self):
        if self.getMarcha().posicao -1:
            self.getEmbreagem().pressionado()
            self.getMarcha().posicao -= 1
            print(f'O carro está na marcha {self.getMarcha().posicao}')  
        else:
            print('O carro está marcha Ré... ')          
      


class Embreagem:
    def __init__(self, pressionado): #Self é a instância
        self.setPressionado(pressionado)

    def setPressionado(self,novoPresionado): self.__pressionado = novoPresionado
        
    def getPressionado(self): return self.__pressionado       
    
    
class Cambio:
    def __init__(self, posicao):
        self.setPosicao(posicao)

    def setPosicao(self, NovaPosicao): self.__posicao = NovaPosicao

    def getPosicao(self): return self.__posicao    

class Pneu:
    def __init__(self, pressao, balanceado):
        self.setPressao(pressao)
        self.setBalanceado(balanceado)

    def setPressao(self,novaPressao): self.__pressao = novaPressao

    def getPressao(self): return self.__pressao     
    
    def setBalanceado(self, balanceado): self.__balanceado = balanceado

    def getBalanceado(self): return self.__balanceado    






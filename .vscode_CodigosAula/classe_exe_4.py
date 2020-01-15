import pycep_correios

class Endereco:
   
    def __init__(self,cep,numero):
        self.__cep = cep
        self.__numero = numero
      

    def setRua(self,rua): self.__rua = rua

    def getRua(self): return self.__rua

    def setNumero(self,numero): self.__numero = numero

    def getNumero(self): return self.__numero

    def setCep(self,cep): self.__cep = cep

    def getCep(self): return self.__cep

    def setCidade(self,cidade): self.__cidade = cidade

    def getCidade(self): return self.__cidade

    def setEstado(self,estado): self.__estado = estado

    def getEstado(self): return self.__estado

    def endereco(self,cep):
        return self.__cep

    def carregar(self,cep):
        endereco = pycep_correios.consultar_cep(cep)
        setCidade = endereco['Cidade']
        setEstado = endereco['Estado']



# exemplos d classe ================================================

class Nó:
   esquerda, direita, valor = None, None, 0

   def __init__(self, valor):
     # construtor dos valores
     self.esquerda = None
     self.direita = None
     self.valor = valor

class Ordenação:
   def __init__(self):
     # inicializa a raiz da árvore
     self.raiz = None

   def AdicionaNo(self, valor):
     return Nó(valor)

   def Inserir(self, raiz, valor):
     # inserir novo valor
     if raiz == None:
         # não há nenhum valor
         return self.AdicionaNo(valor)
     else:
         # já está na árvore
         if valor <= raiz.valor:
            # se os dados forem menores do que os armazenados
            # entra na sub-árvore do lado esquerdo
            raiz.esquerda = self.Inserir (raiz.esquerda, valor)
         else:
            # entra na sub-árvore do lado direito
            raiz.direita = self.Inserir (raiz.direita, valor)
         return raiz


# =============================== classe 

class A:
   a = 1 # atributo publico
   __b = 2 # atributo privado a class A

class B(A):
   __c = 3 # atributo privado
   
   def __init__(self):
     print (self.a)
     print (self.__c)

a = A()
print (isinstance(a, B)) # ''Objeto a'' é uma instância da ''classe B''? Falso.

a = B() # Instancía o ''objeto a'' na ''classe B'' e imprime os atributos da classe.
print (isinstance(a, B)) # ''Objeto a'' é uma instância da ''classe B''?Verdadeiro.

b = B() # Instancía o ''objeto b'' na ''classe B'' e imprime os atributos da classe.
print (isinstance(b, B)) # ''Objeto b'' é uma instância da ''classe B''? Verdadeiro.

b = A() # Instancía o ''objeto b'' na ''classe A''.
print (isinstance(b, A)) # ''Objeto b'' é uma instância da ''classe A''? Verdadeiro.


# ========================================= classe ======

#Atributos da classe

class Carro(object):
   estado = "novo"

print(Carro.estado) # 'novo'

c = Carro()
print('*',c.estado) 

# ================================================ classe

#Podemos alterar as propriedades através dos métodos.
class Carro1(object):
    estado = "novos"
   
    def dirigir(self):
        self.estado = "usados"

#
# 1 exemplo
#
porsche = Carro1()
porsche.dirigir()
print(porsche.estado) # usado

#
# 2 exemplo
#
ferrari = Carro1()
print(ferrari.estado) # novo

# ---------------- class ----------------============================

#Método construtor __init__
class Carro2(object):
    def __init__(self, estado):
        self.estado = estado

bmw = Carro2('semi-novo')
print(bmw.estado) # 'semi-novo'

# classs =======================================================================

# herancça
class Veiculo(object):
    estado = "novooo"

class Carro5(Veiculo):
    pass

bmw = Carro5()
print(bmw.estado) # 'novo'

#Em outras palavras, podemos definir as propriedades dinamicamente.

class Carro(object):
    pass

Fusca = Carro()
Fusca.estado = "     novo"
print(Fusca.estado) # novo

#O atributo definido dessa forma é considerado da instância.

## ------------============================= classeee ================




    
    
    
    

    
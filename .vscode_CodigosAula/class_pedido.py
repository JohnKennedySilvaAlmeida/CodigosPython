from class_itempedido  import ItemPedido
from datetime import date # data 

class Pedido:

    def __init__(self,cliente):
        self.cliente = cliente
        self.itens = [] #pra inicializar e criar 
        self.data = date.today() # imprimir date

    @property
    def cliente(self): return self.__cliente

    @cliente.setter
    def cliente(self,novocliente): self.__cliente = novocliente

    @property
    def data(self): return self.__data

    @data.setter
    def data(self,novadata): self.__data = novadata   

    @property
    def itens(self): return self.__itens

    @itens.setter
    def itens(self,itens): self.__itens = itens

    def adicionarItem(self,codigo,descricao,quantidade,preco):
        item = ItemPedido(codigo,descricao,quantidade,preco)
        if hasattr(self,'_Pedido__Itens') == False:
            self.itens = []
        self.itens.append(item)

    def removerItem(self,codigo):
        deletaritem =''
        for item in self.itens:
            if item.codigo == codigo:
                deletaritem = item
                break
        self.itens.remove(deletaritem)        

    def getTotal(self):   
        total = 0
        for item in self.itens:
            total += item.quantidade * item.preco
        return total  

    def imprimir(self):
        #cabeçalho
        print("Pedido da loja Startup SA")
        print("*"*50)
        print("="*50)
        #dados do cliente
        print("Dados do Cliente")
        print("Nome: {}".format(self.cliente.nome))
        print("CPF: {}".format(self.cliente.cpf))
        print("Endereco: {}, {}".format(self.cliente.endereco.getRua(), self.cliente.endereco.getNumero()))
        print("Cidade: {} - {}".format(self.cliente.endereco.getCidade(), self.cliente.endereco.getEstado()))
        print("*"*50)
        print("="*50)
        #itens do pedido
        print("Itens do Pedido")
        print("Codigo - Descricao - Quantidade - Preco Unitário(R$)")
        for item in self.itens:
            print("{} - {} - {} - {:.2f}".format(item.codigo,
                item.descricao,
                item.quantidade,
                item.preco))
        #total do pedido
        print("*"*50)
        print("="*50)
        print("Total do pedido:     {:.2f}".format(self.getTotal()))

        



from Contato import Contato

class Contatos:

    def __init__(self,contato):
        self.listaContatos = []
        self.contato = contato
    
    @property
    def contato(self):
        return self.__contato

    @contato.setter
    def contato(self,novocontato):
        self.__contato=novocontato

    @property
    def listaContatos(self):
        return self.__listaContatos

    @listaContatos.setter
    def listaContatos(self,novolistaContatos):
        self.__listaContatos=novolistaContatos
        
    #lista existente
    def Contatos(self):
       print("lista dos contatos")
       for i in self.listaContatos: 
            print(f'{i.Nome} - {i.Apelido} - {i.Telefone} - {i.Online}')

    def Adicionar(self,Nome, Apelido, Telefone, Online):
        item = Contato(Nome, Apelido, Telefone, Online)
        self.__listaContatos.append(item)
        print("Contato adicionado com sucesso!!")
        
    def Remover(self,Nome):
        itemParaDeletar = ""
        for i in self.__listaContatos:
            if i.Nome == Nome:
                itemParaDeletar = i
                print(f'{i.Nome} foi removido da conversa')
                break

        self.__listaContatos.remove(itemParaDeletar) 

    def Consultar(self,Nome):
        for i in self.listaContatos: 
            #Consulta pelo telefone: or i.Telefone == Telefone
            if i.Nome == Nome:
                return i

        print(f"{Nome} não foi encontrado")
        return None
                

         
        
        

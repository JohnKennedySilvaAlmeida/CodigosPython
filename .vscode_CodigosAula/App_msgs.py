from Contato import Contato
from Usuario import Usuario
from Contatos import Contatos
from Conversa import Conversa
from Mensagem import Mensagem

print('1')
#1 Criar usuário
#constructor user/contact
Contact=Contato('John','Aripower','3333-7213',True)
myUser=Usuario('John','Aripower','3333-7213',True)
print(myUser.Nome)

print('2')
#2 Criar lista de contatos (adicionar ao menos três contatos)
#constructor contacts(contact)
myContacts = Contatos(Contact)
myContacts.Adicionar('AAA','henryxD','9999-9999',True)
myContacts.Adicionar('BBB','henryxD','9999-9999',True)
myContacts.Adicionar('CCC','henryxD','9999-9999',False)
myContacts.Contatos()

print('3')
#3 Criar conversa
#constructor chat
myUser1=Usuario('user1','test','4444-4444',True)
msg=Conversa(myUser1.Nome,'A','B')
msg.Conversa(None)

print('4')
#4 Adicionar participantes na conversa
msg.adicionarParticipante(myContacts.Consultar('AAA'))

print('5')
#5 Criar mensagem
chat='Mensagem teste' 
date='1999/13/13'
text = Mensagem(chat,date)
print(chat)

print('6/7')
#6/7 Adicionar texto (imagem, áudio ou vídeo opcional) na mensagem/ Enviar mensagem  
# constructor text = Mensagem('texto pré determinado :/','1999/13/13')
msg.enviarMensagem(text)

print('8')
#8 Receber mensagem (texto fixo, pra simular o recebimento)
msg.receberMensagem()
#1 user na gravação
msg.gravarConversa('teste.txt',text.Texto,text.Data)

print('9')
#9 Adicionar novo contato à lista de contatos
myContacts.Adicionar('DDD','henryxD','9999-9999',False)

print('10')
#10 Adicionar participante na conversa
msg.adicionarParticipante(myContacts.Consultar('BBB'))
msg.Conversa(None)

print('11')
#11 Remover outro participante da conversa
# Exe inicial:removerPartipante|Extra porque não foi pedido!!. 
msg.removerParticipante(myContacts.Consultar('AAA'))
msg.Conversa(None)
myContacts.Remover('AAA')

print('12')
#12 Gravar conversa em arquivo
msg.Conversa('BBB')
chat='certamente nao e uma conversa' 
date=''
text = Mensagem(chat,date)
msg.enviarMensagem(text)
msg.receberMensagem()
text.Data
msg.gravarConversa('teste.txt',text.Texto,text.Data)


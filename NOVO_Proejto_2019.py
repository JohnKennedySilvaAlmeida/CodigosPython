# CHATBOT Program

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

try:

    bot = ChatBot('TW Chat Bot')

    conversa = [
    'Oi',
    'Olá', 
    'Tudo bem?', 
    'Tudo ótimo', 
    'Você gosta de programar?',
    'Sim, eu programo em Python',
    'Sim',
    'não',
    'depende',
    'talvez',
    'queria',
    'vida e boa',
                ]

    bot.set_trainer(ListTrainer)
    bot.train(conversa)

    while True:
        pergunta = input("Usuário (Vc): ")
        resposta = bot.get_response(pergunta)
        if float(resposta.confidence) > 0.5:
            print('*TW Bot (Bia): ', resposta)
        else:
            print('*TW Bot (Bia): Ainda não sei responder esta pergunta')

except:
    print('...! Algum Erro No Sistema !...')     
finally:
    print('Finalizando... Good Bye')            


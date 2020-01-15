# clsss

from datetime import time, timedelta, date, datetime
    
class Participante:

    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    @property
    def nome (self):
        return self.__nome
    
    @property 
    def email (self):
        return self.__email

class Sala:
    def __init__(self, codigo, descricao):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__disponibilidade = dict() #hora, True/False

        t = timedelta(hours=8) #início do expediente

        for d in range(10):
            t2 = timedelta(hours=d)
            self.__disponibilidade[t+t2] = True
            
    @property
    def codigo (self):
        return self.__codigo

    @property
    def descricao (self):
        return self.__descricao
    
    def reservar (self, horario):
        #verificar se o horário está disponivel
        if self.__disponibilidade[horario] == True: 
            #marcar como reservado mudando para disponível = False
            self.__disponibilidade[horario] = False 
            #retornar True para confirmar que a reserva foi efetuada
            return True
        else:
            #retornar False para mostrar que não foi realizada a reserva
            return False            

    def listarHorarios (self):
        for t, d in self.__disponibilidade.items():
            if d == True:
                print(t)

class Reuniao:

    def __init__(self, descricao):
        self.__descricao = descricao
        self.__participantes = []
    
    def marcar(self, sala, inicio, fim):
        self.__inicio = inicio #datetime
        self.__fim = fim #datetime
        novoHorario = inicio.hour  #obs!  
        while True:
            novoHorario = timedelta(hours=novoHorario)
            if sala.reservar(novoHorario):
                self.__sala = sala
                break
            else:
                print("Horário já reservado, tente outro horário")
                sala.listarHorarios()
                novoHorario = input("Digite horario: ")

    def addParticipante(self, participante):
        self.__participantes.append(participante)


## App ------------------------------------------------------------ 

'''
*OBS ->    __all_ = ["classes", "Sala", "Reuniao", "Participante"]  -> comando *


from classes import *
from datetime import datetime '''


minhaReuniao = Reuniao("Prova final de POO")

lab012 = Sala("012", "Laboratório de Informatica")
inicio = datetime.strptime("19/11/2018 18:00", "%d/%m/%Y %H:%M")
fim = datetime(2018, 11, 19, 19, 0)

minhaReuniao.marcar(lab012, inicio, fim)

minhaReuniao.addParticipante(Participante("Waldemar", "roberti@weg.net"))
minhaReuniao.addParticipante(Participante("Joao", "joao@weg.net"))
minhaReuniao.addParticipante(Participante("Marcos", "marcos@weg.net"))





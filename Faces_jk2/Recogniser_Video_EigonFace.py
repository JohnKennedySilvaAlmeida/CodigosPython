#3 passo

import cv2                                    # opencv
import NameFind                               #função 
import time, sys 
import smtplib

    #   importe as cascatas de Haar para a ditecção de rosto e olhos

face_cascade = cv2.CascadeClassifier('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Haar\\haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Haar\\haarcascade_eye.xml')

recognise = cv2.face.EigenFaceRecognizer_create(15,4000)  # criando EIGEN FACE RECOGNISER
                               
recognise.read('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Recogniser\\trainingDataEigan.xml') # Carregue os dados de treinamento

def email():
    #import smtplib
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #Gmail	smtp.gmail.com	SSL	465
    #Gmail	smtp.gmail.com	StartTLS	587
    #Hotmail	smtp.live.com	SSL	465
    #Mail.com	smtp.mail.com	SSL	465
    #Outlook.com	smtp.live.com	StartTLS	587
    #Office365.com	smtp.office365.com	StartTLS	587
    #Yahoo Mail	smtp.mail.yahoo.com	SSL	465

    smtp.login('john.almeida@aluno.sc.senac.br', 'orlandojohn92')#senha

    de = 'john.almeida@aluno.sc.senac.br'
    para = ['marcos.regis@aluno.sc.senac.br']
    msg = """From: %s
    To: %s
    Subject: Test

    Outro codigo.""" % (de, ', '.join(para))

    smtp.sendmail(de, para, msg)

    smtp.quit()

# -------------------------    INICIAR O VIDEO -----------------------------------------

cap = cv2.VideoCapture(0)              # Objeto da câmera

ID = 0

while True:
    ret, img = cap.read()                                                       #Leia o objeto da câmera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Converta a câmera em cinza
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)                         # Detecte os rostos e guarde as posições
    for (x, y, w, h) in faces:                                                  # Molduras LOCAL X, Y LARGURA, ALTURA
      
        # ------------ AO CONFIRMAR OS OLHOS, ESTÃO DENTRO DO ROSTO MELHOR RECONHECIMENTO DO ROSTO É GANHADO ------------------
        gray_face = cv2.resize((gray[y: y+h, x: x+w]), (110, 110))               # O rosto é isolado e cortado
        eyes = eye_cascade.detectMultiScale(gray_face)
        for (ex, ey, ew, eh) in eyes:
            ID, conf = recognise.predict(gray_face)                              # Determinar o ID da foto
            NAME = NameFind.ID2Name(ID, conf)#Função
            NameFind.DispID(x, y, w, h, NAME, gray)#funcão
   
    cv2.imshow('Sistema de Reconhecimento Facial', gray)                       # Mostre o vídeo
        #Sistema de Reconhecimento Facial EigenFace

    if cv2.waitKey(1) & 0xFF == ord('s' or 'S'):                                       #Sair s ou S
        email()#notificar
        break

cap.release()
cv2.destroyAllWindows()

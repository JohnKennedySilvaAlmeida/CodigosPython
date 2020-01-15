#Teste Por etapas

import cv2
import matplotlib.pyplot as plt
import numpy as np


def detecção_Faces():

    arqCasc = 'haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(arqCasc)
    
    webcam = cv2.VideoCapture(0)  #instancia o uso da webcam
    
    while True:
        s, imagem = webcam.read() #pega efeticamente a imagem da webcam
        imagem = cv2.flip(imagem,180) #espelha a imagem
    
        faces = faceCascade.detectMultiScale(
            imagem,
            minNeighbors=5,
            minSize=(30, 30),
        maxSize=(200,200)
        )
    
        # Desenha um retângulo nas faces detectadas
        for (x, y, w, h) in faces:
            #cv2.putText(imagem,'Leon',(x - 20,y + h + 60), font, 3,(255,0,0),5,cv2.LINE_AA)
            cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
        cv2.imshow('Video', imagem) #mostra a imagem captura na janela
    
        #o trecho seguinte é apenas para parar o código e fechar a janela
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    webcam.release() #dispensa o uso da webcam
    cv2.destroyAllWindows() #fecha todas a janelas abertas


#https://www.youtube.com/user/jaumzexpatinete/videos ----------------------------------------------------
#import numpy as np
#import cv2

def detecção_Faces_Olhos():

    def AddName():
        Name = input('Seu nome: ')      # abrir nomes no arquivo txt
        Info = open("C:/Users/Jk_cu/OneDrive/Área de Trabalho/J k/Programs python JK/Master_Face/Names.txt", "r+")
        ID = ((sum(1 for line in Info))+1) #adcionar nomes 
        Info.write(str(ID) + " " + "," + " " + Name + "\n")
        print ("Nome armazenado em " + str(ID))
        Info.close()
        return ID 

    ID = AddName()
    Count = 0
   
    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    while(True):
        _, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces: # face
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(roi_gray)

            for (ex,ey,ew,eh) in eyes: #olhos
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        cv2.imshow("frame", frame)

        key = cv2.waitKey(1)

        if key == ord('s') or key == ord('S'): break  # sair	
        
        elif key == 27: break	

    cap.release()
    cv2.destroyAllWindows()


# RECONHECEDOR PARA O RECONHECEDOR DE ROSTO EIGEN 
# PARA O RECONHECIMENTO DE ROSTO TODAS AS CARAS SÃO NECESSÁRIAS PARA SER MESMO TAMANHO 


import cv2                                                                      # Importing the opencv
import NameFind
#from Recogniser import *

#   import the Haar cascades for face and eye ditection

face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalcatface.xml') # Classifier "frontal-face" Haar Cascade
eye_cascade = cv2.CascadeClassifier('Haar/haarcascade_eye.xml') # Classifier "eye" Haar Cascade

recogniser = cv2.face.EigenFaceRecognizer_create(15,4000)  # criando EIGEN FACE RECOGNISER
recogniser.read('Recogniser/trainingDataEigan.xml')                              # Carregue os dados de treinamento

# ------------------------- INICIAR O VIDEO FEED -------------------------------------------
cap = cv2.VideoCapture(0)                                                       # Camera object
# cap = cv2.VideoCapture('TestVid.wmv')   # Video object
ID = 0
while True:
    ret, img = cap.read()                                                       # Leia o objeto da câmera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Converta a câmera em cinza
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)                         # Detecte os rostos e guarde as posições
    for (x, y, w, h) in faces:                                                  # Molduras LOCAL X, Y LARGURA, ALTURA
        #------------ AO CONFIRMAR OS OLHOS ESTÃO DENTRO DO ROSTO MELHOR RECONHECIMENTO DE ROSTO É GANHADO ------------------
        gray_face = cv2.resize((gray[y: y+h, x: x+w]), (110, 110))               # O rosto é isolado e cortado
        eyes = eye_cascade.detectMultiScale(gray_face)
        for (ex, ey, ew, eh) in eyes:
            ID, conf = recognise.predict(gray_face)                              # Determinar o ID da foto
            NAME = NameFind.ID2Name(ID, conf)
            NameFind.DispID(x, y, w, h, NAME, gray)
    cv2.imshow('EigenFace Face Recognition System', gray)                       # Mostre o vídeo
    if cv2.waitKey(1) & 0xFF == ord('q'):                                       #Sair (q)
        break
        
cap.release()
cv2.destroyAllWindows()

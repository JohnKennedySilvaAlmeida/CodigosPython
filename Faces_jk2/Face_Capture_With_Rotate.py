#1 Passo    -   Obs precisa de Claridade para detectar 

import cv2                  # opencv
import numpy as np          # numpy 
import NameFind        # função


WHITE = [255, 255, 255] # tamanho 

#   importe as cascatas de Haar para a detecção de faces
face_cascade = cv2.CascadeClassifier('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Haar\\haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\Haar\\haarcascade_eye.xml')

data_SET = ('C:\\Users\\Jk_cu\\OneDrive\\Documentos\\dataSet\\Usuario.')   #Local p/ guarda as fotos

ID = NameFind.AddName()  #Id chama função
Count = 0  #contador 
cap = cv2.VideoCapture(0)                                             # Objeto da câmera

while Count < 30: # loop para tirar quantidade de fotos  [50]
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)           # Converta a câmera para grayScale
    if np.average(gray) > 110:                   # Testando o brilho da imagem
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)         # Detecte os rostos e guarde as posições
        for (x, y, w, h) in faces:             # Molduras LOCAL X, Y LARGURA, ALTURA
            FaceImage = gray[y - int(h / 2): y + int(h * 1.5), x - int(x / 2): x + int(w * 1.5)]    # O rosto é isolado e cortado
            Img = (NameFind.DetectEyes(FaceImage))
            cv2.putText(gray, "| ROSTO DETECTADO |", (x+int((w/2)), y-5), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)
            if Img is not None:
                frame = Img                      # Mostrar os rostos detectados
            else:
                frame = gray[y: y+h, x: x+w]
                cv2.imwrite(data_SET + str(ID) + "." + str(Count) + ".jpg", frame)#data_SET / gravar
                cv2.waitKey(300)
                cv2.imshow("[FOTO CAPTURADA]", frame)               # mostra a imagem capturada
                Count = Count + 1
    
    cv2.imshow('[Faces de Captura do Sistema de Reconhecimento Facial]', gray)       # Mostre o vídeo
    
    if cv2.waitKey(1) & 0xFF == ord('s' or 'S'):# sair 
        break

print ('[A CAPTURA DE FACE ESTÁ COMPLETA]')

cap.release()
cv2.destroyAllWindows()

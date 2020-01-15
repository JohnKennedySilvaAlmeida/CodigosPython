
#Teste por partes 

import numpy as np
import cv2

def detecção_Faces_Olhos():
    
    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    while(True):
        _, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        font = cv2.FONT_HERSHEY_SIMPLEX

        for (x,y,w,h) in faces: # face
            cv2.putText(frame,'Capture',(x - 20,y + h + 63), font, 1,(255,0,0),5,cv2.LINE_AA)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(roi_gray)

            for (ex,ey,ew,eh) in eyes: #olhos
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        cv2.imshow('frame', frame)

        key = cv2.waitKey(1)

        if key == ord('s') or key == ord('S'): break  # sair	
        
        elif key == 27: break	

    cap.release()
    cv2.destroyAllWindows()

#import cv2
#import numpy as np

def detecção_Faces_Olhos_1():

    classificador = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    classificadorOlho = cv2.CascadeClassifier("haarcascade_eye.xml")


    camera = cv2.VideoCapture(0)
    amostra=1
    numeroAmostra=20
    id = input('Digite seu identificador: ')
    largura,altura = 220 ,220

    print("Capture ...")

    while (True):
        conectado,imagem = camera.read()
        imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        print(np.average(imagemCinza))
        facesDetectadas = classificador.detectMultiScale(imagemCinza,
                                                        scaleFactor=1.5,
                                                        minSize=(150,150))


        for(x,y,l,a) in facesDetectadas:

            cv2.rectangle(imagem, (x,y),(x+l,y+a), (0,0,255),2)
            regiao = imagem[y:y + a , x:x +l]
            regiaoCinzaOlho = cv2.cvtColor(regiao,cv2.COLOR_BGR2GRAY)
            olhosDetectado = classificador.detectMultiScale(regiaoCinzaOlho)

            for(ox. oy, ol, oa) in olhosDetectado:
                cv2.rectangle(regiao, (ox,oy), (ox + ol , oy + oa), (0,255,0),2)

                if cv2.waitKey(1)& 0xFF == ord('q'):
                    if np.average(imagemCinza) > 100:
                        imagemFace = cv2.resize(imagemCinza[y:y+a,x:x +l], (largura,altura))
                        cv2.imwrite("fotos1/pessoa. " + str(id) + "." +str(amostra) + ".jpg", imagemFace)
                        print("[ foto " + str(amostra) + " Capturada com sucesso ]" )
                        amostra +=1


        cv2.imshow("Face",imagem)
        cv2.waitKey(1)

        if(amostra >= numeroAmostra +1 ):
            break

    print("faces detectada com sucesso")
    camera.release()
    cv2.destroyAllWindows()





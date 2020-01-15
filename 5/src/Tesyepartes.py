'''import  numpy  as  np 
import  cv2

img  =  cv2.imread ( 'messi5.jpg' , 0 ) 
cv2.imshow ( 'imagem' , img ) 
k  =  cv2.waitKey ( 0 ) 

if  k  ==  27 :          # espera pela tecla ESC para sair do 
    cv2.destroyAllWindows () 
elif  k  ==  ord ( 's' ):  # espera pela tecla 's' para salvar e sair do 
    cv2.imwrite ( 'messigray.png' ,img ) 
    cv2.destroyAllWindows ()


#parte

import cv2
 
# ler imagem como escala de cinza
grey_img = cv2.imread('/home/img/python.png', cv2.IMREAD_GRAYSCALE)
 
# salvar imagem
status = cv2.imwrite('/home/img/python_grey.png',grey_img)
print("imagem gravada no sistema de arquivos: ",status)	
'''

import cv2

cpt = 0
maxFrames = 5 # if you want 5 frames only.

try:
    vidStream = cv2.VideoCapture(0) # index of your camera
except:
    print ("problem opening input stream")
    sys.exit(1)

while cpt < maxFrames:
    ret, frame = vidStream.read() # read frame and return code.
    if not ret: # if return code is bad, abort.
        sys.exit(0)
    cv2.imshow("test window", frame) # show image in window
    cv2.imwrite("image%04i.jpg" %cpt, frame)
    cpt += 1
import cv2
import time
#import sys

def main(args):
 
    camera_port = 0
  
    nFrames = 30
  
    camera = cv2.VideoCapture(camera_port)
     
    #file = "/home/tavares/imagenTeste.png"
    #file = r"C:\Users\Jk_cu\OneDrive\Área de Trabalho\J k\Programs python JK\5\src\fotos\pessoa.png"
    #file = 'fotos/Pessoas.jpg'  
    file = 'c:/Users/Jk_cu/OneDrive/Área de Trabalho/J k/Programs python JK/5/src/fotos/F.png'  
         
    print ("Digite <ESC> para sair / <s> para Salvar")   
     
    emLoop= True
      
    while(emLoop):
     
        retval, img = camera.read()
        cv2.imshow('Foto',img)
     
        k = cv2.waitKey(100)
     
        if k == 27:
            emLoop= False
         
        if k == ord('s'):
            status = cv2.imwrite(file,img)
           #cv2.imshow(file, img)
            print('Estatus',status)
            emLoop= False

    return 0
 
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    

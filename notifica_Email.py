import smtplib #email
from email.mime.text import MIMEText

# conexão com os servidores do google
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
# username ou email para logar no servidor
username = 'john.almeida@aluno.sc.senac.br'
password = 'johnkennedy'

from_addr = 'john.almeida@aluno.sc.senac.br'
to_addrs = ['bruno.enke@aluno.sc.senac.br']

# a biblioteca email possuí vários templates
# para diferentes formatos de mensagem
# neste caso usaremos MIMEText para enviar
# somente texto
message = MIMEText('Hello World')
message['subject'] = 'Teste'
message['from'] = from_addr
message['to'] = ', '.join(to_addrs)

# conectaremos de forma segura usando SSL
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
# para interagir com um servidor externo precisaremos
# fazer login nele
server.login(username, password)
server.sendmail(from_addr, to_addrs, message.as_string())
server.quit()




'''
#outro cod =================---------------------------------------------------
import time
import smtplib

EMAIL_ADDRESS = "john.almeida@aluno.sc.senac.br" # seu email 
PASSWORD = "xxx" #sua senha 

tempo = time.localtime()


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        #server = smtplib.SMTP('smtp.hotmail.com:25')  portas  =   #25 or 465 smtp.live.com /  587 se a 25 ?
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)
        server.quit()
        print("Sucesso: email enviado!")
    except:
        print("Email falhou ao enviar.")


subject = " Testando .... "
#msg = ("Olha eu aqui"*20)

msg = (f"Sua Entrada foi autorizada hoje dia {tempo.tm_mday}/{tempo.tm_mon}/{tempo.tm_year}")
# às {tempo.tm_hour}:{tempo.tm_min}:{tempo.tm_sec}")

send_email(subject, msg)

# funciona mas falta mehorar alguns aspectos e implementar ???  '''





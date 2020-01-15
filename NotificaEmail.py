# Notificar e mail 
# email 
import smtplib

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#Gmail	smtp.gmail.com	SSL	465
#Gmail	smtp.gmail.com	StartTLS	587
#Hotmail	smtp.live.com	SSL	465
#Mail.com	smtp.mail.com	SSL	465
#Outlook.com	smtp.live.com	StartTLS	587
#Office365.com	smtp.office365.com	StartTLS	587
#Yahoo Mail	smtp.mail.yahoo.com	SSL	465

smtp.login('john.almeida@aluno.sc.senac.br', 'johnkennedy')

de = 'john.almeida@aluno.sc.senac.br'
para = ['bruno.enke@aluno.sc.senac.br']
msg = """From: %s
To: %s
Subject: Test

Outro codigo.""" % (de, ', '.join(para))

smtp.sendmail(de, para, msg)

smtp.quit()

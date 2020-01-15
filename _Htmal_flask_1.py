#importar o pacote do servidor de aplicação
from flask import Flask

# Criar uma instância do servidor de aplicação
app = Flask(__name__)

# Método para executar quando for chamado o raiz (/)
@app.route('/')
def hello():
    mensagem = "Fala Galera"

    retorno = """<html>
        <header><title>Título da janela</title></header>
        <body>Mensagem: {0}</body>        
    </html>""".format(mensagem)

    return retorno

#Outro método
@app.route('/pedido')
def outroHello():
    return "Outra página de teste"
    
#Outro método
@app.route('/cliente')
def carregaCliente():
    return "Clientes"


# Colocar a aplicação pra rodar
if __name__ == '__main__':
    app.run()

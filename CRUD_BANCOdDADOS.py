import sqlite3

conexao = sqlite3.connect('clientes.db') #obs!! DB 

cursor = conexao.cursor()

#criar tabela cliente 
script_clientes = '''create table if not exists Clientes(Codigo integer primary key autoincrement,
nome text not null,
CPF text not null,
Telefone text not null,
Numero integer not null,
Complemento text,
Email text,
Estado_Civil text);'''

cursor.execute(script_clientes)
conexao.commit()

#criar tabela endereços 
script_endereco = '''create table if not exists Endereco(
CEP text primary key,
Rua text,
Bairro text,
Cidade text,
Estado text)'''    

cursor.execute(script_endereco)
conexao.commit()

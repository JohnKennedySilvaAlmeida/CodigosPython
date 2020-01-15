import sqlite3 

conexao = sqlite3.connect('sample.bd') #obs  BD ou DB
cursor = conexao.cursor()

cursor.execute('SELECT SQLITE_VERSION()')
dados = cursor.fetchone()
print(dados)


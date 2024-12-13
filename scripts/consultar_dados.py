import sqlite3

conexao = sqlite3.connect('../credito.db')
cursor = conexao.cursor()

cursor.execute("SELECT * FROM clientes;")
clientes = cursor.fetchall()

for cliente in clientes:
    print(cliente)

conexao.close()
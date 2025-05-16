import sqlite3

conexao = sqlite3.connect('../credito.db')
cursor = conexao.cursor()

def avaliar_credito(cliente):
    if cliente[3] * 0.5 >= cliente[4] and cliente[5] > 600 and cliente[2] > 21:
        return "Aprovado"
    else:
        return "Negado"

cursor.execute("SELECT * FROM clientes")
clientes = cursor.fetchall()

for cliente in clientes:
    status = avaliar_credito(cliente)
    cursor.execute(
        "UPDATE clientes SET Aprovado = ? WHERE ID_Cliente = ?",
        (status, cliente[0]))

conexao.commit()
print("Avaliação de crédito concluída!")
conexao.close()


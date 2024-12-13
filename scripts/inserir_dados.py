import sqlite3

conexao = sqlite3.connect('../credito.db')
cursor = conexao.cursor()

dados = [
    ('João Silva', 35, 5000.00, 2000.00, 750, None),
    ('Maria Oliveira', 29, 2000.00, 1500.00, 620, None),
    ('Lucas Pedro', 42, 8000.00, 5000.00, 810, None),
    ('Ana Souza', 23, 1200.00, 1000.00, 580, None),
    ('Fernanda Lima', 38, 3000.00, 2000.00, 690, None),
    ('Carlos Santos', 45, 7000.00, 4000.00, 700, None),
    ('Beatriz Almeida', 31, 4000.00, 2500.00, 650, None),
    ('Pedro Gonçalves', 50, 1000.00, 900.00, 610, None),
    ('Julia Marques', 26, 1500.00, 800.00, 590, None),
    ('Gabriel Rodrigues', 33, 4500.00, 3000.00, 780, None)
]

cursor.executemany("""
INSERT INTO clientes (Nome, Idade, Renda_Mensal, Valor_Solicitado, Score_Credito, Aprovado)
VALUES (?, ?, ?, ?, ?, ?);
""", dados)

dados = [
    ('Platinum', 'Pontos em compras, Salas VIP', 8000.00, 10000.00),
    ('Gold', 'Cashback em compras', 5000.00, 5000.00),
    ('Internacional', 'Compras internacionais', 3000.00, 3000.00),
    ('Básico', 'Sem benefícios especiais', 1000.00, 1000.00),
];

cursor.executemany("""
INSERT INTO cartoes_credito (Tipo_Cartao, Beneficios, Renda_Minima, Limite_Disponivel)
VALUES  (?, ?, ?, ?);
""", dados)

dados = [
    ('João Silva', 'joao.silva@banco.com', '(11) 99999-9999', 1),
    ('Maria Oliveira', 'maria.oliveira@banco.com', '(21) 98888-8888', 2),
    ('Lucas Pedro', 'lucas.pedro@banco.com', '(31) 97777-7777', 3),
    ('Ana Souza', 'ana.souza@banco.com', '(41) 96666-6666', 4),
]

cursor.executemany("""
INSERT INTO gerentes (Nome, Email, Telefone, ID_Cartao)
VALUES  (?, ?, ?, ?);
""", dados)

print("Dados inseridos com sucesso!")

conexao.commit()
conexao.close()

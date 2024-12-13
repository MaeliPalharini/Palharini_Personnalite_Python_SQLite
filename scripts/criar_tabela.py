import sqlite3

conexao = sqlite3.connect('../credito.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    ID_Cliente INTEGER PRIMARY KEY,
    Nome TEXT,
    Idade INTEGER,
    Renda_Mensal REAL,
    Valor_Solicitado REAL,
    Score_Credito INTEGER,
    Aprovado TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS cartoes_credito (
    ID_Cartao INTEGER PRIMARY KEY,
    Tipo_Cartao TEXT NOT NULL,
    Beneficios TEXT NOT NULL,
    Renda_Minima REAL NOT NULL,
    Limite_Disponivel REAL NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS gerentes (
    ID_Gerente INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    Telefone TEXT NOT NULL,
    ID_Cartao INTEGER NOT NULL,
    FOREIGN KEY (ID_Cartao) REFERENCES cartoes_credito(ID_Cartao)
);
""")

print("Tabelas criadas com sucesso!")
conexao.commit()
conexao.close()

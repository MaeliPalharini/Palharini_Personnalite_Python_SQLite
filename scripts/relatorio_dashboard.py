import  sqlite3
import pandas as pd
import matplotlib.pyplot as plt

import os
caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'credito.db'))
conexao = sqlite3.connect(caminho)

df = pd.read_sql_query("SELECT * FROM clientes", conexao)
resumo = df['Aprovado'].value_counts()
print(resumo)

plt.figure(figsize=(6,6))
resumo.plot.pie(autopct='%1.1f%%', colors=['green', 'red'], labels=['Aprovado', 'Negado'])
plt.title('Distribuição de Crédito')
plt.ylabel('')  # Remove o rótulo "Aprovado"
plt.tight_layout()
plt.show()

df.to_csv('relatorio_credito.csv', index=False)
print("\nRelatório salvo como relatorio_credito.csv")
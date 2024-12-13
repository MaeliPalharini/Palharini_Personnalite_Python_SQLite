# 🏦 Palharini Personnalité
Bem-vindo ao Palharini Personnalité, a solução mais sofisticada e personalizada para análise de crédito e gestão de cartões. Este projeto oferece uma experiência exclusiva e inovadora, conectando clientes às melhores oportunidades financeiras.

## 🛠️ Tecnologias Utilizadas
* Python 3.11.11

* SQLite para armazenamento de dados

* DB Browser for SQLite (opcional, para visualização gráfica)

* IDE: PyCharm

## 📌 Objetivo
Este projeto simula um sistema de análise de crédito:

1. Cria um banco de dados SQLite com clientes fictícios.
2. Avalia os clientes com base em regras pré-definidas.
3. Permite consultas SQL para visualizar os resultados (aprovados/negados).

## 📋 Funcionalidades
🌟 *Avaliação de Crédito Personalizada:*
Analisa clientes com base em critérios claros e objetivos (renda, score, idade).

💳 *Gestão de Cartões de Crédito:*
Inclui tipos de cartões com benefícios exclusivos e limites personalizados.

🧑 💼 *Gerentes Especializados:*
Cada tipo de cartão conta com um gerente dedicado.

🔎 *Consulta de Dados Avançada:*
Permite explorar clientes aprovados, tipos de cartões disponíveis e gerentes cadastrado

## 📁 Estrutura do Projeto
`criar_tabela.py` – Cria a tabela no banco de dados.
    
`inserir_dados.py` – Insere os clientes no banco.
    
`avaliar_credito.py` – Avalia os clientes com base nas regras.
    
`consultar_dados.py` – Faz consultas ao banco.

## 📁 Estrutura do Banco de Dados

### 1. Tabela `clientes`
Guarda as informações dos clientes e sua elegibilidade ao crédito.

| Coluna           | Tipo      | Descrição                             |
|-------------------|-----------|---------------------------------------|
| `ID_Cliente`      | INTEGER   | Identificador único do cliente        |
| `Nome`            | TEXT      | Nome do cliente                      |
| `Idade`           | INTEGER   | Idade do cliente                     |
| `Renda_Mensal`    | REAL      | Renda mensal do cliente              |
| `Valor_Solicitado`| REAL      | Valor do crédito solicitado          |
| `Score_Credito`   | INTEGER   | Score de crédito do cliente          |
| `Aprovado`        | TEXT      | Status de aprovação (Aprovado/Negado) |


### 2. Tabela `cartoes_credito`
Define os tipos de cartões de crédito oferecidos e seus critérios de elegibilidade.

| Coluna            | Tipo      | Descrição                                 |
|--------------------|-----------|-------------------------------------------|
| `ID_Cartao`        | INTEGER   | Identificador único do cartão             |
| `Tipo_Cartao`      | TEXT      | Nome do tipo de cartão                    |
| `Beneficios`       | TEXT      | Benefícios associados ao cartão           |
| `Renda_Minima`     | REAL      | Renda mínima exigida para o cartão        |
| `Limite_Disponivel`| REAL      | Limite de crédito disponível no cartão    |

### 📋 Regras de Aprovação do cartão

Para ser aprovado, o cliente deve atender aos seguintes critérios:

🟢 Valor solicitado: Até 50% da renda mensal.

🟢 Score de crédito: Maior que 600.

🟢 Idade: Maior que 21 anos.

### 3. Tabela `gerentes`
Guarda as informações dos gerentes responsáveis por cada tipo de cartão.

| Coluna            | Tipo      | Descrição                                  |
|--------------------|-----------|--------------------------------------------|
| `ID_Gerente`       | INTEGER   | Identificador único do gerente             |
| `Nome`             | TEXT      | Nome completo do gerente                   |
| `Email`            | TEXT      | E-mail de contato do gerente              |
| `Telefone`         | TEXT      | Telefone de contato do gerente            |
| `ID_Cartao`        | INTEGER   | Identificador do cartão gerenciado         |



## 🔗 Licença
Este projeto está licenciado sob a MIT License. Sinta-se à vontade para usar, modificar e compartilhar.

## ✨ Autora
Maeli Palharini

Apaixonada por dados, desenvolvimento e aprendizado contínuo.
📫 Contato: maeli.palharini@hotmail.com
# 🏦 Palharini Personnalité
Palharini Personnalité é um projeto pessoal desenvolvido com o objetivo de aprimorar habilidades
em Python, SQL e gestão de dados. Ele simula um sistema completo de análise de crédito e gerenciamento
de cartões, permitindo a aplicação de conceitos técnicos de desenvolvimento, banco de dados e lógica de programação.

## 🛠️ Tecnologias Utilizadas
* Python 3.11.11

* SQLite para armazenamento de dados

* Pandas e Matplotlib (relatórios e gráficos)

* DB Browser for SQLite (opcional, para visualização gráfica)

* IDE: PyCharm

## 📌 Objetivo
Simular um sistema de **análise de crédito** com base em regras específicas de aprovação. O sistema:

1. Cria um banco de dados SQLite com dados fictícios.
2. Avalia os clientes com base em regras personalizadas.
3. Permite consultas SQL manuais e automáticas.
4. Gera relatórios em `.csv` e gráficos com visualização de dados.

## 📋 Funcionalidades
🌟 *Avaliação de Crédito Personalizada:*
Analisa clientes com base em critérios claros e objetivos (renda, score, idade).

💳 *Gestão de Cartões de Crédito:*
Inclui tipos de cartões com benefícios exclusivos e limites personalizados.

🧑 💼 *Gerentes Especializados:*
Cada tipo de cartão conta com um gerente dedicado.

## 🔎 Consultas e Relatórios
- SQL para consultas manuais
- Exportação para `.csv`
- Dashboard com gráfico de pizza (pie chart) mostrando a proporção de aprovados e negados

## 📁 Estrutura do Projeto
    scripts/

    ├── criar_tabela.py # Criação das tabelas no banco
    ├── inserir_dados.py # População inicial do banco
    ├── avaliar_credito.py # Avaliação automática dos clientes
    ├── consultar_dados.py # Execução de queries no banco
    └── relatorio_dashboard.py # Geração de relatório CSV e gráfico

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

## 📊 Dashboard de Crédito

Ao rodar `relatorio_dashboard.py`, o projeto:

- Gera um gráfico de pizza com a proporção de clientes aprovados e negados
- Exporta um relatório para `relatorio_credito.csv`

## 🔗 Licença
Este projeto está licenciado sob a MIT License. Sinta-se à vontade para usar, modificar e compartilhar.

## ✨ Autora
Maeli Palharini

Apaixonada por dados, desenvolvimento e aprendizado contínuo.
📫 Contato: maeli.palharini@hotmail.com

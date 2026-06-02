# ☁️ CloudFunFacts

Uma aplicação serverless desenvolvida na AWS que gera curiosidades sobre computação em nuvem utilizando Inteligência Artificial.

---

# 🎯 Objetivo

CloudFunFacts foi criado para consolidar conhecimentos em arquitetura cloud, computação serverless, APIs REST, bancos de dados NoSQL e integração com modelos generativos utilizando serviços AWS.

O sistema busca curiosidades armazenadas no DynamoDB, envia o conteúdo para o Amazon Bedrock e retorna uma versão mais divertida e explicativa para o usuário através de uma interface web simples.

---

# 🏗️ Arquitetura

Fluxo da aplicação:

Usuário → Front-End → API Gateway → AWS Lambda → DynamoDB + Amazon Bedrock → Resposta ao Usuário

---

# 🚀 Serviços AWS Utilizados

- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon Bedrock (Claude Sonnet)
- Amazon CloudWatch

---

# 🔥 Destaques Técnicos

- Arquitetura Serverless
- API REST com API Gateway
- Funções AWS Lambda em Python
- Banco NoSQL DynamoDB
- Integração com Amazon Bedrock
- Monitoramento com CloudWatch
- Front-end consumindo API via JavaScript

---

# 📁 Estrutura do Projeto

CloudFunFacts/

├── FrontEnd/

│   └── index.html

├── Lambda/

│   └── lambda_function.py

├── Screenshots/

│   ├── frontend/

│   └── aws/

└── README.md

---

# 📸 Screenshots

## Front-End

Tela inicial da aplicação:

Front-End Inicial

Exemplo de curiosidade gerada:

Front-End Funcionando

---

## AWS Lambda

Visão geral da função Lambda:

Lambda Overview

Teste executado com sucesso:

Lambda Test

---

## API Gateway

Rota GET da API:

API Gateway Route

Stage publicado:

API Gateway Stage

---

## DynamoDB

Tabela CloudFacts:

DynamoDB Table

Itens armazenados:

DynamoDB Items

---

## Amazon Bedrock

Inference Profile utilizado:

Bedrock Inference Profile

---

## CloudWatch

Logs da aplicação:

CloudWatch Logs

---

# 📚 Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos de:

- Computação Serverless
- APIs REST
- Integração entre serviços AWS
- Bancos de dados NoSQL
- Observabilidade e monitoramento
- Inteligência Artificial Generativa
- Desenvolvimento Front-End

---

# 👨‍💻 Autor

Rafael Figueiredo

Projeto autoral desenvolvido para demonstrar conhecimentos em Cloud Computing, Serverless Architecture e Inteligência Artificial aplicada à A
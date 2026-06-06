# 🤝 Como Contribuir com o CloudFunFacts

Obrigado pelo interesse em contribuir! Este documento explica como o projeto está organizado e como você pode colaborar.

---

## 📋 Pré-requisitos

- Conta na AWS (Free Tier)
- Python 3.11+
- AWS CLI configurado
- Git instalado

---

## ⚙️ Como rodar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/Rafaelmcf/cloudfunfacts.git
cd cloudfunfacts
```

### 2. Configure as permissões AWS
A função Lambda precisa das seguintes permissões IAM:
- `dynamodb:GetItem`
- `dynamodb:Scan`
- `bedrock:InvokeModel`
- `logs:CreateLogGroup`
- `logs:PutLogEvents`

### 3. Configure o DynamoDB
- Crie uma tabela chamada `CloudFacts`
- Partition key: `id` (String)
- Popule com as curiosidades do arquivo `Lambda/lambda_function.py`

### 4. Configure a Lambda
- Runtime: Python 3.11
- Handler: `lambda_function.lambda_handler`
- Timeout: 30 segundos
- Variáveis de ambiente: nenhuma necessária

### 5. Configure o API Gateway
- Tipo: HTTP API
- Rota: `GET /facts`
- Integração: Lambda function

### 6. Hospede o Frontend
- Faça upload do `FrontEnd/index.html` para um bucket S3
- Habilite Static Website Hosting no bucket
- Atualize a URL da API no arquivo `index.html`

---

## 🌿 Fluxo de trabalho Git

```bash
# 1. Crie uma branch para sua feature
git checkout -b feat/nome-da-feature

# 2. Faça suas alterações e commite
git add .
git commit -m "feat: descreva o que foi feito"

# 3. Suba para o GitHub
git push origin feat/nome-da-feature

# 4. Abra um Pull Request no GitHub
```

---

## 📝 Padrão de commits

| Prefixo | Quando usar |
|--------|-------------|
| `feat:` | Nova funcionalidade |
| `fix:` | Correção de bug |
| `docs:` | Alteração em documentação |
| `refactor:` | Refatoração de código |
| `chore:` | Tarefas de manutenção |

---

## 🏗️ Arquitetura resumida

| Serviço | Função |
|--------|--------|
| Amazon S3 | Hospeda o frontend estático |
| Amazon API Gateway | Expõe a rota GET /facts |
| AWS Lambda | Processa a lógica da aplicação |
| Amazon DynamoDB | Armazena as curiosidades |
| Amazon Bedrock | Enriquece o texto com IA |
| Amazon CloudWatch | Monitora logs e métricas |

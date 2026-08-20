# API Connect

## Objetivo

A API Connect é uma API desenvolvida em Python com Flask, criada com o objetivo de disponibilizar endpoints para recebimento e processamento de dados por meio de requisições HTTP.

O projeto utiliza uma estrutura organizada, separando as rotas da aplicação para facilitar a manutenção, a leitura e a evolução da API.

## Tecnologias utilizadas

* Python
* Flask
* Git
* GitHub

## Como executar o projeto localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/EllenMartins0dev/Desenvolvimento-Back-End_API.git
```

### 2. Acessar a pasta do projeto

```bash
cd api-connect-nome-sobrenome
```

### 3. Criar um ambiente virtual

No Windows:

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar as dependências

```bash
pip install flask
```

### 6. Executar a aplicação

```bash
python app.py
```

A API será executada localmente no endereço:

```text
http://127.0.0.1:5000
```

## Endpoints

### GET /

Verifica o funcionamento da API.

**Método:** `GET`

**URL:**

```text
/
```

**Resposta esperada:**

```json
{
    "mensagem": "API Connect funcionando!"
}
```

### POST /dados

Recebe dados enviados no corpo da requisição em formato JSON.

**Método:** `POST`

**URL:**

```text
/dados
```

**Exemplo de requisição:**

```json
{
    "nome": "Fernanda",
    "email": "fernanda@email.com"
}
```

**Resposta esperada:**

```json
{
    "mensagem": "Dados recebidos com sucesso!",
    "dados": {
        "nome": "Fernanda",
        "email": "fernanda@email.com"
    }
}
```

## Estrutura do projeto

```text
api-connect-nome-sobrenome/
├── .gitignore
├── README.md
├── app.py
└── routes/
    └── usuarios_routes.py
```

## Repositório

O código-fonte da API está disponível no GitHub:

URL_DO_REPOSITORIO


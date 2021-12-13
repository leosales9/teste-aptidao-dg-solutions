# Desafio técnico - DG Solutions

> O desafio consiste em criar um projeto que receba os dados de nome e data de nascimento de um usuário e e retorna uma lista com as pessoas e suas respectivas idades.

> Todos os comandos abaixo listados levam em consideração que você está dentro do diretório do projeto.

## Configurando o projeto

### Pré requisitos

-   [Docker](https://docs.docker.com/engine/install/ubuntu/)
    -   [Docker pós instalação](https://docs.docker.com/engine/install/linux-postinstall/)
-   [Docker Compose](https://docs.docker.com/compose/install/#install-compose-on-linux-systems)

### Backend

1. Entre no container do backend:

    ```bash
    docker-compose run --service-ports backend bash
    ```

2. Crie o ambiente virtual Python:

    ```bash
    python -m venv people-venv
    ```

3. Ative o ambiente virtual:

    ```bash
    source people-venv/bin/activate
    ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

5. Saia do ambiente virtual:

    ```bash
    deactivate
    ```

6. Saia do container com `CTRL + D`

### Frontend

1. Entre no container do frontend:

    ```bash
    docker-compose run --service-ports frontend bash
    ```

2. Instale as dependências do projeto

    ```bash
    yarn
    ```

3. Saia do container com `CTRL + D`

## Subindo os serviços e iniciando execução

Execute, se preferir em terminais diferentes, os seguintes comandos:

-   Iniciar backend

    ```bash
    docker-compose up backend
    ```

-   Iniciar frontend

    ```bash
    docker-compose up frontend
    ```

## Rotas da API

> Para esse desafio, foram definidas três rotas:

```bash
GET - /people/list
```
Resposta:

```bash
{
    people: [
        {
            person_birthdate: Date,
            person_id: Integer,
            person_name: String
        }
    ]
}
```
---

```bash
POST - /people/create
```

Payload:
```bash
{
    person_birthdate: Date,
    person_name: String
}
```

Resposta:


```bash
{
    msg: "Success"
}
```
---

```bash
DELETE - /people/remove/:people_id  
```

Resposta:

```bash
{
    msg: "Success"
}
```

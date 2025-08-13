# CrossFit Academy API

API para gerenciamento de academia de CrossFit desenvolvida com FastAPI, Python e Docker.

## Funcionalidades

- **Gestão de Atletas**: CRUD completo para atletas com validações
- **Gestão de Categorias**: Gerenciamento de categorias de treino
- **Gestão de Centros de Treinamento**: Controle de centros de treinamento
- **Validações**: CPF, sexo e outros campos com validação automática
- **Filtros**: Busca por nome e CPF de atletas
- **Documentação**: Swagger UI automático

## Tecnologias

- **FastAPI**: Framework web moderno e rápido
- **SQLAlchemy**: ORM para Python
- **Alembic**: Migrações de banco de dados
- **PostgreSQL**: Banco de dados relacional
- **Docker**: Containerização
- **Pydantic**: Validação de dados

## Estrutura do Projeto

```
santander-bootcamp-fastapi-api/
├── app/
│   ├── models/          # Modelos SQLAlchemy
│   ├── schemas/         # Schemas Pydantic
│   ├── routers/         # Rotas da API
│   └── database.py      # Configuração do banco
├── alembic/             # Migrações
├── main.py              # Aplicação principal
├── requirements.txt     # Dependências
├── docker-compose.yml   # Orquestração Docker
└── Dockerfile          # Imagem Docker

```

## Como Executar

### Pré-requisitos

- Docker
- Docker Compose

### Passos

1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd santander-bootcamp-fastapi-api
```

2. **Configure as variáveis de ambiente**
```bash
cp .env.example .env
```

3. **Execute com Docker Compose**
```bash
docker-compose up --build
```

4. **Execute as migrações**
```bash
docker-compose exec api alembic upgrade head
```

5. **Acesse a API**
- API: http://localhost:8000
- Documentação: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

### Categorias
- `POST /categorias/` - Criar categoria
- `GET /categorias/` - Listar categorias
- `GET /categorias/{id}` - Obter categoria
- `PATCH /categorias/{id}` - Atualizar categoria
- `DELETE /categorias/{id}` - Deletar categoria

### Centros de Treinamento
- `POST /centros-treinamento/` - Criar centro
- `GET /centros-treinamento/` - Listar centros
- `GET /centros-treinamento/{id}` - Obter centro
- `PATCH /centros-treinamento/{id}` - Atualizar centro
- `DELETE /centros-treinamento/{id}` - Deletar centro

### Atletas
- `POST /atletas/` - Criar atleta
- `GET /atletas/` - Listar atletas (com filtros)
- `GET /atletas/{id}` - Obter atleta
- `PATCH /atletas/{id}` - Atualizar atleta
- `DELETE /atletas/{id}` - Deletar atleta

## Exemplos de Uso

### Criar Categoria
```json
POST /categorias/
{
  "nome": "Iniciante"
}
```

### Criar Centro de Treinamento
```json
POST /centros-treinamento/
{
  "nome": "CrossFit Central",
  "endereco": "Rua das Flores, 123",
  "proprietario": "João Silva"
}
```

### Criar Atleta
```json
POST /atletas/
{
  "nome": "Maria Santos",
  "cpf": "12345678901",
  "idade": 25,
  "peso": 65.5,
  "altura": 1.70,
  "sexo": "F",
  "categoria_id": 1,
  "centro_treinamento_id": 1
}
```

## Desenvolvimento

### Executar localmente (sem Docker)

1. **Instale as dependências**
```bash
pip install -r requirements.txt
```

2. **Configure o banco PostgreSQL**
```bash
# Ajuste a DATABASE_URL no .env
DATABASE_URL=postgresql://usuario:senha@localhost:5432/crossfit_db
```

3. **Execute as migrações**
```bash
alembic upgrade head
```

4. **Execute a aplicação**
```bash
uvicorn main:app --reload
```

### Criar nova migração
```bash
alembic revision --autogenerate -m "Descrição da migração"
```

### Aplicar migrações
```bash
alembic upgrade head
```

## Testes

Para testar a API, você pode usar:
- Swagger UI: http://localhost:8000/docs
- Postman
- curl
- Qualquer cliente HTTP

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT.


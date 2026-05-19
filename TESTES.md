# Testes da API de Finanças Pessoais

Lista de testes que devem ser feitos na API. Pode testar pelo Swagger (/docs) ou pelo Postman.

---

## 1. Testes de Autenticação

### 1.1 Criar conta com sucesso
- **Endpoint:** `POST /auth/register`
- **Dados:**
```json
{
  "nome": "Joao Silva",
  "email": "joao@teste.com",
  "senha": "123456"
}
```
- **Resultado esperado:** Status 201, retorna o usuário criado com id, nome, email e criado_em

### 1.2 Criar conta com email duplicado
- **Endpoint:** `POST /auth/register`
- **Dados:** (mesmo email do teste 1.1)
- **Resultado esperado:** Status 400, mensagem "Email já cadastrado"

### 1.3 Criar conta sem nome
- **Endpoint:** `POST /auth/register`
- **Dados:**
```json
{
  "email": "novo@teste.com",
  "senha": "123456"
}
```
- **Resultado esperado:** Status 422 (erro de validação)

### 1.4 Criar conta sem email
- **Endpoint:** `POST /auth/register`
- **Dados:**
```json
{
  "nome": "Joao",
  "senha": "123456"
}
```
- **Resultado esperado:** Status 422 (erro de validação)

### 1.5 Criar conta sem senha
- **Endpoint:** `POST /auth/register`
- **Dados:**
```json
{
  "nome": "Joao",
  "email": "joao2@teste.com"
}
```
- **Resultado esperado:** Status 422 (erro de validação)

### 1.6 Login com sucesso
- **Endpoint:** `POST /auth/login`
- **Dados:**
```json
{
  "email": "joao@teste.com",
  "senha": "123456"
}
```
- **Resultado esperado:** Status 200, retorna access_token e token_type "bearer"

### 1.7 Login com email errado
- **Endpoint:** `POST /auth/login`
- **Dados:**
```json
{
  "email": "errado@teste.com",
  "senha": "123456"
}
```
- **Resultado esperado:** Status 401, mensagem "Email ou senha incorretos"

### 1.8 Login com senha errada
- **Endpoint:** `POST /auth/login`
- **Dados:**
```json
{
  "email": "joao@teste.com",
  "senha": "senhaerrada"
}
```
- **Resultado esperado:** Status 401, mensagem "Email ou senha incorretos"

### 1.9 Login sem email
- **Endpoint:** `POST /auth/login`
- **Dados:**
```json
{
  "senha": "123456"
}
```
- **Resultado esperado:** Status 422 (erro de validação)

### 1.10 Login sem senha
- **Endpoint:** `POST /auth/login`
- **Dados:**
```json
{
  "email": "joao@teste.com"
}
```
- **Resultado esperado:** Status 422 (erro de validação)

### 1.11 Acessar perfil com token válido
- **Endpoint:** `GET /auth/me`
- **Header:** `Authorization: Bearer <token>`
- **Resultado esperado:** Status 200, retorna os dados do usuário

### 1.12 Acessar perfil sem token
- **Endpoint:** `GET /auth/me`
- **Resultado esperado:** Status 401 (não autorizado)

### 1.13 Acessar perfil com token inválido
- **Endpoint:** `GET /auth/me`
- **Header:** `Authorization: Bearer tokenqualquer123`
- **Resultado esperado:** Status 401, mensagem "Token inválido"

---

## 2. Testes de Categorias

### 2.1 Criar categoria com sucesso
- **Endpoint:** `POST /categories`
- **Dados:**
```json
{
  "nome": "Alimentacao",
  "descricao": "Supermercado e restaurante"
}
```
- **Resultado esperado:** Status 201, retorna a categoria criada

### 2.2 Criar categoria sem nome
- **Endpoint:** `POST /categories`
- **Dados:**
```json
{
  "descricao": "Sem nome"
}
```
- **Resultado esperado:** Status 422 (erro de validação)

### 2.3 Criar categoria com nome duplicado
- **Endpoint:** `POST /categories`
- **Dados:** (mesmo nome do teste 2.1)
- **Resultado esperado:** Status 400, mensagem "Já existe uma categoria com esse nome"

### 2.4 Criar categoria sem descrição (opcional)
- **Endpoint:** `POST /categories`
- **Dados:**
```json
{
  "nome": "Transporte"
}
```
- **Resultado esperado:** Status 201, cria com descricao null

### 2.5 Listar todas as categorias
- **Endpoint:** `GET /categories`
- **Resultado esperado:** Status 200, retorna lista de categorias

### 2.6 Buscar categoria existente
- **Endpoint:** `GET /categories/1`
- **Resultado esperado:** Status 200, retorna a categoria

### 2.7 Buscar categoria que não existe
- **Endpoint:** `GET /categories/999`
- **Resultado esperado:** Status 404, mensagem "Categoria não encontrada"

### 2.8 Atualizar categoria
- **Endpoint:** `PUT /categories/1`
- **Dados:**
```json
{
  "nome": "Alimentacao Atualizada",
  "descricao": "Nova descricao"
}
```
- **Resultado esperado:** Status 200, retorna categoria atualizada

### 2.9 Atualizar categoria que não existe
- **Endpoint:** `PUT /categories/999`
- **Dados:**
```json
{
  "nome": "Teste",
  "descricao": "Teste"
}
```
- **Resultado esperado:** Status 404, mensagem "Categoria não encontrada"

### 2.10 Deletar categoria
- **Endpoint:** `DELETE /categories/1`
- **Resultado esperado:** Status 204, sem corpo na resposta

### 2.11 Deletar categoria que não existe
- **Endpoint:** `DELETE /categories/999`
- **Resultado esperado:** Status 404, mensagem "Categoria não encontrada"

---

## 3. Testes de Transações

### 3.1 Criar transação de despesa com sucesso
- **Endpoint:** `POST /transactions`
- **Header:** `Authorization: Bearer <token>`
- **Dados:**
```json
{
  "descricao": "Compra no mercado",
  "valor": 150.00,
  "tipo": "despesa",
  "categoria_id": 1
}
```
- **Resultado esperado:** Status 201, retorna a transação criada

### 3.2 Criar transação de receita com sucesso
- **Endpoint:** `POST /transactions`
- **Header:** `Authorization: Bearer <token>`
- **Dados:**
```json
{
  "descricao": "Salario",
  "valor": 3000.00,
  "tipo": "receita"
}
```
- **Resultado esperado:** Status 201, retorna a transação criada

### 3.3 Criar transação sem descrição
- **Endpoint:** `POST /transactions`
- **Header:** `Authorization: Bearer <token>`
- **Dados:**
```json
{
  "valor": 100.00,
  "tipo": "despesa"
}
```
- **Resultado esperado:** Status 422 (erro de validação)

### 3.4 Criar transação sem valor
- **Endpoint:** `POST /transactions`
- **Header:** `Authorization: Bearer <token>`
- **Dados:**
```json
{
  "descricao": "Teste",
  "tipo": "despesa"
}
```
- **Resultado esperado:** Status 422 (erro de validação)

### 3.5 Criar transação sem tipo
- **Endpoint:** `POST /transactions`
- **Header:** `Authorization: Bearer <token>`
- **Dados:**
```json
{
  "descricao": "Teste",
  "valor": 100.00
}
```
- **Resultado esperado:** Status 422 (erro de validação)

### 3.6 Criar transação com tipo inválido
- **Endpoint:** `POST /transactions`
- **Header:** `Authorization: Bearer <token>`
- **Dados:**
```json
{
  "descricao": "Teste",
  "valor": 100.00,
  "tipo": "invalido"
}
```
- **Resultado esperado:** Status 422 (erro de validação)

### 3.7 Criar transação sem estar logado
- **Endpoint:** `POST /transactions`
- **Dados:** (sem header de token)
- **Resultado esperado:** Status 401 (não autorizado)

### 3.8 Listar transações
- **Endpoint:** `GET /transactions`
- **Header:** `Authorization: Bearer <token>`
- **Resultado esperado:** Status 200, retorna lista de transações do usuário

### 3.9 Listar transações sem estar logado
- **Endpoint:** `GET /transactions`
- **Resultado esperado:** Status 401 (não autorizado)

### 3.10 Listar transações filtrando por tipo receita
- **Endpoint:** `GET /transactions?tipo=receita`
- **Header:** `Authorization: Bearer <token>`
- **Resultado esperado:** Status 200, retorna só transações do tipo receita

### 3.11 Listar transações filtrando por tipo despesa
- **Endpoint:** `GET /transactions?tipo=despesa`
- **Header:** `Authorization: Bearer <token>`
- **Resultado esperado:** Status 200, retorna só transações do tipo despesa

### 3.12 Buscar transação existente
- **Endpoint:** `GET /transactions/1`
- **Header:** `Authorization: Bearer <token>`
- **Resultado esperado:** Status 200, retorna a transação

### 3.13 Buscar transação que não existe
- **Endpoint:** `GET /transactions/999`
- **Header:** `Authorization: Bearer <token>`
- **Resultado esperado:** Status 404, mensagem "Transação não encontrada"

### 3.14 Atualizar transação
- **Endpoint:** `PUT /transactions/1`
- **Header:** `Authorization: Bearer <token>`
- **Dados:**
```json
{
  "descricao": "Descricao atualizada",
  "valor": 200.00
}
```
- **Resultado esperado:** Status 200, retorna transação atualizada

### 3.15 Atualizar transação que não existe
- **Endpoint:** `PUT /transactions/999`
- **Header:** `Authorization: Bearer <token>`
- **Dados:**
```json
{
  "descricao": "Teste"
}
```
- **Resultado esperado:** Status 404, mensagem "Transação não encontrada"

### 3.16 Deletar transação
- **Endpoint:** `DELETE /transactions/1`
- **Header:** `Authorization: Bearer <token>`
- **Resultado esperado:** Status 204, sem corpo na resposta

### 3.17 Deletar transação que não existe
- **Endpoint:** `DELETE /transactions/999`
- **Header:** `Authorization: Bearer <token>`
- **Resultado esperado:** Status 404, mensagem "Transação não encontrada"

---

## 4. Testes de Rotas Básicas

### 4.1 Rota raiz
- **Endpoint:** `GET /`
- **Resultado esperado:** Status 200, retorna mensagem de boas-vindas

### 4.2 Health check
- **Endpoint:** `GET /health`
- **Resultado esperado:** Status 200, retorna `{"status": "ok"}`

---

## Como usar esta lista

1. Comece pelos testes de autenticação (seção 1)
2. Depois teste as categorias (seção 2)
3. Por fim teste as transações (seção 3)
4. Marque os que passaram e anote os que falharam

Pode testar tudo pelo Swagger em http://localhost:8000/docs

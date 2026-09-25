# CRUD Catálogo Black Clover - backend & banco de dados

## Sobre o Projeto
API RESTful construída para gerenciar o catálogo de personagens do universo de Black Clover. Este repositório contém a lógica de back-end
e a modelagem do banco de dados relacional, lidando com chaves estrangeiras complexas (Esquadrões, Locais, Raças e Espíritos).

A interface web fica em um repositório separado: [crud-animes-frontend](https://github.com/odavicosta/crud-animes-frontend), publicada em [catalogo-clover.vercel.app](https://catalogo-clover.vercel.app/).

## Funcionalidades (Features)
* Criação, Leitura, Atualização e Exclusão (CRUD) de personagens.
* Filtros dinâmicos por nome, magia, local de origem e esquadrão.
* Leitura pública; criação, edição e exclusão protegidas por token.
* Banco de dados normalizado para garantir a consistência das entidades do anime.

## Tecnologias Utilizadas (Tech Stack)
* **Python 3**
* **Flask** (Criação da API e rotas)
* **MySQL** (Banco de Dados Relacional)
* **Aiven** (Hospedagem do Banco de Dados na nuvem)
* **Render** (Hospedagem da API, em https://api-black-clover.onrender.com)

## Modelagem do Banco de Dados
![Diagrama do Banco de Dados](assets/Diagrama_crud_bc.png)
*O banco foi projetado levando em consideração regras específicas do universo, como raças secundárias e posse de espíritos elementais.*

## Endpoints da API

| Método | Rota                | Autenticação | Descrição |
|--------|---------------------|--------------|-----------|
| GET    | `/personagens`      | Não          | Lista os personagens em ordem alfabética, com os nomes de esquadrão, raça, local e espírito. Aceita filtros. |
| POST   | `/personagens`      | Sim          | Cadastra um novo personagem. Responde `201`. |
| PUT    | `/personagens/<id>` | Sim          | Atualiza um personagem. Responde `200`. |
| DELETE | `/personagens/<id>` | Sim          | Remove um personagem. Responde `200`. |

**Filtros do GET** (todos opcionais, busca parcial):
`?nome=&magia=&local=&esquadrao=`
`local` e `esquadrao` filtram pelo **nome** do local ou do esquadrão, não pelo id.

**Corpo JSON do POST e do PUT:**
```json
{
  "nome": "Asta",
  "tipo_magia": "Anti-Magia",
  "id_esquadrao": 1,
  "id_espirito": null,
  "id_raca": 1,
  "id_raca_secundaria": null,
  "id_local_origem": 1,
  "eh_nobre": false,
  "eh_portador_demoniaco": true
}
```
- `nome`, `tipo_magia`, `id_raca` e `id_local_origem` são obrigatórios no banco.
- As flags `eh_nobre` e `eh_portador_demoniaco` valem `false` quando omitidas.

**Autenticação:** POST, PUT e DELETE exigem o header
```
Authorization: Bearer <ADMIN_TOKEN>
```
Sem o header, ou com um token errado, a resposta é `401 {"erro": "Não autorizado"}`. O GET é público.

**Outros códigos de resposta:**
- `413`: o corpo da requisição passa de 1 MB.
- `500`: erro do banco, com a mensagem em `{"erro": "..."}`.
- PUT e DELETE em um `id` inexistente respondem `200` mesmo assim.

## Variáveis de Ambiente

**Obrigatórias.** Se alguma faltar, a aplicação não inicia, e o erro diz quais variáveis estão faltando:

| Variável      | O que é |
|---------------|---------|
| `DB_HOST`     | Host do MySQL |
| `DB_PORT`     | Porta do MySQL (número) |
| `DB_USER`     | Usuário do banco |
| `DB_PASSWORD` | Senha desse usuário |
| `DB_NAME`     | Nome do banco |

**Opcionais:**

| Variável      | O que é |
|---------------|---------|
| `ADMIN_TOKEN` | Token exigido nas rotas de escrita. **Sem ele, POST, PUT e DELETE sempre respondem 401**; o GET continua funcionando. |
| `DB_SSL_CA`   | Caminho do certificado da CA do banco (ex.: o `ca.pem` do Aiven). Com ele, o certificado do servidor é verificado na conexão. Se apontar para um arquivo inexistente, a aplicação não inicia. |

Para gerar um token forte:
```
py -c "import secrets; print(secrets.token_urlsafe(32))"
```

## Como rodar o projeto localmente (Windows)

**1. Clone o repositório e entre na pasta**
```
git clone https://github.com/odavicosta/crud-animes-backend.git
cd crud-animes-backend
```

**2. Crie e ative o ambiente virtual**
```
py -m venv venv
.\venv\Scripts\Activate.ps1
```

**3. Instale as dependências**
```
pip install -r requirements.txt
```

**4. Defina as variáveis de ambiente na sessão do PowerShell**
```
$env:DB_HOST="127.0.0.1"
$env:DB_PORT="3306"
$env:DB_USER="seu_usuario"
$env:DB_PASSWORD="sua_senha"
$env:DB_NAME="black_clover"
$env:ADMIN_TOKEN="seu_token"
```
Os valores acima são para um MySQL local populado como na seção abaixo. As variáveis valem apenas para a sessão atual do terminal: se fechar e abrir outro, defina de novo.

**5. Execute a aplicação**
```
python app.py
```
A API estará rodando em http://127.0.0.1:5000.

O frontend aponta para a API de produção. Para usá-lo com a API local, troque a URL `https://api-black-clover.onrender.com` pelo endereço local nos arquivos `app.js` e `cadastro.js` do frontend.

## Como popular um banco novo

Os dois arquivos precisam ser carregados nesta ordem:

1. **`database.sql`**: cria o banco `black_clover` e as cinco tabelas (sem dados).
2. **`seed.sql`**: insere os dados de todas as tabelas (`locais`, `racas`, `espiritos`, `esquadroes` e `personagens`). Não cria banco nem tabelas.

Com o cliente `mysql`:
```
mysql -u seu_usuario -p --default-character-set=utf8mb4 -e "source database.sql"
mysql -u seu_usuario -p --default-character-set=utf8mb4 black_clover -e "source seed.sql"
```
No PowerShell, use `source` como acima em vez de redirecionar com `<`: o PowerShell não aceita `<` e, com pipe, pode corromper os acentos.

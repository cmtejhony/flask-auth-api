readme feito com chatgpt
# 🔐 API de Autenticação com Flask

Este projeto é uma API RESTful construída com Flask para autenticação de usuários, utilizando SQLite como banco de dados e JWT para proteger rotas.

---

## 🚀 Funcionalidades

- Registro de novos usuários
- Login com geração de token JWT
- Proteção de rotas com autenticação JWT
- Armazenamento seguro de senhas com hash
- Organização em pastas para escalabilidade

---

## 🧰 Tecnologias utilizadas

- Python 3
- Flask
- Flask SQLAlchemy
- Flask JWT Extended
- Python Dotenv
- SQLite

---

## 🛠️ Como rodar o projeto localmente

1. Clone o repositório:

```bash
git clone https://github.com/cmtejhony/flask-auth-api.git
cd flask-auth-api
python -m venv venv

2. Crie e ative um ambiente virtual
bash
Copiar
Editar
python -m venv venv
venv\Scripts\activate   # No Windows
# Ou
source venv/bin/activate   # No Linux/Mac
3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt

4. Crie um arquivo .env na raiz do projeto com o conteúdo:
env
Copiar
Editar
JWT_SECRET_KEY=uma_chave_super_secreta
5. Rode a aplicação
bash
Copiar
Editar
python app.py
A API estará disponível em http://localhost:5000.

📦 Estrutura de pastas
bash
Copiar
Editar
flask-auth-api/
│
├── models/
│   └── user.py         # Modelagem do usuário
│
├── venv/               # Ambiente virtual (ignorado pelo Git)
├── app.py              # Arquivo principal da aplicação
├── .env                # Variáveis de ambiente (não versionado)
├── .gitignore          # Arquivos ignorados pelo Git
├── requirements.txt    # Dependências do projeto
├── README.md           # Este arquivo
✅ Endpoints principais
Método	Rota	Protegida	Descrição
POST	/register	❌	Registro de novo usuário
POST	/login	❌	Login e geração de JWT
GET	/protected	✅	Exige autenticação com token

📬 Contato
Projeto criado por [João Pedro Flach].
Contribuições, sugestões e melhorias são bem-vindas!

# 🎬 Flix API

Uma API simples desenvolvida com Django Rest Framework para simular um sistema de catálogo de filmes e categorias.

## 🚀 Tecnologias utilizadas

* Python
* Django
* Django Rest Framework
* SQLite

## 🛠 Funcionalidades

* Cadastro de filmes
* Cadastro de categorias
* Filtro por categoria
* Exibição de todos os filmes e detalhes individuais

## 📦 Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/CFBruna/flix_api.git

# Acesse a pasta do projeto
cd flix-api

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Rode as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```
## 📄 Licença

Este projeto está licenciado sob a **MIT License**.  
Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.

---

## 💡 Créditos

Desenvolvido por [Bruna (CFBruna)](https://github.com/CFBruna) com 💻 e ☕  
Este projeto foi desenvolvido como parte dos estudos durante o curso **Django Master**.

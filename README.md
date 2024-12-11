# Projeto Blog em Django

Bem-vindo ao repositório do **Projeto Blog em Django**! Este é um sistema de blog desenvolvido com o framework Django, focado em funcionalidade, simplicidade e escalabilidade. Aqui você encontra instruções para clonar, instalar e utilizar o projeto.

## Tecnologias Utilizadas

- **Python 3**
- **Django 4**
- Banco de Dados: SQLite (padrão, pode ser configurado para outros)
- HTML/CSS/JavaScript para o front-end

## Funcionalidades

- Sistema de autenticação para usuários (login, registro e logout).
- Criação, edição e exclusão de postagens de blog.
- Administração personalizada para gerenciar o blog.
- Suporte a tags ou categorias (dependendo da implementação).

## Requisitos de Sistema

Certifique-se de ter as seguintes ferramentas instaladas antes de continuar:

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)
- Virtualenv (recomendado para isolar dependências)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/luizomf/projeto-blog-django-23.git
   cd projeto-blog-django-23
   ```

2. **Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate # No Windows, use: venv\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados:**

   Execute as migrações para configurar o banco de dados:

   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento:**

   ```bash
   python manage.py runserver
   ```

6. **Acesse o projeto:**

   Abra o navegador e acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Uso

1. **Administração:**
   
   Crie um superusuário para acessar a área administrativa:

   ```bash
   python manage.py createsuperuser
   ```

   Depois, acesse [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) para gerenciar postagens, usuários e outros recursos.

2. **Publicação de Posts:**
   
   Os usuários autenticados podem criar, editar e excluir postagens diretamente da interface do site.

## Testes

Para executar a suite de testes do projeto:

```bash
python manage.py test
```

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Fork o repositório.
2. Crie um branch para suas alterações: `git checkout -b minha-feature`
3. Envie suas alterações: `git commit -m 'Minha nova feature'`
4. Realize um push: `git push origin minha-feature`
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
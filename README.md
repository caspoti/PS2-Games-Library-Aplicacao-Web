# PS2 Games Library

Uma aplicação web desenvolvida com **Python e Django** para criar e gerenciar uma biblioteca pessoal de jogos de PlayStation 2.

O projeto permite cadastrar jogos que já foram jogados, adicionar avaliações, reviews, favoritos, capas e trailers, além de pesquisar e visualizar informações detalhadas de cada jogo.

---

## Sobre o projeto

O **PS2 Games Library** nasceu como um projeto pessoal para colocar em prática os conhecimentos adquiridos durante meus estudos de **Python, Django, banco de dados, templates e desenvolvimento web**.

A proposta é criar uma espécie de biblioteca pessoal onde posso registrar os jogos de PlayStation 2 que já joguei e guardar algumas informações sobre cada experiência.

Cada jogo possui uma página própria com suas informações.

---

## Funcionalidades

- Listagem de jogos de PlayStation 2
- Pesquisa de jogos
- Upload e exibição das capas dos jogos
- Ano de lançamento
- Sistema de avaliação
- Sistema de favoritos
- Review pessoal de cada jogo
- Página individual para cada jogo
- Integração com trailers do YouTube
- Navegação entre páginas utilizando Django
- Layout responsivo
- Interface inspirada na estética do PlayStation 2

---

## Tecnologias utilizadas

- Python 3
- Django
- SQLite
- HTML5
- CSS3
- YouTube Embed
- Git
- GitHub

---

## Estrutura do projeto

Uma estrutura aproximada do projeto:

```text
PS2-Games/
│
├── games/
│   ├── migrations/
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── games.html
│   │   ├── game.html
│   │   └── favorites.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── media/
│   └── games/
│
├── static/
│
├── manage.py
│
├── db.sqlite3
│
└── README.md

## Como executar o projeto

1 - git clone https://github.com/seu-usuario/ps2-games.git

2 - cd ps2-games

3 - python -m venv venv

4 - venv\Scripts\activate

5 - pip install -r requirements.txt

6 - python manage.py migrate

7 - python manage.py createsuperuser

8 - python manage.py runserver
# ShopApp

![ShopApp Logo](https://skillicons.dev/icons?i=python,django,postgresql,git,github,bootstrap)

**ShopApp** — это приложение для электронной коммерции, построенное на базе Django и других современных технологий. Приложение обеспечивает удобный и интуитивно понятный пользовательский интерфейс как для клиентов, так и для администраторов. Включает такие функции, как управление продуктами, корзина и оформление заказов.

## Особенности

- **Аутентификация пользователей:** Регистрация, вход и управление учетными записями.
- **Управление продуктами:** Добавление, редактирование и удаление продуктов.
- **Корзина покупок:** Добавление товаров в корзину, обновление количества и оформление заказа.
- **Управление заказами:** Пользователи могут просматривать, отслеживать и завершать свои заказы.

## Используемые технологии

Вот основные технологии, использованные в проекте **ShopApp**:

### Бэкенд:
- ![Django](https://skillicons.dev/icons?i=django) **Django** — фреймворк для быстрого веб-разработки и чистой архитектуры.
- ![Python](https://skillicons.dev/icons?i=python) **Python** — язык программирования, на котором работает бэкенд приложения.
- ![PostgreSQL](https://skillicons.dev/icons?i=postgresql) **PostgreSQL** — реляционная система управления базами данных для хранения данных приложения.

### Фронтенд:
- ![Bootstrap](https://skillicons.dev/icons?i=bootstrap) **Bootstrap 5** — CSS-фреймворк для стилизации и адаптивности интерфейса.
- ![Font Awesome](https://skillicons.dev/icons?i=fontawesome) **Font Awesome** — использован для добавления иконок в приложение.

### Другие инструменты:
- ![Git](https://skillicons.dev/icons?i=git) **Git** — система управления версиями для отслеживания изменений в коде.
- ![GitHub](https://skillicons.dev/icons?i=github) **GitHub** — хостинг для репозиториев с использованием Git.

## Начало работы

Чтобы запустить **ShopApp** локально, выполните следующие шаги:

### Требования

2. Установите **Python** (для управления зависимостями и запуска Django сервера).
3. Установите **PostgreSQL** (если не используете контейнер PostgreSQL из Docker).

### Установка

1. Клонируйте репозиторий:
   ```bash
   git clone git remote add origin https://github.com/Frengocode/Django-Shop-App.git
   python -m venv venv
   for windows ./v + tab/s + tab/a + tab

   for mack or liniux source bin/activate

   pip install -r requirements.txt

   python manage.py migrate

   python manage.py runserver


2. Укажите все параметры в env. 

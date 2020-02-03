# shelter
#### Проект предлагает простой бэкенд на Django и Django Rest Framework с базой данных и API.

### Запуск приложения
- pip install -r requirements.txt для установки зависимостей
+ python3 manage.py makemigrations - для инициализации модели (эта команда также необходима после обновления модели)
+ python3 manage.py migrate - для фиксации изменений в модели (эта команда также необходима после обновления модели)
+ python3 manage.py runserver - для запуска на localhost:8000/api

### Реализованные возможности
- CRUD интерфейс в админку добавляется через регистрации  моделей в admin.py
+ добавлена команда в django-admin для создания пустых записей в модели Dogs, создан dogshelter/management/commands/createdogs.py, запускается python3 manage.py createdogs.py + число нужных записей
+ доступен API для CRUD oпераций с помощью viewsets, serializers, routers по localhost:8000/api/dogshelter
+ в serializers.py добавлена возможность вычиcлять поле doc_info на основе полей byname и breed (в модели Dogs)
+ для модели Costs через админку введен запpeт на редактирование
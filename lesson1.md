# Установка Django

1. Активация виртуального окружения
```shell
python -m venv venv
pip install django, pillow

pip freeze > requierments.txt       

django-admin startproject myshop  
python myshop/manage.py runserver 8001
python manage.py makemigrations
python manage.py createsuperuser
```

2. 
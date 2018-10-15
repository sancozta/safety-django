### Safetydjango

Recomenda-se utilizar um terminal bash para facilitar o desenvolvimeto e criação do ambiente local.

#### Preperando o Ambiente

	python manage.py runserver

#### Instalando Dependências

	pip install -r requirements.txt

#### Deploy no Heroku

	web: gunicorn project.wsgi
	
#### Comandos Úteis

	python -m django --version
    django-admin startproject project
    python manage.py runserver 8080 
    python manage.py startapp polls
    pip freeze > requirements.txt


        
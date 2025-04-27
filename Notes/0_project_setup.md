# Project Setup

## Install Django
First create a virtual environment `env` and activate it.
```bash
python3 -m venv env
source env/bin/activate
```

Install Django and Django REST Framework
```bash
pip install django djangorestframework
```

Add a `requirements.txt` file
```bash
pip freeze > requirements.txt
```

Create a django project at the root directory
```bash
django-admin startproject learn_drf .
```

## PostgreSQL Configuration
Install `psycopg2` for PostgreSQL which is the PostgreSQL adapter for Python. Django uses it to connect to PostgreSQL.
```bash
pip install psycopg2
```
Now, create a database, a user and then grant the user to that database
```bash
sudo -u postgres psql # enter into postgresql
```
```sql
CREATE DATABASE learn_drf_db;
CREATE USER learn_drf_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE learn_drf_db TO learn_drf_user;
```

Update Django Settings to Use PostgreSQL in our `learn_drf/settings.py`
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'learn_drf_db',
        'USER': 'learn_drf_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',  # or your database host
        'PORT': '5432',       # default port for PostgreSQL
    }
}
```

## Create Custom User

Django has its own `user` class with some possible . But if we want to add some custom fields then we have to create a custom user class. Note that this class has to be created before running our initial migration. 

### Create an `app` Package
First we will create an `app` packages where all the app modules will reside. 
- First create a directory `apps` from the root directory
- Create an `__init__.py` file which is important to make the dirctory as package

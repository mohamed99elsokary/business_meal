# how to run it
## install python 3
## create python env using

```shell
python3 -m venv env
source env/bin/activate
```

## install requirements using:

```shell
pip install -r requirements.txt
```

## create db:

```shell
python manage.py migrate
```

## create superuser:

```shell
python manage.py createsuperuser
```

and follow the steps it asks for

## run server:

```shell
python runserver.py
```

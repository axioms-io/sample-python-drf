# sample-python-drf
Django REST Framework (DRF) Sample using [Axioms](https://axioms.io). Secure your DRF APIs using Axioms Authentication and Authorization.


## Setup
Create virtualenv,

```
python3 -m venv venv
```

Then activate virtualenv and install requirements,

```
source venv/bin/activate
pip install -r requirements-dev.txt
```

Set environment variables,
```
export DJANGO_SECRET_KEY=djangosecretkey
```

## Run Server

```
python manage.py runserver 0.0.0.0:5000
```
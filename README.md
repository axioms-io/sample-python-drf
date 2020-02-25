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

## Test using Postman
Postman collection is included in this repository. Import the collection in your Postman, setup environment variables `host` (i.e. localhost:5000) and `access_token` (you can obtain from your client) and test these APIs.
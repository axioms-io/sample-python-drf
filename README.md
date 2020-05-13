# sample-python-drf
Django REST Framework (DRF) Sample using [Axioms](https://axioms.io) and [axioms-drf-py](https://github.com/axioms-io/axioms-drf-py). Secure your DRF APIs using Axioms authentication and authorization.

## Prerequisite

* Python 3.7+
* An [Axioms](https://axioms.io) client which can obtain access token after user's authentication and authorization and include obtained access token as bearer in `Authorization` header of all API request sent to Python/Django/DRF application server.

## Setup
Clone this repository,

```
git clone https://github.com/axioms-io/sample-python-drf.git
cd sample-python-drf
```

Create virtualenv,

```
python -m venv venv
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

## Add Config
Create a `.env` file in your main Django app and add following configs (see `.sample-env`),

```
AXIOMS_DOMAIN=<your-axioms-slug>.axioms.io
AXIOMS_AUDIENCE=<your-axioms-resource-identifier>
```

## Run Server

```
python manage.py runserver 0.0.0.0:5000
```

## Test using Postman
Postman collection is included in this repository. Import the collection in your Postman, setup environment variables `host` (i.e. localhost:5000) and `access_token` (you can obtain from your client) and test these APIs.

## Documentation
See [documentation](https://developer.axioms.io/docs/sdks-samples/use-with-apis/python/django-apis) for `axioms-drf-py`.

## Deploy to Heroku
You will need to provide Axioms domain and Axioms audience to complete deployment.

<a href="https://heroku.com/deploy?template=https://github.com/axioms-io/sample-python-drf">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy" width="200px">
</a>

[![Edit sample-python-drf](https://codesandbox.io/static/img/play-codesandbox.svg)](https://codesandbox.io/s/github/axioms-io/sample-python-drf/tree/master/?fontsize=14&hidenavigation=1&theme=light)
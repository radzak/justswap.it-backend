# justswap

JustSwap

This project was generated with [`wemake-django-template`](https://github.com/wemake-services/wemake-django-template). Current template version is: [cf9edf14f2fd06df8493944d2fbf0e8352a1bf4f](https://github.com/wemake-services/wemake-django-template/tree/cf9edf14f2fd06df8493944d2fbf0e8352a1bf4f). See what is [updated](https://github.com/wemake-services/wemake-django-template/compare/cf9edf14f2fd06df8493944d2fbf0e8352a1bf4f...master) since then.


[![wemake.services](https://img.shields.io/badge/%20-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services) 
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)


## Prerequisites

You will need:

- `docker` with [version at least](https://docs.docker.com/compose/compose-file/#compose-and-docker-compatibility-matrix) `18.02`


## Development

To run the Django app locally, you need to build the Docker containers,
apply migrations and create a super user. 


```bash
docker-compose build
docker-compose run --rm web python manage.py migrate
docker-compose run --rm web python manage.py createsu
```

To run the docker containers you need to invoke the following command:
```bash
docker-compose up
```

You can use `admin@example.com`, password: `admin` to login into
the admin panel (http://localhost:8000/admin/login/) and Django Rest Framework
Browsable API (http://localhost:8000/auth/login/).


## API endpoints

- `/api/auth/users/*` - User creation, activation, password change, see
  https://djoser.readthedocs.io/en/latest/base_endpoints.html for more
  information.
- `/api/auth/jwt/*` - Obtain/refresh/verify JWT token endpoint, refer to
  https://djoser.readthedocs.io/en/latest/jwt_endpoints.html for more details.  


## Documentation

Full documentation is available here: [`docs/`](docs).

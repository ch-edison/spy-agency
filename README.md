Spy Agency
====================

For the development of app you find two applications in apps
### system_hits
Here is all the logic that allows you to manage a hit
### users
here is all the logic that allows you to manage all the users or hitmen that exist in the app
## Run project

For up project you should run the next command `make build`:

build:

    docker compose -f local.yml up --build -d --remove-orphans

For execute models in app you should run `make makemigrations`:

build:

    docker compose -f local.yml run --rm api python3 manage.py makemigrations


For migrate the models to database you should run `make migrate`:

build:

    docker compose -f local.yml run --rm api python3 manage.py migrate


## USERS - SICARIOS
| Email           | Contraseña    |
|-----------------|---------------|
| hitmen1@spy.com | password12345 |
| hitmen2@spy.com | password12345 |
| hitmen3@spy.com | password12345 |
| hitmen4@spy.com | password12345 |
| hitmen5@spy.com | password12345 |
| hitmen6@spy.com | password12345 |
| hitmen7@spy.com | password12345 |
| hitmen8@spy.com | password12345 |
| hitmen9@spy.com | password12345 |


## USERS - MANAGER - GERENTE
| Email            | Contraseña    |
|------------------|---------------|
| manager1@spy.com | password12345 |
| manager2@spy.com | password12345 |
| manager3@spy.com | password12345 |

## USERS - BOSS - JEFE
| Email         | Contraseña    |
|---------------|---------------|
| boss1@spy.com | password12345 |

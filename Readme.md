# flask-postgres-docker
This is a simple demo of CRUD API create in python using `Flask` framework. This demo uses `Flask-SQLAlchemy` and `Flask-Migrate` to connect with `Postgres` database and runs in docker containers.

## Structure
```sh
└── flask_postgresql_api
    └── app
    │    ├── __init__.py
    │    ├── models.py
    │    └── routes.py
    ├── Dockerfile
    ├── docker-compose.yml
    ├── entrypoint.sh
    ├── Readme.md
    ├── requirements.txt
    ├── config.py
    └──  main.py
```



## Installation
First you must have Docker installed, then `git clone` the repo.

Run following command to start building images and run containers.
```sh
docker-compose up --build -d
```
Then you have to run `docker ps` to verify running containers and ports.
```sh
PORTS
0.0.0.0:5000->5000/tcp
0.0.0.0:5432->5432/tcp
```
Finally you can check the server in the url `http://localhost:5000/hello`

## Test APIs

For create user you have to use `createUser` method and this `JSON`.
| METHOD | DESCRIPTION | URL |
| ------ | ------ | ------ |
| POST | Create new user | [localhost:5000/createUser][PlOd] | 
```json
{
    "name": "David",
    "phone": "52123456789",
    "age": 21
}
```

And you can also call the following methods
| METHOD | DESCRIPTION | URL |
| ------ | ------ | ------ |
| GET | Test API | [localhost:5000/hello][PlDb] |
| GET | Get all users | [localhost:5000/getUsers][PlGh] |
| GET | Get user by name | [localhost:5000/getUser?name=#][PlGd] |
| PUT | Update user age by name | [localhost:5000/updateAge?name=#&newAge=#][PlMe] |
| DELETE | Delete a user by name | [localhost:5000/deleteUser?name=#][PlGa] |

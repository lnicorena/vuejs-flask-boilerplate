# Weather app 

### This is a boilerplate for VueJS application served over Python + Flask + Postgres + Redis + Docker
 

# Instructions 

Follow the above instructions to get the app running.




## Front-end setup

``` bash

cd client

# Rename the .env file and configure the API address and port
mv .env-example .env

# Install project dependencies
yarn install

# Compiles and hot-reloads for development at localhost:8080
yarn serve

# Compiles and minifies for production
yarn build

# Run front-end tests
yarn test:unit
yarn test:e2e
```

## Back-end setup

``` bash
# using docker-compose (recommended)
cd server

# build and run the containers (api will be available at: http://127.0.0.1:8081)
docker-compose up --build

# run tests
docker exec -it flask py.test


# or you can always start the backend manually
cd server/flask

# Create python virtual env 
virtualenv -p python venv

# Activate virtual env
source venv/bin/activate

# Install project requirements
pip install -r requirements.txt

# Run postgres and redis instances and configure the env files
.

# serve back-end at localhost:5000
FLASK_APP=app.py flask run

# Compiles and hot-reloads for development at localhost:5000
FLASK_APP=app.py FLASK_DEBUG=1 python -m flask run

# update/save requirements
pip freeze > requirements.txt

# run tests
py.test

```

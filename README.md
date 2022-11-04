# DRF_test

## You need the following technologies to start your project:
* Docker + docker-compose
* Make
* Create .env file in base_dir(DRF_test/)


## Data in .env file:
* ```KEY='django-insecure-ne0o^)@hu2ypzbv)-*#227=tfvfo+&@lqdxycjg$ly&y3vvsax'```
* ```POSTGRES_PASSWORD=postgres_password```
* ```POSTGRES_USER=postgres```
* ```POSTGRES_DB=base```
* ```PORTS_DB="5432:5432"```
* ```PORTS_WEB="8000:80"```
* ```PORTS_NGINX="80:80"```

## First step.
### Commands for launching a project.
*  ```make build``` or  ```docker-compose --env-file .env up --build```

## Second step.
### After starting the project, open a new terminal window and type the following commands:
*  ```make exec``` or ```docker exec -it Django_APP sh``` - Entrance to the container with the project
* ```make admin``` or  ```python manage.py createsuperuser``` - Create an administrator user

## Third step.
### The site operates at the following addresses
* [First address](http://localhost/) or [Second address](http://127.0.0.1/) - New Product Creation page
* [Admin address local](http://localhost/admin) or [Admin address 127](http://127.0.0.1/admin) - Admin panel


## After work, if you need to clear all data, use the following command (DANGER ZONE).
* ```make rm_lite``` or ```docker rm -f $$(docker ps -a -q)``` - Delete the entire container
* ```make rm_middle``` or ```docker rm -f $$(docker ps -a -q) ; docker rmi $$(docker images -a -q)``` - Remove all containers + images
* ```make rm_full``` or ```docker rm -f $$(docker ps -a -q) ; docker rmi $$(docker images -a -q) ; docker volume prune``` - Delete all containers + images + volume

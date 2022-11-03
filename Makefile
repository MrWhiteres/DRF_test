admin:
	python manage.py createsuperuser
run:
	python manage.py runserver 0.0.0.0:8000
up:
	docker-compose --env-file .env up -d
build:
	docker-compose --env-file .env up --build
stop:
	docker-compose down
exec:
	docker exec -it Django_APP sh
rm_lite:
	docker rm -f $$(docker ps -a -q)
rm_middle:
	docker rm -f $$(docker ps -a -q) ; docker rmi $$(docker images -a -q)
rm_full:
	docker rm -f $$(docker ps -a -q) ; docker rmi $$(docker images -a -q) ; docker volume prune

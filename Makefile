build:
	docker-compose build

up:
	docker-compose up -d

logs:
	docker-compose logs -f

down:
	docker-compose down

startapp:
	@docker-compose exec web python manage.py startapp $(filter-out $@,$(MAKECMDGOALS))

migrations:
	docker-compose exec web python manage.py makemigrations

migrate:
	docker-compose exec web python manage.py migrate

%:
	@:

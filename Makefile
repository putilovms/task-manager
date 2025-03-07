.PHONY: install
install:
	poetry install

.PHONY: static
static:
	poetry run python manage.py collectstatic --no-input

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: setup
setup:
	poetry install
	poetry run python manage.py collectstatic --no-input
	poetry run python manage.py migrate

.PHONY: dev
dev:
	poetry run python manage.py runserver 0.0.0.0:8000

PORT ?= 8000
.PHONY: start
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

.PHONY: lint
lint:
	poetry run flake8 task_manager

.PHONY: test
test:
	poetry run python manage.py test

.PHONY: test-coverage
test-coverage:
	poetry run coverage run --source='.' manage.py test
	poetry run coverage xml

.PHONY: makemigrations
makemigrations:
	poetry run python manage.py makemigrations

.PHONY: makemessages
makemessages:
	poetry run django-admin makemessages --ignore="static" --ignore=".env" -l ru_RU

.PHONY: compilemessages
compilemessages:
	poetry run django-admin compilemessages

.PHONY: shell
shell:
	poetry run python manage.py shell
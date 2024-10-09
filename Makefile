.PHONY: install
install:
	poetry install

.PHONY: dev
dev:
	poetry run python manage.py runserver

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

.PHONY: makemigrations
makemigrations:
	poetry run python manage.py makemigrations

.PHONY: setup
setup:
	poetry install
	poetry run python manage.py collectstatic --no-input
	poetry run python manage.py migrate

.PHONY: makemessages
makemessages:
	poetry run django-admin makemessages --ignore="static" --ignore=".env" -l ru_RU

.PHONY: compilemessages
compilemessages:
	poetry run django-admin compilemessages

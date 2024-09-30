install:
	poetry install

dev:
	poetry run python manage.py runserver

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

lint:
	poetry run flake8 task_manager

setup:
	poetry install
	poetry run python manage.py collectstatic --no-input
	poetry run python manage.py migrate

.PHONY: install dev lint start setup

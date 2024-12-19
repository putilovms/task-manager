### Hexlet tests and linter status:
[![Actions Status](https://github.com/putilovms/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/putilovms/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/157533a779f6d55f56f9/maintainability)](https://codeclimate.com/github/putilovms/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/157533a779f6d55f56f9/test_coverage)](https://codeclimate.com/github/putilovms/python-project-52/test_coverage)

# Task Manager
*Educational project*

Task management system. It allows you to set tasks, assign performers and change their statuses. User registration and authentication are also implemented.

Link to the project's website: [https://python-project-52-afhn.onrender.com/](https://python-project-52-afhn.onrender.com/)

***Notice**: the project uses a free hosting plan, the request can take up to 50 seconds.*

## Overview of the web application

This web application is implemented in **Python** and the **Django** framework, and **PostgreSQL** is used as an object-relational database system. The **Bootstrap** framework was used to render the client side and ensure adaptability. The Task Manager **supports internationalization and is localized** in Russian and English. The **Rollbar** service is integrated to track errors. The project is built in compliance with the principles of **CI/CD**.

User registration and authentication has been implemented. It is possible to create tasks, statuses and labels for them, and assign an executor. Tasks can be filtered by various criteria. You can also change and delete all entities. User access restriction has been implemented.

## Installation

1. Requires Python version 3.10 or higher and Poetry
2. Clone the project: `>> git clone https://github.com/putilovms/python-project-52.git`
3. Create an `.env` file in the root of the project and add the following variables to it:
    * `SECRET_KEY` - the secret key
    * `DATABASE_URL` - access to the PostgreSQL database
    * `DEBUG` - activating the debugging mode
    * `ROLLBAR_ACCESS_TOKEN` - access token to the Rollbar service
4. Create migrations necessary for the service to work: `>> make makemigrations`
5. Build the project using the command: `>> make setup`
6. Starting the server: `>> make start`

## Docker Compose

1. To run in product mode:
   1. Create files for environment variables with the following contents:
      * `/compose/product/postgres.env`
         * `POSTGRES_DB` - database name
         * `POSTGRES_USER` - username
         * `POSTGRES_PASSWORD` - password
      * `/compose/product/task_manager.env`
         * `SECRET_KEY` - the secret key
         * `DATABASE_URL` - access to the PostgreSQL database
         * `DEBUG` - activating the debugging mode
         * `ROLLBAR_ACCESS_TOKEN` - access token to the Rollbar service
   2. Go to the directory with compose files `>> cd compose/product/`
   3. The command to launch containers `>> docker-compose up --build`
2. To run in development mode:
   1. Create files for environment variables with the following contents:
      * `/compose/dev/postgres.env`
      * `/compose/dev/task_manager.env`
   2. Go to the directory with compose files `>> cd compose/dev/`
   3. The command to launch containers `>> docker-compose up --build`
3. To run in test mode:
   1. Create file for environment variables with the following contents:
      * `/compose/test/task_manager.env`
   2. Go to the directory with compose files `>> cd compose/test/`
   3. The command to launch containers `>> docker-compose up --build`
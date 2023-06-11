# HotelHeroic

HotelHeroic is a Django application built for managing hotel operations and reservations.

## Features

- Reservation Management: Manage hotel reservations, including booking details, guest information, and room assignments.
- Room Availability: Check room availability for specific dates and make new reservations.
- Billing and Invoicing: Generate invoices for guests and handle billing transactions.
- Reporting: Generate reports to analyze occupancy rates, revenue, and other key metrics.
- User Management: Manage user accounts and assign roles and permissions.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/bvedad/hotelheroic-django.git
   ```

2. Create a virtual environment and activate it:

   ```shell
   python3 -m venv env
   source env/bin/activate
   ```

3. Install the Python dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Set up the database:

```shell
psql postgres -c "CREATE ROLE hh_role;"
psql postgres -c "CREATE USER hh_user WITH PASSWORD 'password' IN ROLE hh_role;"
psql postgres -c "CREATE DATABASE hh_db OWNER hh_role;"
psql postgres -c "CREATE SCHEMA hh_db;"
psql postgres -c "ALTER USER hh_user CREATEDB;"
```

- Apply database migrations

```shell
python manage.py migrate
```

5. Start the development server:

   ```shell
   python manage.py runserver
   ```

The application will be accessible at http://localhost:8000

## Recompile CSS

To recompile SCSS files, follow this setup:

1. Install tools

- [NodeJS](https://nodejs.org/en/) 12.x or higher
- [Gulp](https://gulpjs.com/) - globally
    - `npm install -g gulp-cli`
- [Yarn](https://yarnpkg.com/) (optional)

2. Change the working directory to `assets` folder

```bash
$ cd apps/static/assets
```

3. Install modules (this will create a classic `node_modules` directory)

```bash
$ npm install
// OR
$ yarn
```

<br />

4. Edit & Recompile SCSS files

```bash
$ gulp
```

The generated files (css, min.css) are saved in `static/assets/css` directory.

<br />

## Deployment

The app is provided with a basic configuration to be executed in [Docker](https://www.docker.com/)
, [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

### [Docker](https://www.docker.com/) execution
---

The application can be easily executed in a docker container. The steps:

> Get the code

```bash
$ git clone https://github.com/app-generator/priv-django-dashboard-volt-pro.git
$ cd hotelheroic-django
```

> Start the app in Docker

```bash
$ sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d
```

Visit `http://localhost:85` in your browser. The app should be up & running.

<br />

### [Gunicorn](https://gunicorn.org/)
---

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

> Install using pip

```bash
$ pip install gunicorn
```

> Start the app using gunicorn binary

```bash
$ gunicorn --bind=0.0.0.0:8001 core.wsgi:application
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.


### [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/)
---

Waitress (Gunicorn equivalent for Windows) is meant to be a production-quality pure-Python WSGI server with very
acceptable performance. It has no dependencies except ones that live in the Python standard library.

> Install using pip

```bash
$ pip install waitress
```

> Start the app using [waitress-serve](https://docs.pylonsproject.org/projects/waitress/en/stable/runner.html)

```bash
$ waitress-serve --port=8001 core.wsgi:application
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

## Credits & Links

- [Django](https://www.djangoproject.com/) - The official website
- [Boilerplate Code](https://appseed.us/boilerplate-code) - Index provided by **AppSeed**
- [Boilerplate Code](https://github.com/app-generator/boilerplate-code) - Index published on Github

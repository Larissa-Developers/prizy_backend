# Prizy Back-end

Django REST API back-end for Prizy.

**Requirements:**

* [Python 3.6](https://www.python.org/downloads/release/python-366/)
* [MySQL](https://www.mysql.com/)

**Additional dependencies**

For any Ubuntu-based OS:

```
$ sudo apt install build-essential python3-dev libmysqlclient-dev
```

## Quickstart

**1. Clone the repository:**

```
$ git clone https://github.com/Larissa-Developers/prizy_backend.git
```

**2. Install pipenv:**

Follow the instructions on [Pipenv Documentation](https://pipenv.readthedocs.io/en/latest/) to install `pipenv` on your development environment.

**3. Install dependencies:**

In the project root directory run:

```
(venv) $ pipenv install
```

**4. Create a new MySQL Schema and modify settings.py accordingly:**

```
$ mysql -u <username> -p <password> < <project_dir>/build/init_local_db.sql
```

**5. Migrate to MySQL:**

```
$ python manage.py migrate
```

**6. Create a superuser:**

```
$ python manage.py createsuperuser --username=yourusername --email=youremail
```

**7. Run the server:**

```
$ python manage.py runserver
```

Output:

```
Django version 2.1.2, using settings 'prizy.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

All done. The server is up and running!

## Contributions

See the repo's [wiki](https://github.com/Larissa-Developers/prizy_backend/wiki) for information on the project design and pending tasks ([Trello board](https://trello.com/b/zIPr3q6l/prizy-backend)), as well as the Code of Conduct for teamwork ground rules.

## References

* [Django Documentation](https://docs.djangoproject.com/en/2.1/)
* [Django REST Tutorials & API Guide](https://www.django-rest-framework.org/)
* [Git tutorials](https://www.atlassian.com/git/tutorials)

# Prizy back-end API architecture

Design, API resources and overall functionality draft.

Dimitris Gravanis - <dimgrav@gmail.com>

## About

Prizy will use a mobile, cross-platform thin client to provide members of the **Larissa Developers Meetup**, or event attendees, functionality for participating in prize draws of the occuring event in real-time.

Additionally, its back-end should provide functionality at an admin-level, i.e. an admin panel for account management and for performing prize draws.

Therefore, the application architecture must ensure the security, integrity and partial (client-side) immutability of the performed transactions.

The goal is to provide a concrete platform for future expansion, tailored to any potential upgrades of the mobile client.

## Client Requirements

The mobile client provides the following functionality:

* User registration
* Ongoing event listing
* Participation in Larissa Developers Meetup prize draws
* Prize claim

As such, the API must implement the following:

## API Design

In a (really abstract) nutshell:

```
api
.
├── accounts
│   └── ...
└── events
    └── ...
```

The API should provide the following endpoints:

#### Open

Landing page:

```
{domain}/ (GET)
```

#### Users

JWT authentication / token refresh / verification:

```
{domain}/auth (POST)
{domain}/refresh (POST)
{domain}/verify (POST)
```

User registration:

```
{domain}/api/accounts/register (POST)
```

Event listing:

```
{domain}/api/events (GET)
```

Event check-in:

```
{domain/api/events/<event_id>/checkin (POST)
```

Event draw participation:

```
{domain}/api/events/<event_id>/draws/<draw_id>/participate (POST)
```

Event draw prize claim:

```
{domain}/api/events/<event_id>/draws/<draw_id>/claim (POST)
```

The fundamental principle behind registration, is that a Meetup event attendee will be able to participate only if he has registered for an account.

As a result, draw participations will be handled implicitly, based on the account data (i.e the provided email address), without requiring any additional user information to be submitted via the mobile client app.

### Admin-specific

Django admin panel:

```
{domain}/admin (GET)
```

Perform event prize draw:

```
{domain}/api/events/<event_id>/draws/<draw_id>/perform (POST)
```

## Technologies

Prizy back-end will be built upon:

* [Django 2.1](https://www.djangoproject.com/)
* [Django REST Framework](http://www.django-rest-framework.org/)
* [Django REST Framework JWT](https://getblimp.github.io/django-rest-framework-jwt/)
* [MySQL Server 5.7](https://www.mysql.com/)
* [Python MySQL client](https://pypi.python.org/pypi/mysqlclient)

## To-do list

All of the above! :P

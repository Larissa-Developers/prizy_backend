## Prizy API Postman Collection

Request listing for developing Prizy with Postman

#### Authentication

* `POST` JWT Auth Admin: Authentication request for superuser accounts using JWT
* `POST` JWT Auth User: Authentication request for user accounts using JWT
* `POST` JWT Verify: Token verification for all accounts
* `POST` JWT Refresh: Token refresh for all accounts

#### Accounts

* `POST` Account Setup: Password setup for a pre-created user account
* `POST` Account Register: User account registration
* `PATCH` Account Details: User account information editing
* `GET` Account Details: User account information view
* `GET` Account List: Listing of all registered user accounts
* `GET` Account Setup: Verify registration status for the requested user account

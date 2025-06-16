# okta-with-django
Okta Auth with Django JWT. This is a project that demonstrates how you could implement a fully featured JSON Web Token Authentication system in Django, Okta and React. This includes showing how to implement features like account activation, password reset, and also social authentication with google and facebook oauth2. Further improvements to make it more production ready would just be to utilize the refresh token to get a new access token when the application reloads and also reloads when you go to an important page such as a checkout page, and having alerts present on the frontend to make things more user friendly.

## Okta Auth with Django REST Framework (DRF) API

- Integrate Okta as an external identity provider for authentication.
- Use [django-rest-framework-simplejwt](https://github.com/jazzband/django-rest-framework-simplejwt) for JWT authentication in your Django API.
- Configure Okta to issue JWTs and set up Django to validate these tokens.
- Protect your API endpoints by requiring valid JWTs in the `Authorization` header.
- Use Okta's OAuth2 endpoints for login and token refresh.
- Ensure your Django settings include Okta's public keys for JWT verification.
- Handle user registration, login, and social authentication via Okta, then use the JWT for API access.
- For more details, see [Okta's Django integration guide](https://developer.okta.com/docs/guides/sign-into-web-app/django/main/).


## Okta
```bash
https://manage.auth0.com/dashboard/us/dev-vnynddj36ad11hlo/applications/9cPu4fNzEIUyaENZRGuTNYCjIITVO5ox/credentials
```

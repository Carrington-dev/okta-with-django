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
Here are **clear, structured notes** on integrating **Okta authentication in Django REST Framework (DRF)**—similar to how you'd integrate Google or Facebook sign-in:

---

## 🔐 Okta Authentication with Django REST Framework (DRF)

### 🎯 Objective:

Allow users to log in to your DRF-powered backend using Okta SSO (Single Sign-On), similar to social login via Google or Facebook.

---

### 🧰 Tools/Technologies:

* **Django** + **Django REST Framework**
* **Okta** (OIDC/OAuth2 Provider)
* **`mozilla-django-oidc`** or **`django-allauth`** or **custom JWT integration**
* **Okta Developer Account** ([https://developer.okta.com](https://developer.okta.com))

---

### 🛠️ Steps to Integrate Okta in DRF:

#### 1. **Create an Okta Application**

* Go to **Okta Developer Console**.
* Applications → **Create App Integration**
* Choose **OIDC - OpenID Connect** → Application Type: **Web**
* Set Sign-in redirect URI:

  ```
  http://localhost:8000/oidc/callback/
  ```
* Copy the:

  * **Client ID**
  * **Client Secret**
  * **Okta Domain**

---

#### 2. **Install Required Libraries**

```bash
pip install mozilla-django-oidc djangorestframework
```

Or if using JWT approach:

```bash
pip install python-jose requests
```

---

#### 3. **Configure Django Settings**

```python
# settings.py

INSTALLED_APPS += ['mozilla_django_oidc']

AUTHENTICATION_BACKENDS = [
    'mozilla_django_oidc.auth.OIDCAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
]

OIDC_RP_CLIENT_ID = '<your-client-id>'
OIDC_RP_CLIENT_SECRET = '<your-client-secret>'
OIDC_OP_AUTHORIZATION_ENDPOINT = 'https://<your-okta-domain>/oauth2/default/v1/authorize'
OIDC_OP_TOKEN_ENDPOINT = 'https://<your-okta-domain>/oauth2/default/v1/token'
OIDC_OP_USER_ENDPOINT = 'https://<your-okta-domain>/oauth2/default/v1/userinfo'
OIDC_OP_JWKS_ENDPOINT = 'https://<your-okta-domain>/oauth2/default/v1/keys'
OIDC_RP_SIGN_ALGO = 'RS256'
LOGIN_REDIRECT_URL = '/'
```

---

#### 4. **Create Login and Callback Views**

```python
from mozilla_django_oidc.views import OIDCAuthenticationRequestView, OIDCAuthenticationCallbackView

urlpatterns = [
    path('oidc/login/', OIDCAuthenticationRequestView.as_view(), name='oidc_login'),
    path('oidc/callback/', OIDCAuthenticationCallbackView.as_view(), name='oidc_callback'),
]
```

---

#### 5. **Optional: Custom Backend to Extract More Info**

Override the user creation logic:

```python
# myauth/backends.py
from mozilla_django_oidc.auth import OIDCAuthenticationBackend

class MyOIDCBackend(OIDCAuthenticationBackend):
    def create_user(self, claims):
        user = super().create_user(claims)
        user.email = claims.get('email')
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.save()
        return user
```

---

#### 6. **Protect DRF Views with Authentication**

Use `IsAuthenticated` on your DRF views:

```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"email": request.user.email})
```

---

### 🧪 Testing Locally

* Go to `/oidc/login/` → Redirects to Okta → Login → Returns to `/oidc/callback/` → Authenticated
* Use `Authorization: Bearer <access_token>` for DRF APIs if using JWT approach.

---

### ⚖️ Alternative: Use JWT from Okta in DRF

If you're using a **Single Page App (SPA)** or **mobile client**, you can:

1. Authenticate using Okta on the frontend.
2. Pass the **access token** (JWT) to your Django backend.
3. Use `python-jose` to validate token signature and claims.

Sample verification code:

```python
from jose import jwt
import requests

def verify_token(token):
    jwks_url = 'https://<okta-domain>/oauth2/default/v1/keys'
    jwks = requests.get(jwks_url).json()
    return jwt.decode(token, jwks, algorithms=['RS256'], audience='api://default')
```

---

### ✅ Benefits:

* Enterprise-grade SSO
* Secure and standards-compliant (OAuth2/OIDC)
* Similar flow to social login (Google/Facebook)

---

Let me know if you want:

* Frontend integration (React or mobile)
* Dockerized version
* JWT-based stateless setup
* Using `django-allauth` with Okta

<!-- Would you like a working sample repo or boilerplate to start with? -->

# Project02

## Construction Steps:

1. Backend:
   - API
   - Database
   - Handle users
   - etc...
2. Frontend: User facing component
   - Interact with the API
   - Make notes
   - Sign in/out
   - etc...
3. Connect database with the Backend
4. Deploy the backend, frontend and connect them.

## Instructions:

1. Create/connect venv.
2. Install the requirements.txt
   - If using conda use conda-forge
3. Create new Django Project.
   - django-admin startproject backend
4. Create app
   - python manage.py startapp api
5. Set up your **backend/settings.py** file.

```python
# Extra code:
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

# ...

ALLOWED_HOST = ["*"]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSESS": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# Application definition
# ...

INSTALLED_APPS = [
    # ...
    "api",
    "rest_framework",
    "corsheaders",
    ]

MIDDLEWARE = [
    # ...
    "corsheaders.middleware.CorsMiddleware",
]

# DEFAULT_AUTO_FIELD = ["django.db.models.BigAutoField"]
# ...

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWS_CREDENTIALS = True
```

6. Create & modify the **api/serializers.py** file
7. Modify the **api/views.py** file
8. Modify the **backend/urls.py** file
9. Run migrations.

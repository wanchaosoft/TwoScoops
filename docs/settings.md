dynamic settings:

example 1:

```python
# At the top of settings/base.py
from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)
MEDIA_ROOT = BASE_DIR.child("media")
STATIC_ROOT = BASE_DIR.child("static")
STATICFILES_DIRS = (
BASE_DIR.child("assets"),
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        DIRS = (BASE_DIR.child("templates"),)
    },
]
```

```python
# At the top of settings/base.py
from os.path import join, abspath, dirname

here = lambda *dirs: join(abspath(dirname(__file__)), *dirs)
BASE_DIR = here("..", "..")
root = lambda *dirs: join(abspath(BASE_DIR), *dirs)
# Configuring MEDIA_ROOT
MEDIA_ROOT = root("media")
# Configuring STATIC_ROOT
STATIC_ROOT = root("collected_static")
# Additional locations of static files
STATICFILES_DIRS = (
root("assets"),
)
# Configuring TEMPLATE_DIRS
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        DIRS = (root("templates"),)
    },
]
```

### Django project SECRET_KEY should set environment variable
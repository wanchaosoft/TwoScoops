Model Instruction
================

> models.field.GenericForeignKey


Migrations
----------

management command::

    $ python manage.py makemigrations
    $ python manage.py migrate

but if you encounter other conditions,the following is referring::

    1. Empty the ``django_migrations`` table: delete from ``django_migrations``;
    2. For ``every app``, delete its migrations folder: ``rm -rf <app>/migrations/``
    3. Reset the migrations for the "built-in" apps:
        ``python manage.py migrate --fake``(Take care of dependencies )
    4. For each app run: ``python manage.py makemigrations <app>``
    5. ``python manage.py migrate --fake-initial``
    6. The same as most common conditions.


python instance example:: python
    import sys
    import os


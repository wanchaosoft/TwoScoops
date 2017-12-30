> ### Use Multiple Settings and Requirements

for different settings, you can use following command(when you are in `Projet-Root-Directory`):
``python manage.py runserver --settings=config.local``,
通过指定配置文件来确定运行服务器.

other command like this:
> python manage.py runserver --settings=config.staging

> python manage.py runserver --settings=config.test

> python manage.py runserver --settings=config.production


### Keep secret_key out of code, in Environment Variable.
Please read the README.md document based on fork from [python-django-gunicorn]{https://gitlab.com/osevg/)

This deploys a Python and JavaScript web application using Django and Vue.js through OpenShift v3, being served with 'gunicorn'.

## Deployment Instructions

After an application has been created in the OpenShift (Next Gen)  system (typically done in the web application), when using the 'oc' command line tools, create a new application with the below link and the Django Secret key associated with a project.
```bash
oc new-app https://gitlab.com/osevg/python-django-gunicorn.git --env DJANGO_SECRET_KEY='<key>' python:latest
```

## Connection to PostgreSQL Database
TODO



In this case, because no language type was specified, OpenShift will determine the language by inspecting the code repository. Because the code repository contains a ``requirements.txt``, it will subsequently be interpreted as including a Python application. When such automatic detection is used, ``python:latest`` will be used.

If needing to select a specific Python version when using ``oc new-app``, you should instead use the form:

```
oc new-app python:2.7~https://gitlab.com/osevg/python-django-gunicorn.git  --env DJANGO_SECRET_KEY='...'
```

For this sample application the database will not be initialised automatically and this must be done manually. Further, no super user account will be created.

To initialise the database and create the super user you will need to access the running container for the application using an interactive shell and manually run:

```
python manage.py migrate
python manage.py createsuperuser
```

You will then be able to login into the Django admin interface for the application.

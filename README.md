# Django Sample Application

This repository provides a sample Python web application implemented using the Django web framework and hosted using ``gunicorn``. It is intended to be used to demonstrate deployment of Python web applications to OpenShift 3.

## Production Warnings

The manner in which this sample application has been set up is not entirely suitable for a production deployment. For a production deployment the following changes would be required.

* A persistent volume would need to be used to store the SQLite database, and preferably a separate database service such as PostgreSQL or MySQL used instead.

## Implementation Notes

This sample Python application relies on the support provided by the default S2I builder for deploying a WSGI application using the ``gunicorn`` WSGI server. The requirements which need to be satisfied for this to work are:

* The ``gunicorn`` package must be listed in the ``requirements.txt`` file for ``pip``.

The following changes have been made in comparison to the standard Django application created by running ``django-admin.py startproject``:

* The Django ``DEBUG`` setting is set to ``False`` avoid exposing sensitive data when an exception occurs in the application.
* The Django ``SECRET_KEY`` setting is set from the ``DJANGO_SECRET_KEY`` environment variable.
* The Django ``STATIC_ROOT`` setting is set so that Django static files will be collected together and placed in the ``static`` directory.
* The Django ``LOGGING`` setting has been set up to send Django logging to standard error so that details of exceptions can be captured.
* The Django ``ALLOWED_HOSTS`` setting has been set to allow external connections.
* The Django ``MIDDLEWARE_CLASSES`` settings has been modified to add ``WhiteNoise`` middleware for hosting of static files.
* Add a Django handler for handling requests against the site.

In addition, the ``.s2i/environment`` file has been created to allow environment variables to be set to override the behaviour of the default S2I builder for Python.

* The environment variable ``APP_MODULE`` has been set to declare the location of the module containing the WSGI application entry point.
* The environment variable ``APP_CONFIG`` has been set to declare the name of the config file for ``gunicorn``.
* The environment variable ``DISABLE_MIGRATE`` has been set to disable automatic database migrations on deployments.

## Deployment Steps

To deploy this sample Python web application from the OpenShift web console, you should select ``python:2.7``, ``python:3.4`` or ``python:latest``, when using _Add to project_. Use of ``python:latest`` is the same as having selected the most up to date Python version available, which at this time is ``python:3.4``.

The HTTPS URL of this code repository which should be supplied to the _Git Repository URL_ field when using _Add to project_ is:

* https://gitlab.com/osevg/python-django-gunicorn.git

The ``DJANGO_SECRET_KEY`` environment variable should be set to a suitably long random string by selecting *Show advanced routing, build, and deployment options* and adding it under *Build Configuration*.
 
If using the ``oc`` command line tool instead of the OpenShift web console, to deploy this sample Python web application, you can run:

```
oc new-app https://gitlab.com/osevg/python-django-gunicorn.git --env DJANGO_SECRET_KEY='...'
```

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

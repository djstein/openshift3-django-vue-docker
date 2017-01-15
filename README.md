Please read the README.md document based on fork from [python-django-gunicorn]{https://gitlab.com/osevg/)

This deploys a Python and JavaScript web application using Django and Vue.js through OpenShift v3, being served with 'gunicorn'.

## Deployment Instructions

After an application has been created in the OpenShift (Next Gen)  system (typically done in the web application), when using the 'oc' command line tools, create a new application with the below link and the Django Secret key associated with a project.
```bash
oc new-app https://gitlab.com/osevg/python-django-gunicorn.git --env DJANGO_SECRET_KEY='<key>' python:latest
```

## Connection to PostgreSQL Database
TODO


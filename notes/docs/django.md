# Django and Flask
Combined Django and Flask frameworks.

## Table of Contents
* [Django](#django)
    * [Django Commands](#django-commands)
    * [Django Rest Api](#django-rest-api)
        * [Views with ModelViewSet](#views-with-modelviewset)
    * [Django Hosting](#django-hosting)
* [Flask]

<br><br>

---
## Django
[Learn Django page](https://learndjango.com/tutorials/) for django tutorials


[Polls Tutorial Django Doc](https://docs.djangoproject.com/en/3.1/intro/tutorial01/#the-development-server) and also a tutorial for setting up polls api [Learn DJango Blog]((https://learndjango.com/tutorials/django-polls-tutorial-api))


[Docker-compose and Django docs](https://docs.docker.com/compose/django/)  using postgresql database
<br><br>

---
### Django Commands
Start Project
```
Django-admin startproject {{project-name}} .
```
Migrations
```
python manage.py makemigrations {{component-name}}
python manage.py migrate {{component-name}}
```
Start server
```
python manage.py runserver
```
<br><br>

---
### Django Rest API
Tutorials on Building an API 
<br><br>

**Best Tutorial**
[Django rest framework blog](https://wsvincent.com/django-rest-framework-react-tutorial/) 


**Used this to setup Django Quiz** API [medium](https://medium.com/swlh/overview-building-a-full-stack-quiz-app-with-django-and-react-57fd07449e2f) and [github source](https://github.com/izennn/udemy-quiz-izen)


**Tried this one but gave up on it, didnt use**
Backend is very detailed [Medium Django and React](https://medium.com/swlh/how-to-deploy-django-rest-framework-and-react-redux-application-with-docker-fa902a611abf)


#### Views with ModelViewSet
Django views using ModelViewSet with main urls [stackoverflow](https://stackoverflow.com/questions/18194603/django-rest-custom-url-in-a-modelviewset)
<br><br>

---
### Django Hosting
**Self Hosted**
[Full stack testdriven](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/#postgres) Docker, Postgres, Gunicorn, Nginx, Static Files
<br><br>

**Hosted**
Can try deploying into [learn Django deployment options](https://learndjango.com/tutorials/django-hosting-deployment-options) 
    * Heroku
    * PythonAnywhere
    * Digital Ocean VPS
    * Linode 
    * Cloud but probably not (lightsail vs Elastic Beanstalk)
<br><br>

---
## Flask
[Flask Mega Tutorial blog](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world/page/10)

# Django and Flask
Combined Django and Flask frameworks.

## Table of Contents
* [Django](#django)
    * [Django Commands](#django-commands)
    * [Django Models](#django-models)
        * [Model Field Types](#model-field-types)
        * [Model Field References](#model-field-references)
        * [Metadata](#metadata)
        * [Model Methods](#model-methods)
    * [Django Views](#django-views)
    * [Django URLS](#django-urls)
    * [Django Rest Api](#django-rest-api)
        * [Views with ModelViewSet](#views-with-modelviewset)
    * [Django Hosting](#django-hosting)
    * [Django Projects](#django-projects)
* [Flask]
    * [API Flask](#api-flask)
    * [Flask Projects](#flask-projects)

<br><br>

---
## Django
[Learn Django page](https://learndjango.com/tutorials/) for django tutorials


[Polls Tutorial Django Doc](https://docs.djangoproject.com/en/3.1/intro/tutorial01/#the-development-server) and also a tutorial for setting up polls api [Learn DJango Blog]((https://learndjango.com/tutorials/django-polls-tutorial-api))


[Docker-compose and Django docs](https://docs.docker.com/compose/django/)  using postgresql database


![img](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page/basic-django.png)
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
### Django Models
[MDN Django Models](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models)


#### Model Field Types
[Django Docs on Model Field Types](https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-types)
* ForeignKey used to specify a one to many relationship
* ManyToManyField used to specify many to many relationship (a book can have several genres and each genre can contain several books)
* CharField used to specify strings must specify max_length 
* TextField used for large strings
* BooleanField
* IntegerField
* DateField or DateTimeField (auto_now_add=True)
* EmailField
* FileField used to upload files
<br>


#### Model Field References
[Django Docs on Model Field reference](https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-options)

* help_text a text label for HTML forms
* verbose_name a readable name for the field used in field labels.
* default the default value for the field
* null if true Django will store blank values as NULL (default false)
* blank If True the field is allowed to be blank. 
* choices
<br>

#### Metadata
[DJango Docs](https://docs.djangoproject.com/en/3.1/topics/db/models/#meta-options) on Meta options. Not necessary and optional but allow ordering and human readable name. Complete list of Meta options here[Django Docs](https://docs.djangoproject.com/en/3.1/ref/models/options/)
<br>

**Ordering**
used to control the default ordering of records when query the model type. Use (-) symbol to reverse sorting order.
```
class Meta:
    ordering = ['title', '-pubdate']
```
<br>

**Verbose Name/Verbose Name Plural**
A human readable name 
<br>

#### Model Methods
Can define a class method like str to return a readable string
```
def __str__(self):
    return self.field_name
```


Can also create custom methods
```
def question_count(self):
    return self.questions.count
```
<br><br>

---
### Django Views

<br><br>

---
### Django URLS

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


[Books.agiliq](https://books.agiliq.com/projects/django-api-polls-tutorial/en/latest/apis-without-drf.html) Building API Django tutorial. Using polls.

#### Views with ModelViewSet
**old way GenericViewSet, use ModelViewSet when possible** Generics make you build a ListCreapeAPIView and RetreiveUpdateDestroyAPIView. 

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

### Django Projects 
[MDN DJango](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) Building a local library tutorial [Git source](https://github.com/mdn/django-locallibrary-tutorial)


[Reddit](https://www.reddit.com/r/djangolearning/comments/im9hyx/learn_how_to_build_a_simple_twitter_clone_using/?sort=confidence) Building a twitter clone using django and vue.


[TestDriven](https://testdriven.io/blog/django-spa-auth/) Single Page authentication 
<br><br>

---
## Flask
[Flask Mega Tutorial blog](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world/page/10)


---
### API Flask
[Build an API with Flask](https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f)
<br><br>

---
### Flask Projects
[Hackster](https://www.hackster.io/mjrobot/from-data-to-graph-a-web-journey-with-flask-and-sqlite-4dba35) ussing flask and rpi temp sensor to build a graph.
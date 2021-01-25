# Docker
Sandbox docker environment [Play with docker](https://labs.play-with-docker.com/) 

A guide on developing React inside of Docker [blog](https://willschenk.com/articles/2020/developing_react_inside_docker/)

Setting up docker in pycharm and vscode [Stackoverflow](https://stackoverflow.com/questions/58855616/how-can-i-use-a-docker-container-as-a-virtualenv-for-running-python-tests-from-m)
<br><br>

Start with dockerignore
```
echo "venv .venv .git" > .dockerignore
```


## Table of Contents
* [Tutorials](#tutorials)
* [Docker Commands](#docker-commands)
    * [Flags](#flags)
    * [Build / Run / Push](#build-and-run-and-push)
    * [Docker Run](#docker-run)
* [Docker-compose Commands](#docker-compose-commands)
* [Dockerfile Example](#dockerfile-example)
    * [Jupyter Notebook Dockerfile](#jupyter-notebook-dockerfile)
* [Docker Django Stack](#docker-django-stack)


### Tutorials
Getting started tutorial/Todo app
```
docker run -d -p 80:80 docker/getting-started
```
[Docker-compose Docs](https://docs.docker.com/compose/gettingstarted/) using Flask, Redis to Count clicks.


### Docker Commands
Docker Syntax: docker {{cmd}} {{flags}} {{image:tag}} {{cmd}}
* build
* run
* exec
* ps 
* images
* stop


#### Flags
* -f = File name (defaults to Dockerfile)
* -t = tag
* -d = detached
* -p = port 
* -v = volume
* -e = environment
* -it = interactive shell
* --rm = remove the container once we exit
* --build-arg SOME_ENV_VAR=hello = Is the build time variable


#### Build and Run and Push
Docker Hub [Documentation](https://docs.docker.com/docker-hub/)
```
docker build -t coronel08/{{tag-name}} .
docker run -d -p {{ports}} --name {{name}} coronel08/{{tag-name}}
docker exec -it {{container-id}} bash # if bash fails try sh
docker push coronel08/{{tag-name}}
```


#### Docker Run
An example of docker run command to setup a python container
```
 docker run --rm -it python:3.8 python
 docker run --rm -p 8888:8888 jupyter/scipy-notebook
```
Long docker run example, the env in this is used for hotloading.
```
docker run \
    -itd \ 
    -- rm \
    -v {{${PWD}/folder:folder}} \
    -p {{port:port}} \
    -e CHOKIDAR_USEPOLLING=true \
    {{img_name}}
```


### Dockerfile Example
Run apt-get update and install. Dont forget to remove cahced data. Also use -y flag when installing


Can use either apt-get clean or the rm -rf command to clean 
```
RUN apt-get update && apt-get install -y\
package1\
package2\
&& apt-get clean
# && rm -rf /var/lib/apt/lists/* 

COPY requirements.txt /app/requirements.txt
WORKDIR app
RUN pip install --user -r 
COPY . /app
```


#### Jupyter Notebook Dockerfile 
Building a Jupyter Notebook Dockerfile [Mlinproduction blog](https://mlinproduction.com/docker-for-ml-part-2/)
```
FROM jupyter/scipy-notebook

ARG SOME_ENV_VAR
ENV SOME_ENV_VAR=${SOME_ENV_VAR}

RUN pip install awscli --upgrade --user
RUN echo 'export PATH=~/.local/bin:$PATHn' &gt;&gt; $HOME/.bashrc

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN rm ./requirements.txt
```
Build 
```
docker build --build-arg SOME_ENV_VAR=hello -t my-jupyter-image -f Dockerfile .
```
Run
```
docker run --rm -p 8888:8888 my-jupyter-image
```


---
## Docker-compose commands

* up
* down
* stop

```
docker-compose up -d --build #build flag recreates the file
```


---
## Docker Stack

### Docker Flask Stack
Dockerizing Flask with Postgres, Gunicorn and Nginx [Testdriven.io](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/)

### Docker Django Stack
[Docker docs Django](https://docs.docker.com/compose/django/)

Dockerizing Django with Postgres Gunicorn and Nginx [Testdriven.io](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)
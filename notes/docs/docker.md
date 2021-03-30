# Docker
Sandbox docker environment [Play with docker](https://labs.play-with-docker.com/) 

A guide on developing React inside of Docker [blog](https://willschenk.com/articles/2020/developing_react_inside_docker/)

Setting up docker in pycharm and vscode [Stackoverflow](https://stackoverflow.com/questions/58855616/how-can-i-use-a-docker-container-as-a-virtualenv-for-running-python-tests-from-m)
<br><br>

Start with dockerignore
```
echo "venv .venv .git" > .dockerignore
```

---
## Table of Contents
* [Docker](#docker)
    * [Tutorials](#tutorials)
    * [Docker Commands](#docker-commands)
        * [Flags](#flags)
        * [Build / Run / Push](#build-and-run-and-push)
        * [Docker Run](#docker-run)
    * [Docker-compose Commands](#docker-compose-commands)
    * [Dockerfile Example](#dockerfile-example)
        * [Jupyter Notebook Dockerfile](#jupyter-notebook-dockerfile)
    * [Docker Django Stack](#docker-django-stack)
* [Kubernetes](#kubernetes)
    * [Kubectl](#kubectl)
---
## Tutorials
Getting started tutorial/Todo app
```
docker run -d -p 80:80 docker/getting-started
```
[Docker-compose Docs](https://docs.docker.com/compose/gettingstarted/) using Flask, Redis to Count clicks.


---
## Docker Commands
Docker Syntax: docker {{cmd}} {{flags}} {{image:tag}} {{cmd}}
* build
* run
* exec
* ps 
* images
* rmi = remove images
* stop


### Flags
* -f = File name (defaults to Dockerfile)
* -t = tag
* -d = detached
* -p = port 
* -v = volume
* -e = environment
* -it = interactive shell
* --rm = remove the container once we exit
* --build-arg SOME_ENV_VAR=hello = Is the build time variable


### Build and Run and Push
Docker Hub [Documentation](https://docs.docker.com/docker-hub/)
```
docker build -t coronel08/{{tag-name}} .
docker run -d -p {{ports}} --name {{name}} coronel08/{{tag-name}}
docker exec -it {{container-id}} bash # if bash fails try sh
docker push coronel08/{{tag-name}}
```


### Docker Run
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
    -p {{port-to-open:container-port}} \
    -e CHOKIDAR_USEPOLLING=true \
    {{img_name}}
```

---
## Dockerfile Example
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


### Jupyter Notebook Dockerfile 
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

To recreate a single docker-compose component
* docker-compose stop {{container-name}}
* docker-compose up -d --no-recreate {{container_name}}



---
## Docker Stack

### Docker Flask Stack
Docker, Flask, React, Nginx [Medium](https://medium.com/swlh/deploy-and-secure-a-react-flask-app-with-docker-and-nginx-768ca582863b) 


Dockerizing Flask with Postgres, Gunicorn and Nginx [Testdriven.io](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/)


Flask, Sqlite, Nginx stack [tutorial-academy](https://tutorial-academy.com/uwsgi-nginx-flask-python-sqlite-docker-example/)


Flask, Docker, Nginx [towardsdatascience](https://towardsdatascience.com/how-to-deploy-ml-models-using-flask-gunicorn-nginx-docker-9b32055b3d0)


### Docker Django Stack
[Docker docs Django](https://docs.docker.com/compose/django/)


Dockerizing Django with Postgres Gunicorn and Nginx [Testdriven.io](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)
<br><br>

---
# Kubernetes
[kubernetes](https://kubernetes.io/docs/tasks/tools/) Install tools

* [Kind](https://kind.sigs.k8s.io/docs/user/quick-start/)
* [Minikube](https://minikube.sigs.k8s.io/docs/start/) and [Minikube Cluster tutorial](https://kubernetes.io/docs/tutorials/hello-minikube/)


[Logz.io](https://logz.io/blog/kubernetes-as-a-service-gke-aks-eks/) Kubernetes on cloud providers **loosing support for docker containerd**

## Kubectl

kubectl [command] [TYPE] [NAME] [flags]
```
kubectl create -f {{./pod.json}}
kubectl apply -f {{example-service.yaml}}
```
kubectl get
```
# List all pods in plain-text output format.
kubectl get pods

# List all pods in plain-text output format and include additional information (such as node name).
kubectl get pods -o wide

# List all daemon sets in plain-text output format.
kubectl get ds

# List all pods running on node server01
kubectl get pods --field-selector=spec.nodeName=server01
```
kubectl describe
```
# Display the details of the node with name <node-name>.
kubectl describe nodes <node-name>

# Display the details of the pod with name <pod-name>.
kubectl describe pods/<pod-name>

# Describe all pods
kubectl describe pods
```
kubectl delete
```
# Delete a pod using the type and name specified in the pod.yaml file.
kubectl delete -f pod.yaml

# Delete all the pods and services that have the label '<label-key>=<label-value>'.
kubectl delete pods,services -l <label-key>=<label-value>

# Delete all pods, including uninitialized ones.
kubectl delete pods --all
```
kubectl exec
```
# Get output from running 'date' from pod <pod-name>. By default, output is from the first container.
kubectl exec <pod-name> -- date

# Get output from running 'date' in container <container-name> of pod <pod-name>.
kubectl exec <pod-name> -c <container-name> -- date

# Get an interactive TTY and run /bin/bash from pod <pod-name>. By default, output is from the first container.
kubectl exec -ti <pod-name> -- /bin/bash
```
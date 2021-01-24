# my-notes
Using mkdocs to document my notes on different languages, frameworks, and other. 


For full documentation visit [mkdocs.org](https://www.mkdocs.org).


## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.


## Table of Contents
* [Setup](#setup)
* [Todo](#todo)


### Setup
To setup venv:
```
virtualenv venv

<!-- ACTIVATE VENV
linux: source venv/bin/activate
windows: venv/Scripts/activate
 -->
```
To setup git
```
cat > .gitignore
echo "#Project" > README.md
git init
echo "venv .venv .git" > .dockerignore 
```


### Todo
* [x] Setup venv, python, requirements.txt
* [x] Makedocs
    * [ ] Organize notes
* [ ] Dockerize and setup in reverse proxy
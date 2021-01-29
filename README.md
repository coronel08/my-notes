# My-Notes
Using mkdocs to document my notes on different languages, frameworks, and other. 


For [mkdocs tutorial](https://towardsdatascience.com/creating-software-documentation-in-under-10-minutes-with-mkdocs-b11f52f0fb10)

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
**mkdir -p** (parent) flag to create nested folders


### Todo
* [x] Setup venv, python, requirements.txt
* [x] Makedocs
    * [ ] Organize notes
* [x] Dockerize and setup in reverse proxy
    * [x] Setup Nginx Reverse Proxy
* [ ] Work on React section
    * [ ] API section needs work
        * [ ] Axios vs ____
    * [x] Functions vs Classes
    * [x] Add callbacks vs promises
    * [x] Add classes  vs functions
    * [x] Add React Hooks
        * [x] useState()
        * [x] useEffect()
* [ ] Javascript needs arrow function and other notes
* [x] Work on Django section
    * [x] Add notes on building an api and setting up backend. 
    * [ ] Keep Adding to Django section
* [x] Add Flask Rest section to Django
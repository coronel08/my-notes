# My-Notes
Using mkdocs to document my notes on different languages, frameworks, and other. 

overwrites styling by adding styles in ``` /notes/docs/extra.css```

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


### Run
Run live development server
```
cd notes && mkdocs serve -a localhost:8003
```


### Deploy
Deploy to aws s3 bucket using [Toward AWS](https://towardsaws.com/build-a-simple-devops-pipeline-from-github-to-aws-s3-for-static-website-911c620dce31)

### Todo
* [x] Setup venv, python, requirements.txt
* [x] Makedocs
    * [ ] Organize notes
* [x] Dockerize and setup in reverse proxy
    * [x] Setup Nginx Reverse Proxy
* [x] Work on React section
    * [ ] API section needs work
        * [x] Axios vs Fetch
    * [x] Functions vs Classes
    * [x] Add callbacks vs promises
    * [x] Add classes  vs functions
    * [x] Add React Hooks
        * [x] useState()
        * [x] useEffect()
* [x] Javascript needs arrow function and other notes
* [x] Work on Django section
    * [x] Add notes on building an api and setting up backend. 
    * [ ] Keep Adding to Django section
* [x] Add Flask Rest section to Django
* [ ] Add python 
    * [ ] [Python full stack](https://www.fullstackpython.com)
    * [ ] [FreeCodeCamp](https://www.freecodecamp.org/news/the-ultimate-guide-to-the-pandas-library-for-data-science-in-python/amp/) Pandas
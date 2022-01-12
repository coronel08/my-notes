# New Job Notes

## Table of Contents

-   [Agile](#agile-training)
    -   [Scrum](#scrum)
        -   [Sprints](#sprints)
-   [Jira](#jira-training)
-   [Coding Standards](#coding-standards)

## Agile Training

Agile Manifesto, incremental growth, Offers flexibility, speed, teamwork, and constant improvement

-   Individuals and interactions over proccesses and tools
-   Working software over comprehensive documentation
-   Customer Collaboration over contract negotiation
-   Responding to change over following a plan

### Scrum

Scrum, an Agile framework (others would be lean, etc). Uses sprints 1-2 week project intervals

1. Transparency
2. Inspection
3. Adaption

Broken into **Roles**, **Events**, and **Artifacts**

-   Roles
    -   Project Manager - leads project as scrum master
    -   Development Team - deliver MVP at the end of sprint

Process - the 5 phases of a project

1. Setup - review scope, create jira and tasks
2. LiftOff - plan the 1st sprint, discussion and refinement
3. Discovery - researching and refining mostly around UX/UI design

    - Acceptance Critera - with User Stories, provides the whole deliverable. Defined in Discovery Phase. Calrify goal, common understanding, and testing.
      User Stories - describes the type of user, what they want and why.Written as "As a **user type**, I want to **description of function/use case**, so that **reason why**"
        - frontend - should have wireframes and diagrams
        - backend - should have exmaples of schema and response

4. Delivery - MVP allows for early feedback. Use a checklist of USer Stories or PBI's(Product Backlog Items) to check against to verify completeness.
5. Closeout - Account Management reengagement with form signed by client, unused accounta are decommissioned, docs completed, summary slideshow created, battlecard created.

#### Sprints

Fixed timeline of events, duration of a month or less with a goal.

-   sprint planning - max of 8 hours, collaborate on understanding the sprint goal. should achieve the product backlog items and sprint goal.
-   Daily Scrum - 15 minute event for the development team. review progress on completing Sprint Backlog.
-   Sprint Reviews - at most 4 hours, held at the end of the sprint to inspect the backlog and product.
-   Sprint Restrospective - opportunity for scrum team to inspect itself and create a plan for improvements.
-   Product Backlog - ordred list of everything that is known to be needed for the product. development team is responsilbe for all estimates.

## Jira Training

Classic Scrum or CLassic Kanban boards for templates. Then add team members, members can have multiple roles but should have team to be able to edit.
Next add tasks or sprints to interface.
Can create notifications for issues. go to filters => Issues

-   [Create a Project Template Jira Software](https://developer.atlassian.com/server/jira/platform/creating-a-project-template/)
-   [Create a Template Jira Confluence](https://confluence.atlassian.com/doc/create-a-template-296093779.html)

-   Press W key or . key for search dialog to log work can look into 10 ways to Log Work with Tempo,

**Heirarchy of Jira**

-   Epic - Large body of work broken down into smaller chunks
-   Story - focuses on user features "As a customer I want to be able to - for this - reason "
-   Issues/Task/Bug - Smaller chunks of work
-   Sub-Task - Tasks that shouldn't take longer than a day

**Example of Jira**

-   Epic - User Authentication
-   User Stories
    -   User Login Screen
    -   Forgot Password workflow
    -   Google login support
-   Sub Task
    -   User Login Screen:
        -   Design Page
        -   Icons and Images
        -   Implement Login page html/css/js
        -   SQL to create tables
        -   REST APi for resources
-   (Engineering) Tasks:
    -   Setup Git Repo
    -   AWS account and Containers
    -   CI pipeline

## Coding Standards

-   Score of 8 or higher in Linter
-   avoid using vague variables ` def a(x,y): return x + y` vs `def addition(input_one, input_two): return input_one + input_two`
-   Method definitions inside a class are surrounded by a single line break
-   Imports placed at top of file, file library imports are place on seperate lines. group in the order below
    -   standard library imports
    -   third party imports
    -   local application imports
-   avoid global variables
-   Add docstrings, can use vs code extensions such as Python Docstring Generator
    -   file level docstrings do the following:
        -   describe functionality
        -   explanation of inputs, especially if source location is an AWS Resource
        -   Explanation of output and target location
        -   Name of code author
-   Dates are to be sanitized or standardized using a date parser, the parser from dateutil cam be used. look into `strftime()`

### File and Project conventions

-   Lambda - function names should be prefixed with the account or project name. Additional files should be descriptivve to their function
-   3rd party imports should be included in a ` requirements.txt` or `package.json` included in the project repo.
    -   Pigar or Dephell, tools to generate requirements
-   Include unit testing and integration, include triggers for Cloudwatch or API calls
-   API's are to be secured with an authorizer [AWS Chalice](https://aws.github.io/chalice/quickstart.html)

##

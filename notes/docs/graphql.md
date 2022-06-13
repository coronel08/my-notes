# GraphQL
Queries done in a JS object syntax that offers the ability to define what data to retrieve. 

## Table of Contents
- [GraphQL](#graphql)
    - [Queries](#queries)
    - [Schemas and Types](#schemas-and-types)
    - [Mutations](#mutations)
    - [Grapiql Tool](#grapiql-tool)


### Queries
request example 

```
{
    client(id: "100"){
        name,
        client{
            name
        }
    }
}
```

returns a response like below
{
    "data": {
        "project": {
            "name":"App",
            "client": {
                name:"Test Name"
            }
        }
    }
}


### Schemas and Types
a strongly typed language, the schema specifies the fields as well as the types. 
* Scalar Types Include: String, Int, Float, Boolean, ID

### Mutations
Update data queries, use keyword mutation
```
mutation {
    addProject(
        name: "App",
        description: "test description",
        status: "not started",
        clientId: "1"){
            name
            description
            status
        }
}
```

returns as a response
{ 
    "data": {
        "addProject": {
            "name": "App",
            "description": "test description",
            "status":"not started"
        }
    }
}



### GrapiQL Tool
A tool that comes with the graphql server used to test out queries in Graphql

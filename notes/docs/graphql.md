# GraphQL
Queries done in a JS object syntax that offers the ability to define what data to retrieve. 

## Table of Contents
- [GraphQL](#graphql)
    - [Schemas and Types](#schemas-and-types)
        - [Queries](#queries)
        - [Mutations](#mutations)
        - [Subscriptions](#subscriptions)
        - [Resolvers](#resolvers)
        - [Grapiql Tool](#grapiql-tool)

## Schemas and Types
a strongly typed language, the schema specifies the fields as well as the types. 
* Scalar Types Include: String, Int, Float, Boolean, ID

### Queries
Read only fetch for data

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


### Mutations
Update data queries, use keyword mutation. Write followed by a fetch
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


### Subscription
A long lived connection for receiving data


### Resolvers
GraphQl resolvers connect the fields in a types schema to a data source. 

### GrapiQL Tool
A tool that comes with the graphql server used to test out queries in Graphql

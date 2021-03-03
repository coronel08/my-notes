# Database

| SQL        | NOSQL      |
| :--------- |:---------- |
| SQlite     | MongoDB    |
| Postgres   | CouchDB    |
| Microsoft  | Redis      |


---
## Table of Contents
* [MongoDB](#mongodb)
* [SQL](#sql)


---
## MongoDB
[Mongo Docs](https://docs.mongodb.com/manual/reference/operator/query/) Operators such as greater than or in

* db
* show databases or show dbs
* show collections
* use {{db_name}}   - create and switch to db
* db.{{db_name}}.find()
* db.{{db_name}}.find({key:"value"})   - find specific item using key and value
* 

### CRUD
[Mongo Docs](https://docs.mongodb.com/manual/tutorial/insert-documents/) Insert Documents
[Mongo Docs](https://docs.mongodb.com/manual/crud/) CRUD
Can use the one or many ending for Crud operations


Create
* db.{{db_name}}.insert({name:"Charlie", age:3, breed:"corgi"})
Update
* db.{{db_name}}.updateOne({name:"Charlie"}, {$set: {age:5}})
Delete
* db.{{db_name}}.deleteOne({name:"Charlie"})
* db.{{db_name}}.deleteMany({})    - This deletes evrything
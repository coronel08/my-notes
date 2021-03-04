# Database

| SQL        | NOSQL      |
| :--------- |:---------- |
| SQlite     | MongoDB    |
| Postgres   | CouchDB    |
| Microsoft  | Redis      |


---
## Table of Contents
* [MongoDB](#mongodb)
    * [CRUD](#crud)
        * [Mongoose ODM](#mongoose-odm)
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

Example of finding movie using $in operator in Mongo
db.{{db_name}}.find({title: {$in: ['Amadeus', 'Stand By Me']}})
Example of updating using Mongoose, similar to Mongo
Movie.updateMany({title: {$in:['Amadeus', 'Stand By Me']}}, {score: 10}).then(res => console.log(res))

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


#### Mongoose ODM
[Mongoose Docs](https://mongoosejs.com/docs/guide.html) Schema 
[Mongoose Docs](https://mongoosejs.com/docs/api/model.html#model_Model.find) Model.find(), finding an object in the database using monoose. Also offers things like Model.findOneAndReplace() and other methods. 
[Mongoose Docs](https://mongoosejs.com/docs/guide.html#definition) Making a Schema and Model and Instance methods and Static methods
[Mongoose Docs](https://mongoosejs.com/docs/tutorials/virtuals.html) Can do Virtuals to create temp functions
**For examples using database check out /MongoDB/index.js and /MongoDB/product.js**

When updating an item, remember to make update validate.
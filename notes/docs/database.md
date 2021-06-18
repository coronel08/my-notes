# Database
* Learn SQL [SQL ZOO](https://sqlzoo.net/) or [w3](https://www.w3schools.com/sql/)
* Pandas instead of SQL[Haki Benita Site](https://hakibenita.com/sql-for-data-analysis)
* Move from excel to Python[Medium](https://towardsdatascience.com/a-complete-yet-simple-guide-to-move-from-excel-to-python-d664e5683039)

| SQL        | NOSQL      |
| :--------- |:---------- |
| SQlite     | MongoDB    |
| Postgres   | CouchDB    |
| Microsoft  | Redis      |


## Schema
* Schema - A schema is a container for tables
    * Columns - Header within a table
        * Row - An entry in a table
* Constrains - Rules such as Unique, Not Null, Default
    * Primary Key - a unique identifier such as employee id or primary key
    * Foreign Key - A link between two or more tables
        * Relation
            * one to few - example a user address
            * one to many - medium amount of data approach, store data seperately but reference item thru id
            * one to million - large amount of data, easier to reference the parent on the child doc. Works well for a tweet, a user can have million tweets.
    * Indexes - A constraint created on a column that speeds up the retrieval of data by treating them as unique values. Best used for non primary key or non foreign key. Best used for something like a date
    * Views - virtual table of one or more columns from one or more tables (do not update any data in a view)
    * Stored Procedures - pre compiled sql query 
    ```
    <!-- Where Salaried Employee flag is 1  -->
    EXEC HumanResources.SalariedEmployees @Salaried-Flag=1
    ```
    * Triggers - code that happens when an event happens
    ```
    <!-- Creates a notification stating that a new dept has been created when an INSERT statement is executed against the dept table -->
    CREATE TRIGGER NewDepartment
    ON HumanResources.Department
    AFTER INSERT
    AS RAISEERROR('A new dept has been created',10,9)

    <!-- Add new Dept to Dept table -->
    INSERT INTO HumanResources.Department
    (Name, GroupName, ModifiedDate)
    Values
    ('Business Analysis', 'Research and Development', GET-DATE())
    ```
---
## Table of Contents
* [SQL](#sql)
* [MongoDB](#mongodb)
    * [CRUD](#crud)
        * [Mongoose ODM](#mongoose-odm)

---
# SQL 
## Syntax Basics
```
SELECT <expressions>
FROM <tables>
JOIN <to other table> ON <join condition>
WHERE <predicates>
GROUP BY <expressions>
HAVING <predicate>
ORDER BY <expressions>
LIMIT <number of rows>
```

Example Query
```
WITH emails as (
    SELECT 'me@email.com' AS email
)
SELECT * from emails;
```
Another example
```
WITH emp AS (
    SELECT * FROM (VALUES
        ('Haki',    'R&D',      'Manager'),
        ('Dan',     'R&D',      'Developer'),
        ('Jax',     'R&D',      'Developer'),
        ('George',  'Sales',    'Manager'),
        ('Bill',    'Sales',    'Developer'),
        ('David',   'Sales',    'Developer')
    ) AS t(
        name,       department,  role
    )
)
SELECT * FROM emp;

  name  │ department │   role
────────┼────────────┼───────────
 Haki   │ R&D        │ Manager
 Dan    │ R&D        │ Developer
 Jax    │ R&D        │ Developer
 George │ Sales      │ Manager
 Bill   │ Sales      │ Developer
 David  │ Sales      │ Developer
```

**Create a Pivot table in PANDAS vs SQL**
```
<!-- PANDAS VERSION -->
import pandas as pd
df = pd.DataFrame({
    'name': ['Haki', 'Dan', 'Jax', 'George', 'Bill', 'David'],
    'department': ['R&D', 'R&D', 'R&D', 'Sales', 'Sales', 'Sales',],
    'role': ['Manager', 'Developer', 'Developer', 'Manager', 'Developer', 'Developer'],
})
pd.pivot_table(df, values='name', index='role', columns='department', aggfunc='count')


<!-- SQL VERSION -->
WITH emp AS (
    SELECT * FROM (VALUES
        ('Haki',    'R&D',      'Manager'),
        ('Dan',     'R&D',      'Developer'),
        ('Jax',     'R&D',      'Developer'),
        ('George',  'Sales',    'Manager'),
        ('Bill',    'Sales',    'Developer'),
        ('David',   'Sales',    'Developer')
    ) as t(
        name, department, role
    )
)

<!-- Using CASE but Aggregate Expressions with COUNT is better
SELECT
    role,
    SUM(CASE department WHEN 'R&D' THEN 1 ELSE 0 END) as "R&D",
    SUM(CASE department WHEN 'SALES' THEN 1 ELSE 0 END) as "Sales" 
-->
SELECT
    role,
    COUNT(*) FILTER (WHERE department = 'R&D') as "R&D",
    COUNT(*) FILTER (WHERE department = 'SALES') as "Sales"

FROM
    emp
GROUP BY
    role;
```

## Database Normalization

---

### 1NF 
* No multiple values in a single cell
* No repeating groups/columns of data
* A Primary or Composite key of each table

|Product ID |Product Name  | Amount|
-------- | ------- | -------
| 1 | whey protein | 2 lbs |
| 1 | whey protein | 4 lbs |
| 2 | tea | 12 pack |
| 2 | tea | 24 pack |
| 3 | amino acids | 60 capsules |
| 3 | amino acids | 90 capsules |

**Turns into two tables to avoid duplicate Product ID**

|Product ID(PK) |Product Name  |
-------- | ------- |
| 1 | whey protein |
| 2 | tea |
| 3 | amino acids |


|Product ID(PK) | Amount |
-------- | ------- |
| 1 | 2 lbs |
| 2 | 4 lbs |
| 3 | 12 pack |
| 4 | 24 pack |
| 5 | 60 capsules |
| 6 | 90 capsules |
---
### 2NF
* First normal form completed
* Remove any non-key column that's not dependent on the primary key
* Implement a foreign key

| Product ID(PK) | Product Name  | Product Description | Supplier |
-------- | ------- | -------- | ------- |
| 1 | whey protein | milk based protein | Friendly Supplements |
| 2 | tea | packaged in bags | Worldly Drinks |
| 3 | amino acids | make up protein | Friendly Supplements |

**Should be split into 2 tables to separate supplier**

| Product ID(PK) | Product Name  | Product Description | Supplier ID(FK) |
-------- | ------- | -------- | -------- |
| 1 | whey protein | milk based protein | 1 |
| 2 | tea | packaged in bags | 2 |
| 3 | amino acids | make up protein | 1 |

| Supplier ID(PK) | Supplier |
-------- | ------- |
| 1 | Friendly Supplements |
| 2 | Worldly Drinks |
---

### 3NF
* Second normal form completed
* Eliminate any transitive functional dependencies

| Product ID | Product Name  | Category ID | Category Name |
-------- | ------- | -------- | ------- |
| 1 | protein powder | 1 | Sports and Fitness |
| 2 | tea | 2 | Food and Drink |
| 3 | amino acids | 1| Sports and Fitness |
| 4 | coffee | 2| Food and Drink |

**Split table in two**

| Product ID (PK) | Product Name  | Category ID (FK) |
-------- | ------- | -------- |
| 1 | protein powder | 1 |
| 2 | tea | 2 |
| 3 | amino acids | 1|
| 4 | coffee | 2|

| Category ID(PK) | Category Name |
-------- | ------- |
| 1 | Sports and Fitness |
| 2 | Food and Drinks |

Or also create a mapping table with 2 foreign keys and remove the "Category ID" from the "Product Table"
| Product ID(FK) | Category ID(FK) |
-------- | ------- |
| 1 | 1 |
| 2 | 2 |
| 3 | 1 |
| 4 | 2 |

---
# MongoDB
[Mongo Docs](https://docs.mongodb.com/manual/reference/operator/query/) Operators such as greater than or in

* db
* show databases or show dbs
* use {{db_name}}   - create and switch to db
* show collections   - use after switching to db to see contents
* db.{{db_name}}.find() - to show everything in collections
* db.{{db_name}}.find({key:"value"})   - find specific item using key and value

Example of finding movie using $in operator in Mongo
db.{{db_name}}.find({title: {$in: ['Amadeus', 'Stand By Me']}})
Example of updating using Mongoose, similar to Mongo
Movie.updateMany({title: {$in:['Amadeus', 'Stand By Me']}}, {score: 10}).then(res => console.log(res))

## CRUD
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

Put vs Patch request. Put = overwrites while Patch = changes a portion

### Mongoose ODM
[Mongoose Docs](https://mongoosejs.com/docs/guide.html) Schema 
[Mongoose Docs](https://mongoosejs.com/docs/api/model.html#model_Model.find) Model.find(), finding an object in the database using monoose. Also offers things like Model.findOneAndReplace() and other methods. 
[Mongoose Docs](https://mongoosejs.com/docs/guide.html#definition) Making a Schema and Model and Instance methods and Static methods
[Mongoose Docs](https://mongoosejs.com/docs/tutorials/virtuals.html) Can do Virtuals to create temp functions
**For examples using database check out /MongoDB/index.js and /MongoDB/product.js**

[MongoDB Blog](https://www.mongodb.com/blog/post/6-rules-of-thumb-for-mongodb-schema-design-part-3) schema blog rules pt3

When updating an item, remember to make update validate.


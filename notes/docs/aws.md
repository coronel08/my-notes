# AWS
Can work with AWS through AWS Management Console, CLI, or SDK

Elastic Beanstalk - allows for code and desired configuration and provisions of instances
AWS CloudFormation - is a Yaml based tool used to define resources

## Table of contents



## Notes


## EC2


### Instance Types
* General Purpose - Balanced
* Compute Optimized - for processing heavy loads
* Memory Optimized - for something like a high performance database
* Accelerated Computing - graphics or streaming
* Storage Optimized - Data warehousing or high read and write performance

Serverless Computing
* AWS lambda - Cloud function that only gets charged when triggered 
* ECS - Elastic Container Service
* EKS - Elastic Kubernetes Service
* Fargate - Works with both ECS and EKS, its a container engine

### Pricing
* On Demand - always available 
* EC2 Savings Plan - Ideal for workloads that require consistent compute usage 1 year or 3 year terms. 72% savings
* Reserved Instance - Billing discount applied to On Demand instance with 1 year or 3 year renewal
* Spot Instance - Ideal for flexible workloads or one that can withstand interruptions. 90% savings
* Dedicated Host - Fully dedicated to one host

### Scaling
* EC2 Auto Scaling - Auto optimizes servers and instances to meet needs, can set min, desired, and max
* Elastic Load Balancing (ELB) - Balances traffic coming in

* SNS - Simple Notification Service, publish messages to subscribers
* SQS -Simple Que Service, send store and receive messages 


## Global Infastracture
Regions are geographically isolated areas and are made up of smaller availability zones/ data centers,  
Regions are picked based on the following:
* Compliance or regulations 
* Proximity 
* Available Services - some services may not be availaable in your region yet
* Pricing - varies by region due to operating costs

### Edge Locations
Amazon Cloudfront is a Content Delivery Network that caches content closer to customers. An Edge Location is a site that is used for CDN.

## Networking
Public and private subnets in a VPC can communicate with each other
* VPC - Virtual Private Cloud, can organize resources into subnets 
    * Internet Gateway - attach an internet gateway to a vpc to connect to the internet
* VPG - Virtual Private Gateway / VPN 
* AWS Direct Connect establishes a direct connection between your data center and a VPC


### Network ACL
* Network Access Control List - subnet level firewall that checks packet coming or leaving a subnet. stateless(always checks)
* Security Group - Statefull and set at instances and can group instances. by default denies all inbound and allows all outbound

### DNS
* Route 53 - Manages Dns records
* Cloudfront - 

## Storage and DB 
Snapshots - incremental backups <br>
Lifecycle policies move data around to different storage classes based on time <br>
* Elastic Block Store (EBS) - behave like physical hard drives. up to 16TiB, stores blocks which is better for example editing video where only some blocks change. Attach to EC2 and are a Zone level resource. Used for storing Amazon RDS databases.
* Amazon Simple Storage (S3) - store data as objects and stores them into buckets (max object size 5tb). Write once read many storage 
    * S3 Standard - Can also store static website hosting in S3
    * S3 Standard Infrequent Access - long term storage but needs quick access, lower storage price and higher retrieval price
    * S3 OneZone IA - Stores data in a single zone, lower storage price
    * S3 Intelligent Tiering - Ideal for data with unknown or changing access patterns
    * S3 Glacier - Long term storage for data archiving, retrieve within hours
    * S3 Glacier Deep Archive - lowest cost storage, retrieve within several hours
* Amazon Elastic File System (EFS) - multiple instances reading and writing simultaneously, linux file system, regional resource and auto scaling.  
* Amazon Relational Database Service - SQL to store and query data, managed service that automates scaling and setup
* Amazon DynamoDB - non relational database using key-value pairs
* Amazon Redshift - Data warehousing services for big data analytics


## Security
Follow best practice of giving least privilages 
* AWS IAM - Identity and Access Management, by default all actions denied. Have to grant privelages as the root user
    * Users - 
    * Groups - Collection of Users and permissions 
    * Policies - allows or denies permissions to AWS  
    * Roles - Access to temporary time and permissions, given to users, apps, etc best for short term
* AWS Organizations - For large business
    * Service Control Policy (SCP) - To centrally control policies, Can do policies in Organizational Units and individual members.
* AWS Artifcat - Security and Compliance reports
* AWS Shield - DDOS protection service
* AWS Key Management Service (KMS) -
* AWS Web Application Firewall (WAF) - 

## Support
* AWS Support plans
    * Basic - 
    * Developer - Best practice guidance, Client Side Diagnostics, and architecture support
    * Business - Use case guidance, All aws trusted advisor checks, 
    * Enterprise - Application architecture guidance, event management, (Technical Account Manager)TAM 
* AWS Well Architected Framework - Evaluates workload agaisnt the 5 pillars
    * Operational Excellence -  The ability to run and monitor systems and improve supporting processes and procedures
    * Security - Delivering business value through trisk assesssments and mitigation
    * Reliability - Recover from interruptions and change resources to meet demand
    * Performance Efficiency - Selecting right resources based on workload requirements and making informed decisions to maintain efficiency
    * Cost Optimization - Reduce cost of ownership, avoid or eliminate unneeded cost.

## Migration 
* AWS Cloud Migration Framework
    * Business 
    * People - HR
    * Governance
    * Platform
    * Security
    * Operations
* 6 Different Staretegies for Migration
    * Rehosting - Lift and Shift 
    * Replatforming - Lift, Tinker, and Shift
    * Refactoring - Driven by a need to add new features and edit code
    * Repurchasing - Software as a service option
    * Retaining - Keeping critical applications at the source environment
    * Retiring - removing applications that are no longer needed
* Snow Family - transports data into aws physically
    * snowcone - 8tb
    * snowball - 42tb to 80tb 
    * snowmobile - 100PB
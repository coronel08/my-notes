# AWS
Savings PLans available for Lambda, Fargate, and EC2
Horizontal Scaling  = adding several smaller instances when workloads increase 
Can work with AWS through AWS Management Console, CLI, or SDK


Server-based services include: Amazon EC2, Amazon RDS, Amazon Redshift and Amazon EMR.
Serverless services include: AWS Lambda, AWS Fargate, Amazon SNS, Amazon SQS and Amazon DynamoDB.



* Elastic Beanstalk - automatically handles the deployment details of capacity provisioning, load balancing, auto-scaling. Can also perform health checks on Amazon EC2 instances. Platform as a Service
* AWS CloudFormation - is a Yaml based tool used to define resources


AWS Well Architected Dramework, best practices for designing in cloud
1. Operational Excellence - run and monitor systems to deliver business value, automate changes and manage daily operations.
2. Security - protect information
3. Reliability - ability to recover from disruptions.
4. Performance efficiency - use computing resources efficiently
5. Cost Optimization service


* Infastructure as a Service - building blocks of cloud
* Platform as a Service - removes the need to manage infastructure like hardware and OS. 
* Software as a Service - completed product that is run and managed 
## Table of contents

* [AWS](#Aws)
* [Services](#services)
* [EC2](#ec2)
    * [Instance Types](#instance-types)
    * [Pricing](#pricing)
    * [Scaling](#scaling)
* [Global Infastructure](#global-infastructure)
* [Networking](#networking) 
* [Storage and DB](#storage-and-db)
* [Security](#security)
* [Support](#support)
* [Migration](#migration)

## Services
* Amazon Athena - Analytics service that makes it easy to query data in Amazon S3 using standard SQL commands.
* AWS CloudHSM - security model that lets you use your own encryption keys
* AWS CodeBuild - continuous integration service allows testing code
* AWS CodeCommit - used for software version control by developers. 
* AWS CodeDeploy - automates code deployment to instances
* AWS Config - continually audit, monitor for compliance, or vulnerabilities in AWS.Helps with compliance auditing, security analysis, change management, and troubleshooting. 
* Amazon Detective - easily investigate security findings.
* AWS Glue - data transformation tool that Extracts, Transforms, and Load service 
* Amazon GuardDuty - threat detection that monitors accounts and workloads
* Amazon Macie - data security and data privacy service that uses machine learning to protect data 
* AWS Professional Services - team of experts that help set up desired business on AWS
* Amazon Quicksight - Business Intelligence tool
* AWS Service Limits or Service Quotas - can use AWS Trusted Advisors Service Limit dashboard to monitor. Can be increased by contacting Amazon. Applied to AWS account level

## EC2
Elastic Cloud Computation
Infrastructure as a Service - computers and data storage provided

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
    * Standard RI - Most significant discount 72%
    * Convertible RI - change attributes as long as its an even exchange discount 54%
* Spot Instance - Ideal for flexible workloads or one that can withstand interruptions. 90% savings
* Dedicated Host - Fully dedicated to one host

* AWS Resource Groups - Use to create custom console for environments and view/manage resources easily.

* AWS Cost & Usage report - contains the most conprehensive set of AWS cost and usage data
* AWS Cost Explorer - visualize and understand and manage AWS cost and usage, forecast up to 12 months ahead.  

### Scaling
* EC2 Auto Scaling - Auto optimizes servers and instances to meet needs, can set min, desired, and max. Cannot span multiple Regions.
* Elastic Load Balancing (ELB) - Balances traffic coming in, not global service. Distributes traffic across multiple Availability Zones within the same AWS Region.

* SNS - Simple Notification Service, publish messages to subscribers
* SQS -Simple Que Service, send store and receive messages 
* Amazon Machine Image (AMI) - provides info to launch an instance from a previous image or template

* CloudEndure Disaster Recovery - minimizes downtime and data loss, continually replicates machines

## Global Infastracture
Regions are geographically isolated areas and are made up of smaller availability zones/ data centers,  
Regions are picked based on the following:
* Compliance or regulations 
* Proximity 
* Available Services - some services may not be availaable in your region yet
* Pricing - varies by region due to operating costs



Edge Locations
Amazon Cloudfront is a Content Delivery Network that caches content closer to customers. An Edge Location is a site that is used for CDN.


## Networking
Public and private subnets in a VPC can communicate with each other
* VPC - Virtual Private Cloud, can organize resources into subnets 
    * Internet Gateway - attach an internet gateway to a vpc to connect to the internet
    * Transit Gateway - simplifies how customers connect all of their VPC's, acts as a hub
* VPG - Virtual Private Gateway / VPN 
    * AWS Client VPN 
    * AWS site-to-site VPN - uses IPSec to establish connection between on premise and AWS
* AWS Direct Connect establishes a direct connection between your data center and a VPC
* AWS Outposts - provides AWS infastracture to on premises facility. 


### Network ACL
* Network Access Control List - subnet level firewall that checks packet coming or leaving a subnet. stateless(always checks)
* Security Group - Statefull and set at instances and can group instances. by default denies all inbound and allows all outbound. Used to control which Ip address can connect

### DNS
* Route 53 - Manages Dns records and offer health checks to monitor health and performance.
* Cloudfront - Can integrate AWS Shield and AWS WAF to protect against network DDOS attacks.

## Storage and DB 
EBS => multiple servers in same availability zone. 
EFS => multiple availability zones
S3 => multiple availability zones


Snapshots - incremental backups <br>
Lifecycle policies move data around to different storage classes based on time <br>
* Elastic Block Store (EBS) - behave like physical hard drives. up to 16TiB, stores blocks which is better for example editing video where only some blocks change. Attach to EC2 and are a Zone level resource. Used for storing Amazon RDS databases. More expensive than S3. Cannot be attached to multiple compute resources at a time.


* Amazon Simple Storage (S3) - store data as objects and stores them into buckets (max object size 5tb). Write once read many storage. Can host a static website or can be used as a media store for Cloudfront. Amazon S3 assigns a URL for each object you upload. Can scale and replicate data automatically across multiple Availability Zones(except One-Zone IA). Cant be attached to compute resources
    * S3 Standard - Can also store static website hosting in S3
    * S3 Standard Infrequent Access - long term storage but needs quick access, lower storage price and higher retrieval price
    * S3 OneZone IA - Stores data in a single zone, lower storage price
    * S3 Intelligent Tiering - Ideal for data with unknown or changing access patterns
    * S3 Glacier - Long term storage for data archiving, retrieve within hours
    * S3 Glacier Deep Archive - lowest cost storage, retrieve within several hours


* Amazon Elastic File System (EFS) - multiple instances reading and writing simultaneously, linux file system, regional resource and auto scaling.  


Databases
* Amazon RDS (Relational Database Service) - SQL to store and query data, managed service that automates scaling and setup
* Amazon DynamoDB - non relational database using key-value pairs
* Amazon Redshift - Fully Managed data warehousing services for big data analytics. Server Based
* Amazon Storage Gateway - helps extend their on-premise storage to AWS
* Amazon Aurora - Mysql and PostgreSQL relational database, an Amazon RDS service
* Amazon Elastic Map Reduce (EMR) - fast and efficient processing of big data using Hadoop framework  

## Security
Security Bulletins - AWS notifies customers about security and privacy events.

Follow best practice of giving least privilages 
* AWS IAM - Identity and Access Management, by default all actions denied. Have to grant privelages as the root user
    * Users - Recommended IAM entity when granting a person long term access permissions.
    * Groups - Collection of Users and permissions 
    * Policies - allows or denies permissions to AWS, attached to users
    * Roles - Access to temporary time and permissions, given to users, apps, etc best for short term. Does not have standard long-term credentials instead temp credentials.
* AWS Organizations - For large business
    * Service Control Policy (SCP) - To centrally control policies, Can do policies in Organizational Units and individual members.
* AWS Artifcat - Security and Compliance reports
* AWS Shield - DDOS protection service
* AWS Key Management Service (KMS) - to create and control encryption keys used to encrypt data such as EBS volumes
* AWS Web Application Firewall (WAF) - used to monitor HTTP and HTTPS requests that are forwarded to Amazon CloudFront or Load Balancer
* AWS Inspector - Automated security assessment service that helps improve the security and compliance


* Cloudwatch - Focuses on the activity of AWS services and resources, reporting on their health and performance. Security repositry with threat analytics and metrics.
* Cloudtrail - Log of all actions and API calls taking place in AWS

* Amazon Cognito - let's customers add user sign in with Facebook, Google, Amazon
* Amazon Cloud Directory - directory service provides web-based directories to organize users, groups, devices, policies
* Amazon Directory Service - provides single sign on to AWS, uses existing Microsoft Actice Directory

## Support
* AWS Support plans
    * Basic - 
    * Developer - 
        * Best practice guidance, 
        * Client Side Diagnostics
        * Architecture/tecgnical support during business hours.
    * Business - response time of 1 hour for production systems
        * Use case guidance, 
        * All aws trusted advisor checks
        * AWS Personal Health dashboard 
        * 24x7 technical support engineers. 
        * AWS Support API
        * Access to Infastructure Event Management(IEM) for a fee, included with Enterrpise
        * Chat access to AWS Support Engineers
    * Enterprise - Response time of 15 mins for production systems
        * Application architecture guidance, event management, 
        * Technical Account Manager (TAM) and Support Concierge Service (AWS Billing and account experts) 
        * AWS support API 
        * Access to Infastructure Event Management(IEM) - provide architectural and scaling guidance

* AWS Well Architected Framework - Evaluates workload agaisnt the 5 pillars
    * Operational Excellence -  The ability to run and monitor systems and improve supporting processes and procedures. Example: Cloudformation to manage servers as code. 
    * Security - Delivering business value through trisk assesssments and mitigation
    * Reliability - Recover from interruptions and change resources to meet demand
    * Performance Efficiency - Selecting right resources based on workload requirements and making informed decisions to maintain efficiency
    * Cost Optimization - Reduce cost of ownership, avoid or eliminate unneeded cost.

## Migration 
* AWS Total Cost Ownership (TCO) - free tool that provides info on possible savings when deploying to AWS. (Cost Explorer only analyzes current cost and ussage)
* AWS Application Discovery Service - helps systems integrators plan application migration projects by identifying on-premise applications.
* AWS Cloud Adoption Framework (CAF) - helps organizations design a road map to cloud adoption

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

* CloudEndure Migration - automated lift and shift for migrating apps.

* AWS Server Migration Service(SMS) - migrates workloads to AWS, supports virtual machine migrations, then saves them as a new Amazon Machine Image(AMI) that can be launched as an EC2

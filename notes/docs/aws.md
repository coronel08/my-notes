# AWS

Savings PLans available for Lambda, Fargate, and EC2

Horizontal Scaling = adding several smaller instances when workloads increase

Can work with AWS through AWS Management Console, CLI, or SDK

## Global Infastracture

Regions are geographically isolated areas and are made up of smaller availability zones/ data centers, Elastic Load Balancing automatically distributes your incoming traffic across multiple targets, such as EC2 instances, containers, and IP addresses, in one or more Availability Zones. It monitors the health of its registered targets, and routes traffic only to the healthy targets. Elastic Load Balancing scales your load balancer as your incoming traffic changes over time. It can automatically scale to the vast majority of workloads.

Regions are picked based on the following:

-   Compliance or regulations
-   Proximity
-   Available Services - some services may not be availaable in your region yet
-   Pricing - varies by region due to operating costs

Edge Locations
Amazon Cloudfront is a Content Delivery Network that caches content closer to customers. An Edge Location is a site that is used for CDN.

## Solution Architect

When providing solutions can split requirements into:

-   Functional Requirements : Define what an application does
-   Non Functional Requirements : Define how an application operates

**AWS Well Architected Framework, best practices for designing in cloud**

1. Operational Excellence - run and monitor systems to deliver business value, automate changes and manage daily operations. Example Cloudformation to manage servers as code
2. Security - protect information, Delivering business value through risk assesssments and mitigation
    - Security Pillar of AWS Well Architected Framework can be broken down to:
        1. IAM management - IAM, Cognito or Directory Service
        2. Detective Controls - Security Hub, GuardDuty, Inspector, Detective
            - Security Hub = A single place to aggregate and organize security findings for multiple AWS services. checks compliance with security standards and best practices. Suppports integration with CloudWatch Events allowing for custom actions when a finding is received. Region specific
        3. Infastructure Protection - WAF for traffic filtering and AWS Shield for DDOS protection.
        4. Data Protection - protect data at rest and transit using AWS KMS, AWS Certificate Manager, AWS Secrets Manager, AWS CloudHSM
        5. Incident Response - plan to respond to security incident, AWS Config monitoring tool
3. Reliability - ability to recover from disruptions and change resources to meet demands
4. Performance Efficiency - use computing resources efficiently
5. Cost Optimization service - Reduce cost of ownership, avoid or eliminate unneeded cost

<br>

-   Cloud Value Framework, problems may occur with Migration related costs, such as Cloud Readiness and Entrenched It Organization be sure to look into:

    1. Cost Savings : Total Cost of Ownership (TCO), compare cost of on premise vs aws and performance increases. Consumption based model allows to pay only for what you use.
        - Formula for Cost savings / sunk costs + migration costs = ROI. Make sure to include operational costs, depreciation, and recovery value for Hardware
    2. Staff Productivity : Cloud opens up productivity with servers, networks, storage, apps, facilities, and security
    3. Operational Resilience
    4. Business Agility

-   Cloud Economics is made up of :
    -   Business Value(Total Cost of Ownership TCO) :
    -   Cloud Financial Management : use measurements and accountability to track spending. Optimize cost by identifying waste. Plan and Forecast future costs and spending. Cloud Financial Operations means investing in people process and tools.

## Amazon Partner Network

-   Consulting Partners - firms that help customers design, architect, build, migrate and manage their workloads and applications on AWS. Can include MSP
    -   Can achieve levels Registered => Select => Advanced => Premier
-   Technology Partners - provide hardware, connectivity and software solutions that are hosted on or integrated with the AWS cloud. Can include Independent Software Vendors
    -   Can Achieve 3 tiers based on engagement Registered => Select => Advanced
-   Partner Central - provides partners with tools and content they need to grow their business on AWS

Shared Responsiblity Model:

**AWS is Responsible for**: Compute, Storage, Database, Networking, Edge Locations, Availability Zones and Regions.

**Customer is Responsible for**: App, Access Management, OS, Network and Firewall, Client and Server side encryption, and Network Traffic Protection.

[Getting Started](https://aws.amazon.com/getting-started/?nc1=h_ls)

Server-based services include: Amazon EC2, Amazon RDS, Amazon Redshift and Amazon EMR.

Serverless services include: AWS Lambda, AWS Fargate, Amazon SNS, Amazon SQS and Amazon DynamoDB.

-   Global Services include:

    -   IAM(Identity and Access Management)
    -   Route 53 DNS service
    -   Cloudfront CDN
    -   WAF Web application firewall

-   Infastructure as a Service - building blocks of cloud
-   Platform as a Service - removes the need to manage infastructure like hardware and OS.
-   Software as a Service - completed product that is run and managed

## Table of contents

-   [AWS](#aws)
    -   [Global Infastructure](#global-infastructure)
    -   [Solution Architect](#solution-architect)
-   [Services](#services)
    -   [Serverless Computing](#serverless-computing)
-   [EC2](#ec2)
    -   [Auto Scaling/ Load Balancing](#auto-scaling-and-load-balancing)
-   [Elastic BeanStalk](#elastic-beanstalk)
-   [SNS + SQS + Kinesis](#SNS-SQS-and-Kinesis)
-   [Lambda](#lambda)
-   [Networking](#networking)
    -   [Network ACL](#network-acl)
    -   [DNS](#dns)
-   [Storage and DB](#storage-and-db)
    -   [EBS](#ebs)
    -   [S3](#s3)
    -   [EFS](#efs)
    -   [Databases](#databases)
        -   [DynamoDB](#DynamoDB)
-   [Security](#security)
    -   [IAM](#iam)
    -   [Cognito](#amazon-cognito)
    -   [Security Token Service](#security-token-service)
    -   [Monitoring](#monitoring)
-   [Support](#support)
-   [Migration](#migration)
-   [API gateway](#api-gateway)
-   [Code as Config](#code-as-config)
    -   [Serverless Application Model](#serverless-application-model)
    -   [Cloud Development Kit](#cloud-development-kit)
    -   [AWS Step Function](#aws-step-functions)
        -   [Policy Example](#policy-example)

## Services

Most services are region scoped

-   AWS Amplify - fully managed service for hosting static web apps. CI/CD
-   AWS AppSync - managed service that uses GraphQL. Can combine data from more than one source. Also able to get real time data or access local data on mobile apps from offline as well.
    -   Security
        -   API_KEY:
        -   AWS IAM:
        -   OPENID_CONNECT:
        -   AMAZON_COGNITO_USER_POOLS:
-   AWS Budgets - Lets customers set custom budgets and receive alerts on costs, requires approximately 5 weeks of usage data to generate budget forecasts.
-   AWS Certificate Manager (ACM) - provision, manage and deploy certificates(public or private) for https
-   AWS CloudHSM - security model that lets you use your own encryption keys
-   AWS CodePipeline - Full CI build for AWS, Codestar is a wrapper that groups everything into one
    -   AWS CodeCommit - used for software version control by developers. github clone
        -   Use AWS STS with AssumeRole API to share cross accounts. SSH Keys, Git credentials, AWS access keys, or HTTPS credentials in user profiles. Doesnt support HTTP public access
    -   AWS CodeBuild - continuous integration service allows testing code, jenkins clone
        -   compiles source code, runs unit tests, and produces artifacts. Can build docker images
        -   Buidspec.yml(placed at root folder) for instructions
        -   by default can't access resources in VPC, CodeBuild is launched outside of VPC
        -   Timeouts - default value is 8 hours, can change it between 5 min - 8 hours.
        -   Deployment - allows more control over deployment compared to Elastic Beanstalk(EBS)
            -   in-place deployment -
            -   blue/green deployment - provision a new set of instances, traffic is pointed to the new instances can revert to old instances if errors.
    -   AWS CodeDeploy - automates code deployment to instances.
        -   Order is Stop Application => Before Install => After Install => Start Application
        -   Deployment Groups - contains settings and configurations used during deployment such as rollbacks, triggers, and alarms
        -   Appspec.yml - YAML or JSON file for specifying deployment hooks. Placed in the root directory
            -   ECS - defines `TaskDefinition`, `LoadBalancerInfo`, subnets, security groups,
            -   Lambda - defines which lambda version to deploy, which lambda version to use as validation tests
            -   EC2 - used to determine what it should install, what lifecycle event hooks to run in response to deployment lifecycle events.
        -   Hooks - correspond to lifecycle events such as ApplicationStart, ApplicationStop, ValidateService etc.
        -   Agent - a software package that makes it possible to be used in CodeDeploy
            ![](https://assets-pt.media.datacumulus.com/aws-dva-pt/assets/pt2-q56-i1.jpg)
-   AWS Control Tower - setup baseline environment for scalable and secure workloads
-   Amazon Detective - easily investigate security findings. Collects data from AWS resources and uses machine learning on data
-   AWS Glue - data transformation tool that Extracts, Transforms, and Load service
-   Amazon GuardDuty - threat detection that continously monitors accounts and workloads for mailicious activity and unauthorized behavior, gets data from CloudTrail events, VPC flow logs, DNS logs.
-   Amazon Elastisearch - Operational Analytics
-   Amazon Macie - data security and data privacy service that uses machine learning to automatically protect data. Available to protect data on S3. Common use case is discovering relevant data fields collected by Macie and turning those fields into custom alerts.
-   AWS Professional Services - team of experts that help set up desired business on AWS
-   Amazon Quicksight - Business Intelligence tool, Dashboards and Visualizations
-   AWS Service Limits or Service Quotas - can use AWS Trusted Advisors Service Limit dashboard to monitor. Can be increased by contacting Amazon. Applied to AWS account level
-   AWS Trusted Advisors - tool that provides live/real time guidance (phone or chat) to help provision resources following AWS best practices. Need to use atleast a Business Account.
-   Server Name Indication(SNI) - used to route multiple SSL certificates

### Serverless Computing

![](https://raw.githubusercontent.com/coronel08/my-notes/main/photos/serverless.png)

-   AWS lambda - Cloud function that only gets charged when triggered
-   ECS (Elastic Container Service) -
    -   Task Definition - json metadata to tell ECS how to run a docker container.
    -   Task Role - allow each tasks to have a specific role, use different roles for different services.
        -   Task Placement - When service is scaled in ECS the task placement figures out what container to put it in
            -   Binpack - places task on instance with least available cpu/memory. cost savings
            -   Random
            -   Spread - Evenly spread task
    -   Dynamic Port Mapping - allows multiple tasks from a single service on the same container instance. ECS manages registering and deregistering containers using instance ID and port for each container.
    -   If you terminate an instance while in STOPPED state that may lead to synchronization issues, isnt automatically removed from cluster.
    -   ECR (Elastic Container Registry) - store images, make sure IAM permissions are set "ecr:GetAuthorizationToken" to authenticate to a registry.
    -   Start Docker container
        -   $(aws ecr get-login --no-include-email) - retrieves token valid for 12 hours
        -   docker pull 1234567890.dkr.ecr.eu-west-1.amazonaws.com/demo:latest
-   EFS (Elastic File Storage)
-   EKS (Elastic Kubernetes Service) -
-   Fargate - Works with both ECS and EKS, its a container engine
-   DynamoDB & Aurora
-   API Gateway
-   SNS, SQS, AWS App Sync, Amazon Event Bridge
-   AWS Step Functions
-   Amazon Kinesis, Amazon Athena

---

## EC2

Elastic Cloud Computation - ec2 storage is called "Instance Store" gets terminated with instance

Infrastructure as a Service - computers and data storage provided

EC2 Metadata - Only accesible from inside AWS. URL: http://169.254.169.254/latest/meta-data

-   Instance Types:
    -   General Purpose - Balanced
    -   Compute Optimized - for processing heavy loads
    -   Memory Optimized - for something like a high performance database
    -   Accelerated Computing - graphics or streaming
    -   Storage Optimized - Data warehousing or high read and write performance
-   Pricing:

    -   On Demand - always available
    -   EC2 Savings Plan - Ideal for workloads that require consistent compute usage 1 year or 3 year terms. 72% savings
    -   Reserved Instance - Billing discount applied to On Demand instance with 1 year or 3 year renewal
        -   Standard RI - Most significant discount 72%
        -   Convertible RI - change attributes as long as its an even exchange discount 54%
        -   Locations
            -   Regional Reserved Instances - Does not provide capacity reservation.
            -   Zonal Reserved Instances - provides capacity in the specified availability zone. Abilitty to create and manage Capacity Reservations independently from billing discounts offered by Savings Plans or regional Reserved Instances
    -   Spot Instance - Ideal for flexible workloads or one that can withstand interruptions. 90% savings
        -   Instances can be Stopped, Hibernated, Terminated BUT NOT REBOOTED.
    -   On-Demand Capacity Reservations -reserve compute capacity in an Availability Zone for any duration. Managed independently from Savings Plans or Regional Reserved Instances.
    -   Dedicated Instance - Instance running on dedicated hardware but may share hardware with other instances in same account.
    -   Dedicated Host - Fully dedicated to one host
        ![](https://assets-pt.media.datacumulus.com/aws-dva-pt/assets/pt1-q21-i1.jpg)

    <br><br>

-   EC2 USer Data - can pass shell scripts and cloud-init directives. Used to run common configuration tasks. Run only during boot cycle when first launched but can be configured to run on restart.

    -   scripts - executed with root privileges

-   AWS Resource Groups - Use to create custom console for environments and view/manage resources easily.

-   AWS Cost & Usage report - contains the most conprehensive set of AWS cost and usage data
-   AWS Cost Explorer - visualize and understand and manage AWS cost and usage, forecast up to 12 months ahead.

-   Amazon Machine Image (AMI) - provides info to launch an instance from a previous image or template

-   CloudEndure Disaster Recovery - minimizes downtime and data loss, continually replicates machines

### Auto Scaling and Load Balancing

-   Scaling:

    -   EC2 Auto Scaling - Auto optimizes servers and instances to meet needs, can set min, desired, and max. Cannot span multiple Regions but can span availability zones in 1 region.
        -   By default health check configurations of auto scaling groups are set to EC2, to automate the replacement of unhealthy instances change from EC2 to ELB
        -   Cannot add a volume to an existing instance if the existing volume is approaching capacity. A volume is attached to a new instance when it is added
        -   Auto Scaling groups in a vpc launches the EC2 instances in subnets
        -   Can seperate public vs private traffic. An internet facing load balancer will have a public IP address and will route requests to targets using private IP address. Therefore EC2 targets dont need a public IP.
    -   Elastic Load Balancing (ELB) - Balances traffic coming in, not global service. Distributes traffic across multiple Availability Zones within the same AWS Region. Communicates with EC2 instances using private IP addresses.
        -   Monitors health of Instances and only routes traffic to healthy targets
        -   Access Logs - disabled by default, logs info such as time the request was received, clients IP, latencies, request paths, and server responses. Stored in S3 buckets and automatically encrypted using SSE-S3
        -   3 types of balancers (Stickiness in load balancing uses cookies to keep client connecting to the same server)
            -   Classic Load Balancer - HTTP, HTTPS, TCP. Used when needed to support older architecture
                -   Provides a static DNS name we can use in our application.
                -   Cross-Zone Load Balancing - enabled by default thru console, CLI/API disables it by default. No Charges for inter AZ data.
                -   Support for sticky sessions using application generated cookies
            -   Application Load Balancer (ALB) - HTTP, HTTPS, Websocket. Used to route web traffic only, IP's are not static. Works on the 7th layer/Application.
                -   Can route based on URL, hostname, Query String and fits well with docker.
                -   Cross-Zone Load Balancing - on by default with no charges for inter AZ data
                -   Target groups can be Ec2 instances, Ip Addresses, or Lambda Functions
                -   Provides a static DNS name we can use in our application.
                -   need to use the "X-Forwarded-For" header to get originating IP address of traffic.
                -   SSL Passthrough - data passes through fully encrypted
                -   SSL Termination / Offloading - load balancer decrypts traffic
                -   Request Tracing - track http requests, load balancer adds a header with a trace identifier to each request it receives.
                -   Access Logs - captures detailed information about requests sent to your load balancer, disabled by default. Can analyze traffic patterns and troubleshoot issues because it tracks IP, latency, request path, and server response.
                -   Have to make sure that load balancer is able to communicate with targets on listener and health check port. Must also make sure Load Balancer security groups allow traffic on the new port in both directions.
                    -   ![](https://assets-pt.media.datacumulus.com/aws-dva-pt/assets/pt1-q28-i1.jpg)
            -   Network Load Balancer - TCP, UDP, TLS(new SSL). Low Latency and high performance, IP's are static. Works on layer4/Transport of OSI model, the end to end connections using TCP or UDP
                -   exposes a public static IP. Doesn't support "X-Forwarded-For" header
                -   Availablity Zone - creates a load balancer in each Availablity Zone,
                -   Cross-Zone Load Balancing - Disabled by default, pay for inter AZ data if enabled (Data between availability zones)
                -   Supports targets by IP address, including targets outside VPC
                    ![](https://media.datacumulus.com/aws-dva-pt/assets/pt4-q50-i1.jpg)
        -   Scaling Policy Types (after scaling there is a default cooldown of 300 seconds before another scaling option can happen.)
            -   Target Tracking scaling - Increase or decrease based on target value such as 60% cpu usage
            -   Step Scaling - Increase or decrease based on scaling adjustments that vary by alarm breach. Cloudwatch alarms trigger the scaling process.
            -   Simple Scaling - Increase or decrease based on a single scaling adjustment
            -   Scheduled Actions - Schedule adjustments based on patterns and time

---

## Elastic BeanStalk

-   Elastic Beanstalk - automatically handles the deployment details of capacity provisioning, load balancing, auto-scaling. Can also perform health checks on Amazon EC2 instances. Platform as a Service
    -   Deployment Options
        -   All at Once - fastest but has downtime
        -   Rolling - updates a bucket at a time then moves to next. Rollback would be manually done
        -   Rolling with additional batches - like rolling but spins up new instances to move the batch. rollback would be manually done.
        -   Immutable - spins new instances in ASG, deploys to these and then swaps instances
        -   Traffic Splitting / Canary Testing - Only small % of traffic sent to new version to test for failures
        -   Blue Green - manual swap of URL's thru Route 53, better for minimum downtime and ability to rollback quickly
    -   If Deployment fails when upgrading version, they get replaced with most recent successful deployment.
    -   Beanstalk Extensions - zip file with .ebextensions/ directory and extensions ending in .config like `.ebextensions/<mysettings>.config`. Resources defined in ebextensions will get deleted on termination.
        -   Yaml or JSON formatted files
        -   To decouple application like a persistent Database or configure your environment, define externally and reference through environment variables
            <br>
            `option_settings: aws:elasticbeanstalk:environment: LoadBalancerType: network`
            ![](https://media.datacumulus.com/aws-dva-pt/assets/pt1-q10-i1.jpg)

[EBS Samples](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/tutorials.html)

---

## SNS SQS and Kinesis

-   SNS - Simple Notification Service, publish messages to subscribers

    -   Topic Publish - create a topic and a subscription
        -   FIFO - one message delivery thru SQS. First in/First Out
        -   Standard - Best effort to keep message order, at least once delivery. publish to SQS, Lambda, HTTP, SMS, Email
    -   Direct Publish - for mobile create a platform and endpoint

-   SQS -Simple Que Service, send store and receive messages. used to decouple applications. Default retention 4 days, max 14 days. up to 10 messages at a time. Group data by using Group ID. Scales automatically. Max size is 256kb.

    -   standard queue vs FIFO queue - Can't change queue type after you create it. At least once delivery. First In => First Out 300 msg/s without batching, 3000 msg/s with.
    -   Message Visibility Timeout - message visibility timeout is 30 seconds by default, max 12 hours, if not processed within the timeout it will be processed twice. Prevents other consumers from receiving and processing the same message.
    -   Dead Letter Queue(DLQ) - set a threshold of how many times the message can go back into the queue. After the threshold the message goes into the DLQ(Dead Letter Queue)
    -   Delay Queue - default is 0 seconds but can be up to 15 minutes
    -   Long Polling - Pull requests to SQS Queue, decreases API calls and increases efficiency. "WaitTimeSeconds" Between 1 - 20 seconds.
    -   Security - can encrypt messages in queues using AWS KMS(Key Management Service)
    -   Delete - When you delete a que all the messages are no longer available. Can take up to 60 seconds.

-   Kinesis - collect, process, and analyze streaming data such as Application logs, Metrics, and telemetry data. Meant for real time big data. Group data into shards using a partition key.
    -   Kinesis Data Streams - scaled with shards. Retention between 1 day(default) to 365. Manage scaling thru shard splitting or shard merging.
        -   producers - gets info from producers/source, puts it into shards. Provisioned Throughput Exceeded when shard is over used, need to use highly destributed partition key, retries with exponential backoff, or increase shards.
        -   consumers - gets data streams and processes it in kinesis data firehose, kinesis data analytics, apps, or lambda
            -   shared (classic) Fan out consumer pull - max 5 get records api calls/sec
            -   enhanced fan out consumer push - higher cost and lower latency pushes data to shards instead of pulling.
    -   Kinsesis Data Firehouse - upload streaming data into resources, automatic scaling. no data storage. convert data along the way. easiest way to load streaming data in data stores and analytic tools.
        -   writes data to S3, Redshift, ElasticSearch, or custom API or 3rd party like MongoDB
    -   Kinesis Data Analytics - SQL application, build sql queries
    -   Kinesis Video Streams -

---

## Lambda

-   Pay per request and compute time, increasing RAM will also improve CPU and Network.
    -   from 128mb - 10gb (64mb increments), at 1792mb you get more than one CPU and need to use multi-threading
    -   Execution time ranging from 1 sec - 15 minutes
    -   /tmp directory max size is 512mb, disk space for lambda that is discarded when function stops running. Environment variables size max is 4kb.
    -   Dependencies - code and dependencies get zipped together and uploaded to Lambda if less than 50mb, else S3 first.
    -   Versioning - is code + configuration that cant be changed. Versions get their own ARN(Amazon Resource Name) and cant be Changed
    -   Aliases - point to different lambda function versions like "dev", "test". Aliases can't reference other aliases. Can be wieghted to distribute and test features between versions
    -   Lambda and CodeDeploy - can automate traffic shift for lambda aliases either rolling or all at once.
        ![](https://media.datacumulus.com/aws-dva-pt/assets/pt1-q13-i3.jpg)
-   Application Load Balancer multi-header values - the load balancer supports values thru query strings in the http address that get turned into json arrays. Application Load Balancers are integrated with lambda with a target group.
-   lambda @ edge - for deployment alongside CDN using CloudFront, can use lambda to change requests and responses from CloudFront
-   Lambda layers - zip file archive that contains additional code or data
-   Invoking functions
    -   Synchronous Invocation - result is returned right away
        -   Services:
    -   Asynchronous Invocation - events are placed in an Event Queue
        -   Services: S3, SNS, CloudWatch Events, CodeCommit/CodePipeline
        -   Lambda Destinations - can send results to destinations like SQS for succesful and failed events. Recommend to use destinations over DLQ
    -   Event Source Mapping Invocation - reads from an event source that invokes a lambda function
        -   Streamed Services: DynamoDB, Kinesis. by default if function returns error the entire batch is reprocessed until succeed or expire
        -   Polled Services: SQS, MQ.
-   Logging and Monitoring
    -   Cloudwatch Events - either cronjob or codepipeline into Cloudwatch Events/EventBridge. Lambda metrics are displayed in Cloudwatch Metrics. Can't be used to debug and trace data across accounts.
    -   X-Ray - enable in lambda configuration and use SDK in code.
        -   Environment variables
            -   \_X_AMZN_TRACE_ID: contains the tracing header
            -   AWS_XRAY_CONTEXT_MISSING: by default, Log_Error
            -   AWS_XRAY_DAEMON_ADDRESS: the x ray daemon IP port
-   Lambda Container Images - Can package lambda function code and dependencies as a container image using Docker. Image sizes up to 10GB in size.
    -   Container image must use Lambda Runtime API and Lambda functions must be created from the same account as the ECR.
    -   /tmp directory - temp storage with 512mb of storage
-   Networking
    -   By default the Lambda function is launched in its own VPC and can't access resources or internet unless defined,
    -   ENI(Elastic Network Interface) allows it to interact with VPC
    -   Deploying lambda function in a private subnet with NAT Gateway/Instance gives it internet access. Can also use VPC endpoints to privately access AWS Services without a NAT
        ![](https://media.datacumulus.com/aws-dva-pt/assets/pt3-q39-i1.jpg)
-   Scaling - Concurrency is the number of requests that a Lambda function is serving at any given time. If a lambda function is invoked while a request is still being processed nother instance is allocated and functions concurrency is increased. Can cause a portion of requests that are served by new instances to have a higher latency.
    -   up to 1000 concurrent executions, can be throttled with reserved concurrency
    -   Provisioned Concurrency - ensures all requests are served by initialized instances with low latency, used before an increase in invocations. Can use Application Auto Scaling to increase on schedule or based on utilization(use Application Auto Scaling API to register a target to create a scaling policy).
    -   Reserved Concurrency - When a function has reserved concurrency no other function can use that concurrency. Limits the maximum concurrency for the function (can't configure on a schedule)

---

## Networking

Public and private subnets in a VPC can communicate with each other. A subnet can only be associated with one route table at a time.

-   VPC - Virtual Private Cloud is a regional resource, can organize resources into subnets which are availability zone resources
    -   Internet Gateway - attach an internet gateway to a vpc to connect to the internet. Public subnets have a route to the internet gateway
    -   NAT Gateway - AWS managed allow your instances in private subnets to access the internet while remaining private
    -   Transit Gateway - simplifies how customers connect all of their VPC's, acts as a hub
    -   VPC Endpoints, only used within your VPC. Just to access AWS services privately within your VPC
        -   VPC Endpoints Gateway - only for S3 and DynamoDB allow you to connect to AWS using a private network instead of wwww
        -   VPC Endpoint Interface(ENI) - the rest of the services
    -   VPC Peering - connects two VPC privately with AWS network, must be established in each VPC
    -   VPC Flow Logs - captures information about IP traffic to VPC, Subnet, Elastic Network Interface(ENI). Sent to S3 or Cloudwatch logs for storage. Can be used on VPC, subnet, or Network Interface to review IP traffic going to and from.
-   VPG - Virtual Private Gateway / VPN
    -   AWS Client VPN
    -   AWS site-to-site VPN - uses IPSec to establish connection between on premise and AWS. Over internet
    -   AWS Direct Connect establishes a direct connection between your data center and a VPC. It is a private connection and doesn't use internet.
    -   AWS Outposts - provides AWS infastracture to on premises facility.

![](https://raw.githubusercontent.com/coronel08/my-notes/main/photos/vpc.png)

### Network ACL

-   Network Access Control List (NACL) - subnet level firewall that checks packet coming or leaving a subnet. stateless(always checks)
    -   Access Control List (ACL) - works with S3, WAF, VPC's
-   Security Group - Statefull and set at instances and can group instances. by default denies all inbound and allows all outbound. Used to control which Ip address can connect. Virtual Firewall at the instance level

[NACL vs Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html)

### DNS

![](https://assets-pt.media.datacumulus.com/aws-dva-pt/assets/pt1-q34-i1.jpg)

-   Route 53 - Manages Dns records and offer health checks to monitor health and performance.
    -   Most common record routings are:
        -   A: hostname to ipv4 example.com -> 12.3.1.3
        -   AAAA: hostname to ipv6
        -   Cname: hostname to hostname test.example.com -> (only for non root domain). Can be used to map one domain name to another
        -   Alias: hostname to AWS resource, free and works for root domain. Can point to somthing like S3
    -   Time to Live
        -   High TTL(24hrs) has less traffic and possibly outdated records
        -   Low TTL(60hrs) more traffic on DNS and records are outdated for less time.
    -   Routing Policy
        -   simple -
        -   weighted - distributed based on percentage loads
        -   latency - redirect to server with least latency
        -   failover - health check mandatory
        -   geolocation - routing based on user location, needs a default policy in case no match.
        -   geoproximity - if you want to shift traffic from one region to another by increasing the bias
        -   multi-value - route traffic to multiple resources and associate health checks with records. not a substitute for Load Balancing but helps.
    -   Health Checks - checks status of resources, can integrate with CloudWatch
-   Cloudfront - Can integrate AWS Shield and AWS WAF to protect against network DDOS attacks.
    -   Can use infront of an Application Load Balancer
    -   Cloudfront Key Pairs - created by root user, used to create signed URLs or signed cookies.
        ![](https://media.datacumulus.com/aws-dva-pt/assets/pt1-q4-i2.jpg)

---

## Storage and DB

EBS => multiple servers in same availability zone.

EFS => multiple availability zones

S3 => multiple availability zones

Snapshots - incremental backups <br>

Lifecycle policies move data around to different storage classes based on time <br>

### EBS

-   Elastic Block Store (EBS) - behave like physical hard drives. up to 16TiB, stores blocks which is better for example editing video where only some blocks change. Attach to EC2 and are a Zone level resource. Used for storing Amazon RDS databases. More expensive than S3.
    -   Cannot be attached to multiple compute resources at a time. Free tier offers 30gb per month
    -   Types
        -   GP2/GP3: General Purpose SSD. 1tb - 16tb
            -   Burst up to 3,000 IOPS and a max of 16,000 IOPS achieved at 5.3Tb
        -   IO1/IO2: High performance SSD for low latency and high throughput. Need more than 16,000 IOPS. 4gb - 16tb
            -   Can be attached to multiple EC2 instances in the same AZ
            -   Maximum ratio of provisioned IOPS to requested Volume Size(in Gb) is 50:1.
                -   Example: for a 200Gb volume, max IOPS possible is 200 \* 50 = 10,000 IOPS
        -   ST1: Low Cost HDD designed for frequently accessed. Data Warehouse. Can't be a boot volume. 125mb - 16tb
        -   SC1: Low cost HDD less frequently accessed workloads
    -   Security - supports both in flight encryption and at rest using KMS
    -   Option to delete on termination
    -   Migration - to migrate you need to take a snapshot and restore it to another AZ

### S3

Objects = files and buckets = directories

-   Amazon Athena - Analytics service that makes it easy to query data in Amazon S3 using standard SQL commands.

-   Amazon Simple Storage (S3) - store data as objects and stores them into buckets (max object size 5tb). Write once read many storage. Can host a static website or can be used as a media store for Cloudfront. Amazon S3 assigns a URL for each object you upload. Can scale and replicate data automatically across multiple Availability Zones(except One-Zone IA). Cant be attached to compute resources

    -   Types
        -   S3 Standard - Can also store static website hosting in S3
        -   S3 Standard Infrequent Access - long term storage but needs quick access, lower storage price and higher retrieval price
        -   S3 OneZone IA - Stores data in a single zone, lower storage price
        -   S3 Intelligent Tiering - Ideal for data with unknown or changing access patterns
        -   S3 Glacier - Long term storage for data archiving, minimum storage duration 90 days, retrieve within hours
            -   Expedited Retrieve - 1-5 mins
            -   Standard - 3-5 hours
            -   Bulk - 5-12 hours
        -   S3 Glacier Deep Archive - lowest cost storage, minimum storage duration 180 days, retrieve within several hours
            -   Standard - 12 hours
            -   Bulk - 48 hours
    -   S3 Encryption
        -   SSE-S3 - server side encrypts S3 objects using keys managed by AWS
            -   Must set header "x-amz-server-side-encryption":"AES256"
        -   SSE-KMS - Key Management Service, server side encryption. Stores the Customer Master Key(CMK) and receives data from the clients which it encrypts and sends back.
            -   Must set header "x-amz-server-side-encryption":"aws:kms"
            -   Leverages GenerateDataKey & Decrypt KMS API calls
            -   Count against KMS limits
        -   SSE-C - Manage your own encryption, server side encryption
            -   Https must be used
            -   Encryption key must be provided in HTTP headers
        -   Client Side Encryption - Client handles encrypt/decrypt and manages keys
            ![](https://media.datacumulus.com/aws-dva-pt/assets/pt5-q55-i1.jpg)
    -   S3 Security, (can connect to s3 using VPC Endpoints and logged in AWS Cloudtrail). Cloudtrail tracks bucket level actions by default, need to enable S3 data events to track object level actions.
        -   User Based - IAM Policies sets what Users are allowed to do what API calls
        -   Resource Based
            -   Bucket wide rules from the S3 console
            -   Object Access Control List (ACL) - finer grain control
            -   Bucket Access Control List (ACL) - less common
    -   S3 Replication( buckets can be in different accounts)
        -   CRR(Cross Region Replication) - compliance reasons, lower latency, across accounts
        -   SRR(Same Region Replication) - log aggregation, live replication between production and test accounts
    -   S3 Lifecycle Rules can be created for path prefix or certain object tags
        -   transition actions - when objects are moved to another storage class
        -   expiration actions - objects are deleted after some time
    -   S3 Performance
        -   Multi Part Upload - auto applied for files 5gb or larger. speeds up transfers by splitting up file
        -   S3 Transfer Acceleration - Increase transfer speed by using AWS Edge locations
        -   S3 Byte-Range - Can be used to speed up downloads by running parallel, can also be used to retrieve partial data
        -   S3 Select and Glacier Select - use SQL statements to filter data

-   [S3 REST API](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RESTAuthentication.html)

### EFS

-   Amazon Elastic File System (EFS) - multiple instances reading and writing simultaneously, linux file system (not compatible with windows),
    -   Regional resource and auto scaling. More expensive than EBS. use Security groups to control access.
    -   Bursting Vs Provisioned: Bursting throughput grows with filesystem but with provisioned throughput is set to a high throughput regardless of file size
    -   Lifecycle Management: move file after N days into either standard or EFS-IA(Infrequent Access)
    -   Security - Encryption at rest using KMS

### Databases

-   Amazon RDS (Relational Database Service) - SQL to store and query data, managed service that automates scaling, backups, and setup. Stored on EBS. Can host MySQL, Oracle, Microsoft SQL, MariaDB, Postgres.
    -   Read Replicas - up to 5 Read Replicas, ASYNC so reads are eventually caught up. Cant write to replica. IF AWS in same region you do not pay for data transfers
    -   RDS Multi AZ(Disaster Recovery) failover in case of loss
    -   Encryption - encrypt with AWS KMS. If master is not encrypted the read replicas can't be encrypted. SSL Certificate to encrypt data in flight,needs to be turned on.
    -   Security - uses security groups to control which IP can communicate. Can also use Policies, username and password or IAM-token authentication(only in Mysql and Postgresql and only last 15 mins)
-   Amazon Aurora - Mysql and PostgreSQL relational database, an Amazon RDS service. 5x performance. Offers high availability, read scaling, and auto scaling
    -   Can have up to 15 read replicas and a Master
    -   Has writer endpoint for master and reader endpoint for load balancing replicas
-   Amazon ElastiCache - managed Redis or Memcached service. In memory DB that makes app stateless.
    -   REDIS - has Read Replicas and data durability, backup and restore features.
    -   MEMCACHED - Multi-node for sharding, no backup and restore or replication. For data that can be lost.
    -   Cache Strategies
        -   Lazy-Loading - Only requested data is cached. If data not in cache it has to read cache, read db, and then write to cache resulting in higher read latency. Data can also be stale as it isnt updated right away.
        -   Write Through - Data in cache is never stale but gets a write penalty instaed of read penalty. Data is written to cache then written to db
    -   Replication Cluster
        -   No cluster - One primary node up to 5 replicas. 1 write and several reader nodes. One shard all nodes have all the data.
        -   Cluster Mode - data is partitioned across shards
-   Amazon Redshift - Fully Managed data warehousing services for big data analytics. Server Based
-   Amazon Storage Gateway - helps extend their on-premise storage to AWS
-   Amazon Elastic Map Reduce (EMR) - fast and efficient processing of big data using Hadoop framework, Apache Spark, or Apache Hive
-   DocumentDB - managed MongoDB
-   Neptune - graph database

#### DynamoDB

-   Amazon DynamoDB - non relational database using key-value pairs. Replication across 3 AZ.
    -   Maximum size of an item is 400kb, can store large objects in S3 and send metadata to DynamoDB
    -   Primary Keys
        -   Partition Key only (hash) - must be unique for each item ex: user id
        -   Partition key + sort key - data is grouped by partition key, sort key is range key ex: user id = partition key and game id = sort key
    -   Indexes
        -   Local Secondary Index (LSI) - must be defined at creation, alternate range key for table that is local to hash key. up to 5 indexes per table
        -   Global Secondary Index (GSI) - speed up queries on non-key attributes, can be modified unlike LSI. If writes are throttled on GSI then main table will be throttled.
    -   Throughput, can be increased temporarily using burst credit and spread throughout partitions
        -   read capacity units - throughput for reads.
            -   Eventually Consistent Reads - By default. 2 reads per second for up to 4kb in size
            -   Strongly Consistent Reads - 1 read per second for up to 4kb in size
        -   write capacity units - 1 write capacity represents 1 write per second of 1kb in size
        -   throttling - if we exceeed use we get ProvisionedThroughputExceededException, can be fixed with exponential back off or using DynamoDB Accelerator(DAX)
    -   API
        -   write
            -   PutItem
            -   UpdateItem
            -   Conditional Writes - accepts a write only if conditions are met
        -   delete
            -   DeleteItem - can also be a conditional delete
            -   DeleteTable
        -   read
            -   GetItem - read based on primary key
        -   batching - reduces # of API calls. It is possible that only some of the actions in the batch succeed while others do not.
            -   BatchWriteItem - up to 25 in one call, up to 16mb of data written, up to 400kb of data per item. If batched items fail we need to use exponential back-off algorithm
            -   BatchGetItem - up to 100 items, up to 16mb of data
        -   Transactions - CRUD operations for multiple rows in different tables. if one update fails they all fail
            -   capacity - consumes 2x WCU RCU
            -   TransactWriteItems/TransactGetItems - Transactions alloww to group multiple actions together and submit them as a single all or nothing operation.
        -   query - returns items based on filter or value. up to 1mb of data
        -   scan - scans the entire table and filters out data(inefficient)
    -   DAX - DynamoDB Accelerator, low latency cache with 5 minutes TTL for cache by default
    -   Streams - changes in DynamoDB can be turned into a stream and read by Lambda and EC2 instances. Made of shards like Kinesis Data Streams
        -   Lambda - uses event source mapping with permissions. Invoked synchonously
    -   CLI
        -   --projection-expression - attributes to retrieve
        -   --filter-expression - filter results from a query, applied after a query finishes but before results are returned. max 1mb of data
        -   --page-size - full dataset received but each API call will request less data
        -   --max-items - max # of results
        -   --starting-token - dictates where to start
    -   Backup - writes to S3 buckets but can't be used by users. To create backups that you can download or use in another AWS service use AWS Data Pipeline, Amazon EMR, or AWS Glue
        -   On-Demand - Create backsup when you want
        -   Point in Time - Enable automatic, continuous backups

---

## Security

Security Bulletins - AWS notifies customers about security and privacy events.

Root Account user can use MFA authentication such as (not sms, but other IAM users aside from root can use SMS) :

-   Hardware MFA Device - hardware device that generates code to sign in
-   U2F Security Key - USB device used for authentication
-   Virtual MFA device - software app that runs on a device that generates code to sign in.

Follow best practice of giving least privilages

-   AWS Artifcat - Security and Compliance reports
-   AWS Shield - DDOS protection service offered in standard or advanced. Layer 3 and 4 protection. Integrates with Route53, Cloudfront, Elastic Load Balancer(ELB).
-   AWS Key Management Service (KMS) - to create and control encryption keys used to encrypt data such as EBS volumes. Audit key usage using CloudTrail. KMS stores the CMK and receives data from the clients, which it encrypts and sends back.
    -   Customer Master Key (CMK) - symmetric (AES-256 keys), never get access to the key. Includes metadata such as key ID, creation date, description, and key state. Contains the key material used to encrypt and decrypt data.
        -   AWS Managed Service Default CMK - Free
        -   User Keys created in KMS - $1/month
        -   User Keys imported - $1/month
    -   Asymmetric (RSA & ECC key pairs) - public key is downloadable but cant access private key. Can use for encryption outside of AWS
    -   KMS Key Policies
        -   Default KMS Policy - created if key policy not provided
        -   Custom KMS Key Policy - define users and roles that can access the keys. Useful for cross account access
    -   Envelope Encryption - anything over 4kb needs to be encrypted using Envelope Encryption, using GenerateDataKey API
-   AWS Web Application Firewall (WAF) - Used to monitor HTTP and HTTPS requests that are forwarded to Amazon CloudFront, API Gateway, or Load Balancer. Pricing based on how many rules you deploy and traffic.
    -   Regular Rules - filters => condition => rules => Web Access Control List(ACL).
    -   Rate-based Rules - requests will be blocked as it crosses rate based limit. Rate is calculated every 5 minutes.
-   AWS Inspector - Automated security assessment service that helps improve the security and compliance of EC2 instances.
-   SSM Parameter Store - store configuration and secrets encrypted by KMS. Configured using path and IAM policies. Integrates with CloudWatch and Cloudformation. Doesn't automatically rotate the database credential
    -   SecureString - plain text parameter name with an encrypted value. only uses one call to get
-   AWS Secrets Manager - force rotation of secrets every X days. Secrets are encrypted using KMS. Integrate with RDS, RedShift, and DocumentDB. More expensive than SSM Parameter Store. Can't be used for encrypting data at rest.

### IAM

-   AWS IAM - Identity and Access Management, by default all actions denied. Have to grant privelages as the root user. Manage access in AWS by creating policies and attaching them to IAM Identities(users, groups, roles)
    -   Users - Recommended IAM entity when granting a person long term access permissions.
    -   Groups - Collection of Users and permissions, can't contain other groups or nest. Users can belong to more than 1 group
    -   Policies - allows or denies permissions to AWS, attached to identity or users
        -   Policy Generator Site - https://awspolicygen.s3.cn-north-1.amazonaws.com.cn/policygen.html
        -   Policy Simulator - google it
        -   Policy Principal - specify the principal that is allowed or denied access to a resource (a principal is a person or app that can make a request for an action on an AWS resource). Can use it in trust policies for IAM roles and in resource based policies, Can't use in an IAM identity based policy
        -   Policy Resource - specify a resource using an ARN
        -   Policy Condition - specify conditions
        -   Policy Variables - policy variables act as placeholders in template
        -   Permissions Boundary - managed policy that is used for an IAM user or role. Defines maximum permissions that the identity based policies can grant but does not grant permissions.
            ![](https://assets-pt.media.datacumulus.com/aws-dva-pt/assets/pt1-q59-i1.jpg)
    -   Roles - Access to temporary time and permissions, given to users, services, apps, etc best for short term. Does not have standard long-term credentials instead temp credentials. Use an IAM policy for permissions.
    -   Trust Policy - The only Resource based policy that IAM supports. Define which (accounts, users, and roles) can assume a role. Must attach both a trust policy and an identity policy to an IAM Role.
    -   Certificates - used as a certificate manager only when you need to support HTTPS in a region that doesn't support AWS Certificate Manager(ACM).
    -   Access Advisor and Credential Reports - tool to identify unused roles, IAM reports the last used timestamp
    -   Access Analyzer - identify resources in your organization and accounts that are shared with an external entity. Helps identify unintended access to resources
-   AWS Organizations - For large business
    -   Service Control Policy (SCP) - To centrally control policies, Can do policies in Organizational Units and individual members. limit permissions but do not grant permissions.
    -   Organization Trail - trail that logs all events
    -   ![](https://media.datacumulus.com/aws-dva-pt/assets/pt3-q32-i1.jpg)

### Amazon Cognito

-   Amazon Cognito - let's customers add user sign in with Facebook, Google, Amazon. Helpful for hundreds of users, mobile users, or authenticate with SAML. Look into re:Invent Serverless Authentication and Authorization slideshow.

    -   Types
        -   Cognito User Pools - sing in for app users, integrate with API gateway and application load balancer. serverless database of users. returns a token
            -   Lambda Triggers - can invoke lambda functions on triggers
    -   Cognito Identity Pools - aws credentials mapped to IAM roles and policies that allows guests, integrates with cognito user pools. free
    -   Cognito Sync - deprecated aand replaced by AppSync, syncs data from device to Cognito
        ![](https://media.datacumulus.com/aws-dva-pt/assets/pt1-q4-i3.jpg)

-   Amazon Cloud Directory - directory service provides web-based directories to organize users, groups, devices, policies
-   Amazon Directory Service - provides single sign on to AWS, uses existing Microsoft Actice Directory

### Directory Service

-   AWS Managed Microsoft AD - AD managed in AWS and can have on prem AD as a trusted connection. If user not in AWS checks On Prem
-   AD Connector - proxy into on prem AD
-   Simple AD - AD compatible managed directory on AWS, cant be joined with on premise AD. For microsoft in AWS

### AWS Single Sign-On

-   AWS Single Sign On (SSO) - cloud service that allows users to sign in to a user portal with their existing corporate credentials and access all of their accounts and apps from one place. Can be integrated with Microsoft Active Directory, meaning they can enter their Active Directory credentials.

### Security Token Service

-   Security Service Token (STS) - limited and temp access up to 15 mins - 1 hour.
-   API
    -   AssumeRole - defines IAM role and access within account or cross account
    -   AssumeRoleWithSAML - return credentials for users logged with SAML
    -   AssumeRoleWithWebIdentity - Use cognito Pools instead of this
    -   GetSessionToken - MFA
    -   GetFederationToken - obtain temp creds for federated user
    -   GetCallerIdentity - return details about IAM user or role
    -   DecodeAuthorizationMessage - decode error message when API is denied
    -   iam:PassRole - passes permissions to other services
-   Policy - IAM Policies and S3 bucket Policies work together to decide allowable actions.
    -   Managed Policy - maintained by AWS
    -   Customer Managed Policy - Best Practice and allows version control and variables
    -   Inline policy - Strict 1-1 relationship between policy and principal, policy is deleted if you delete the IAM principal

### Monitoring

-   AWS Systems Manager - allows to group resources like Ec2 instances, S3 buckets, by application, view operational data for monitoring and troubleshooting and take actions on groups of resources.
    <br> <br>

-   Cloudwatch - Focuses on the activity of AWS services and resources, reporting on their health and performance. Security repositry with threat analytics and metrics.
    -   Metrics -
        -   Basic Monitoring - metrics every 5 mins, enabled by default using AWS Management Console
        -   Detailed Monitoring - metrics every 1 min, enabled by default using CLI or SDK
        -   High Resolution - metrics every 1 second, alarm can be triggered as often as 10 seconds
    -   Logs - Can go to S3 for archival, stream to ElasticSearch. By default no logs from EC2 will go to CloudWatch. Can be setup on premise also. Never expire by default
        -   Cloudwatch Logs Agent - old version of agent, can only send CloudWatch logs
        -   CloudWatch Unified Agent - Can collect additional metrics like ram etc.
    -   Events - send notifications can schedule on a CRON or event pattern.
        -   EventBridge - evolution of Cloudwatch events, can work with Zendesk, DataDog, Etc. Use when you need to integrate with 3rd party SaaS applications.
    -   Alarm - triggers notifications for any metric
-   Cloudtrail - Log of all actions and API calls taking place in AWS by a user, role, or an AWS Service.
-   AWS Config - continually audit, monitor for compliance, or vulnerabilities in AWS.Helps with compliance auditing, security analysis, change management, and troubleshooting.
    -   Specify resource to record => Setup S3 bucket to configure snapshots => Setup SNS to stream notifications => Grant AWS Config permissions for S3 and SNS => Setup rules
-   X-Ray - troubleshooting application performance and errors, provides end to end view of requests as they travel through your application and maps underlying components. Can collect data across AWS Accounts. To debug and trace data across accounts
    -   must import the AWS X-Ray SDK and install X-Ray daemon to enable it
    -   Tracing - end to end way to follow requests
        -   Segments/SubSegments - details on app/service
        -   Sampling - amount of requests sent, can control amount of data that you record and modify sampling behavior without having to redeploy
        -   Annotations - Key-Value pairs used to index traces and use with filters
        -   Metadata - Key-Value pairs, not indexed or used for searching
    -   If not working in:
        -   EC2 ensure IAM role has proper permissions and daemon running. The X-Ray daemon uses the instances profile role automatically.
        -   AWS Lambda ensure IAM role has IAM execution role and X-ray is imported into code
        -   Example of write permissions for X-Ray via IAM policy: <br>
        ```
            {
                "Version": "2012-10-17"
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Action": [
                            "xray:PutTraceSegments",
                            "xray:PutTelemetryRecords",
                            "xray:GetSamplingRules",
                            "xray:GetSamplingTargets",
                            "xray:GetSamplingStatisticSummaries"
                        ],
                        "Resource": ["*"]
                    }
                ]
            }
        ```

| CloudWatch                                          | CloudTrail                          | Config                                           |
| --------------------------------------------------- | ----------------------------------- | ------------------------------------------------ |
| resource performance monitoring, events, and alerts | account specific activity and audit | resource specific history, audit, and compliance |

### Improve Security AWS

1. Accurate account info
2. use MFA
3. no hard coding secrets - use AWS Secrets Manager
4. Limit security groups - use AWS Config or AWS Firewall Manager to ensure VPC config is correct
5. Intentional data policies
6. Centralize AWS Cloudtrail logs
7. Validate IAM roles - AWS IAM Access Analyzer
8. Take action on GuardDuty findings
9. Rotate your keys
10. Become involved in dev cycle

---

## Support

-   AWS Support plans
    -   Basic -
    -   Developer -
        -   Best practice guidance,
        -   Client Side Diagnostics
        -   Architecture/tecgnical support during business hours.
    -   Business - response time of 1 hour for production systems
        -   Use case guidance,
        -   All aws trusted advisor checks (online tool that guides best practices on cost and performance improvements)
        -   AWS Personal Health dashboard
        -   24x7 technical support engineers.
        -   AWS Support API
        -   Access to Infastructure Event Management(IEM) for a fee, included with Enterrpise
        -   Chat access to AWS Support Engineers
    -   Enterprise - Response time of 15 mins for production systems
        -   Application architecture guidance, event management,
        -   Technical Account Manager (TAM) and Support Concierge Service (AWS Billing and account experts)
        -   AWS support API
        -   Access to Infastructure Event Management(IEM) - provide architectural and scaling guidance

---

## Migration

-   AWS Total Cost Ownership (TCO) - free tool that provides info on possible savings when deploying to AWS. (Cost Explorer only analyzes current cost and ussage)
-   AWS Application Discovery Service - helps systems integrators plan application migration projects by identifying on-premise applications.
-   AWS Cloud Adoption Framework (CAF) - helps organizations design a road map to cloud adoption
-   AWS Migration Portfolio Assesment : available to Amazon Partner Network (APN). An assesment tool that recommends instance sizes, cost comparison, migration estimate, timeline and costs.

-   AWS Cloud Migration Framework
    -   Business
    -   People - HR
    -   Governance
    -   Platform
    -   Security
    -   Operations
-   6 Different Staretegies for Migration
    -   Rehosting - Lift and Shift recreate on AWS
    -   Replatforming - Lift, Tinker, and Shift
    -   Refactoring - Driven by a need to add new features and edit code, modernize
    -   Repurchasing - Software as a service option
    -   Retaining - Keeping critical applications at the source environment
    -   Retiring - removing applications that are no longer needed
-   Snow Family - transports data into aws physically

    -   snowcone - 8tb
    -   snowball - 42tb to 80tb
    -   snowmobile - 100PB

-   CloudEndure Migration - automated lift and shift for migrating apps.

-   AWS Server Migration Service(SMS) - migrates workloads to AWS, supports virtual machine migrations, then saves them as a new Amazon Machine Image(AMI) that can be launched as an EC2

---

## API Gateway

-   Can handle API versioning and handle different environments
-   API Types - mapping templates only available for AWS and HTTP(able to transform payload in route)
    -   HTTP API - Lambda, HTTP backends. no data mapping, usgae plan, or API keys
    -   Websocket API - Lambda, HTTP, AWS Services. stateful use case so theyre implemented in real time applications. used for 2 way communication
    -   REST API - Lambda, HTTP, AWS Services
    -   Mock - returns a response without sending to the backend
-   Endpoint Types
    -   Edge-Optimized - routed through CloudFront Edge locations
    -   Regional - For Clients within the same region
    -   Private - Only accessed from your VPC
-   Deployment Stages - need to deploy for changes to be in effect, deployed in stages
    -   Stage Variables - environment variables for API gateway, passed in context object in AWS
    -   Canary Deployment - usually prod stage, can choose % of traffic the stages receive
-   Caching - reduces # of calls made to API, Default TTL is 300 seconds but max is 3600s. Capacity between .5gb to 237gb. expensive so used mainly in production
-   Usage Plans & Api Keys - use Api keys to identify clients and meter access, how much and how fast they can call api. can throttle and add quota
-   CloudWatch - metrics are by stage
-   Security - controlling and managing access to REST API 
    -   Resource Policies / IAM - JSON similar to Lambda Resource policy, Allow for access and security. Great for users and role already in AWS
    -   Cognito User Pools - API gateway automatically verifies using AWS Cognito
    -   Lambda Authorizer / Custom Auth - token based auth OAuth or SAML, great for 3rd party

---

## Code as Config

-   AWS CloudFormation - is a Yaml based tool used to define resources, infastructure as code. Uploads templates into S3
    -   [AWS Resorces, all 224](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) represent different AWS components
    -   Parameters - provide inputs for templates
        -   Ref, YAML shorthand !Ref can call Parameters and Resources
        -   Fn::GetAtt - returns the value of an attribute from a resource in the template
        -   bootstrapped from filepath example location "/etc/ecs/ecs.config"
        -   Parameters Supported:
            -   String
            -   Number
            -   List<number> - Array of integers or floats
            -   CommaDelimitedList - array of literal strings seperated by commas
            -   AWS::EC2::KeyPair::KeyName - Amazon Ec2 Key pair name
            -   AWS::EC2::SecurityGroup::Id - Security group ID
            -   AWS::EC2::Subnet::Id - subnet Id
            -   AWS::EC2::VPC::Id - VPC ID
    -   Resources - describes resources that you want to provision, can associate with conditions
    -   Mappings - hardcoded values, handy for dev vs prod or AWS regions etc
        -   Fn::FindInMap
    -   Outputs - optional values that can be imported into other stacks.example outputting variables like VPC ID or Subnet ID. Exported output values must have unique names within a single region.
        -   Need to be exported and imported using Fn::ImportValue
    -   Conditions, can't be used with Parameters
        -   Fn::If / Fn::Not / Fn::Equals etc
    -   Other Functions
        -   Fn::Join
        -   Fn::Sub
    -   Drift Detection - detects if a stacks configuration differs, has drifted from expected configuration.
    -   Rollbacks - if failure the changes get deleted and version rolls back to before failure
    -   ChangeSets - view changes in stack before it happens
    -   Nested Stacks - reuse stacks in other stacks example load balancer
    -   Cross Stacks - Only within same region, helpful when stacks have different lifecycles, use Export and Import
        -   Fn::ImportValue - returns value of an output exported by another stack
    -   StackSets - Create, Update, Delete stacks across multiple accounts and regions
        ![](https://media.datacumulus.com/aws-dva-pt/assets/pt1-q3-i1.jpg)

### Serverless Application Model

Defines infastructure in a template. Combination of Lambda functions, event sources, and other resources(API, Database, Event Source Mapping) that work together to perform tasks. Enables teams to store and share reusable applications and assemble and deploy serverless architecture. No need to clone, build, package, or publish source code to AWS before deploying it.

-   Yaml Code that is built on CloudFormations and can use CodeDeploy to deploy lambda functions.
-   Structure - requires transform and resources
    -   Transform Header (required) - indicates its SAM template "Transform: 'AWS::Serverless-2016-10-31'"
    -   Accepts: Global, Description, Metadata, Parameters, Mappings, Conditions, Resources, Outputs
    -   Globals (optional)
        -   AWS::Serverless::Api - creates a collection of Amazon API gateway resources and methods that can be invoked through HTTPS endpoints.
        -   AWS::Serverless:: Application
        -   AWS::Serverless::Function - creates a Lambda function
        -   AWS::Serverless::HttpApi
        -   AWS:: Serverless::LayerVersion
        -   AWS::Serverless::SimpleTable - Creates a DynamoDB table with a single attribute primary key.
        -   AWS::Serverless::StateMachine
    -   Resources (required) - specifies the resources such as EC2 or S3.
    -   Package and Deploy
        -   AWS cloudformation package
        -   AWS cloudformation deploy
-   Policy Templates - adds permission to lambda
    -   S3ReadPolicy - read only permission
    -   SQSPollerPolicy - poll SQS queue
    -   DynamoDBCrudPolicy - crud policy
-   Serverless Application Repository (SAR) - repo for serverless applications

### Cloud Development Kit

AWS CDK used to define resources using programming languages and cloudformation. If you want to define AWS infastructure in a programming language use Cloud Development Kit (CDK)

-   Steps to use CDK - Create template from CDK => add code to create resources => Build the app (optional) => Synthesize one or more stacks in the app => Deploy
    1. Template - ` CDK Init` and select language
    2. Resources -add code to create resources.
    3. Build -
    4. Synthesize - creates a CloudFormation template
    5. Deploy - ` CDK deploy`

### AWS Step Functions

Serverless function orchestrator. Can create multi step proccesses using Lambda Functions for each step in the proccess to create a workflow. Handles state, checkpoints, restarts.

-   Written in JSON Used to model workflows. Start workflow with SDK, API Gateway, Event Bridge
    -   Standard Workflows - max duration 1 year, 2000/second. exaclty one workflow
    -   Express Workflows - max duration 5 minutes 100,000/second. at least once workflow

Task Example in step formation, example is of a single task. Can use different types such as `Wait`, `Fail`, etc.

```
"HelloWorld": {
    "Type": "Task",
    "Resource": "arn:aws:lambda:use-east-1:12345:function:HelloFunction",
    "Next": "AfterHelloWorldState",
    "Comment": "Run the HelloWorld Lambda function"
}
```

#### Policy Example

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1", # who/what is authorized
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject", # which condition
            "Resource": "arn:aws:s3:::notes.fdlme.com/*" # Resources to which authorized tasks are performed
        }
    ]
}
```

-   S3 policy example with policy variable, example gives each user a home folder with access

    -   ![](https://assets-pt.media.datacumulus.com/aws-dva-pt/assets/pt1-q40-i1.jpg)

-   Cloudformation acceptable Templates
    -   ![](https://assets-pt.media.datacumulus.com/aws-dva-pt/assets/pt1-q60-i1.jpg)

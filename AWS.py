# IAM stands for Identity and Access Management and this is how AWS controls who has access to your organization's
# account.

#  EC2 stands for Elastic Compute Cloud, and the word of the day is elastic.

#  Notice under the summary that this user group has an ARN, or A-R-N, which stands for Amazon Resource Names, all of
#  your cloud infrastructure, including your servers, networking components, storage, IAM users, your roles, almost
#  everything will have a unique ARN.

# The other AWS service that got launched in 2006, was called Simple Storage Service, and it's abbreviated as S3.

# Because you could now virtually build servers and storage solutions in the cloud with EC2 and S3, these services
# acquired the term Infrastructure as a Service, or IaaS, where instead of building out your own physical infrastructure
# of racks and servers, you're renting someone else's racks, and only paying them for how much of the service you
# consume.

# OWASP top 10 !!!!!! course about vulnerabilities

#  Virtual machines in AWS are called Amazon Machine Images or AMI.

# Check Allow SSH traffic from and make sure that anywhere is selected in the pull down. This will allow you to connect
# a terminal to your EC2 instance using your private key from the key pair from anywhere in the world. Later on, we'll
# dive more into how security groups work and talk about some of the ways that you can further protect your server.
# Also, check Allow HTTP traffic from the internet since this EC2 instance will be a publicly available web server.
# I have the HTTPS option unchecked because we won't be installing an SSL key directly onto our web server in this
# course.

#  Stopping and starting an instance is different than just rebooting it. If you stop and start an instance this virtual
#  machine will actually move to another physical server in the availability zone. So do this if you're having problems
#  connecting to the instance because it could be a hardware failure on the AWS side.

# Vertical scaling is increasing the physical hardware to a single server. Horizontal scaling spreads traffic across
# several identical servers.

# Stopping and starting an instance can move the virtual machine to a new physical host.

# Elasticity expands upon scalability and can scale resources up and down automatically to match demand.

# In the VPC console, on the left-hand menu, click on Internet Gateways. One was already created for us when we launched
# our new instance. This allows our servers and our public subnet to talk out to the internet, and it also allows for
# outside internet traffic to pass into our server, which is filtered by the security groups on that instance

# If you need this public IP address to stay the same, regardless of what happens to this instance, then you'll need
# to request an elastic IP.

#  One way to securely connect to your instances is by using a bastion host. A bastion host is an instance you put in
#  the public subnet that is really locked down and monitored, and you connect to this machine first, and then from
#  there, you make connections to the other servers in your VPC. AWS has a quick start script for this. Type bastion
#  into the search bar and hit Enter. Click on the Linux Bastion Hosts entry. These quick starts are some common
#  architectures using AWS best practices that you can launch directly into your AWS account.

# Another method for connecting securely to Linux and Windows instances is to use AWS Session Manager.

#  Another common solution to securing your network is to use a VPN. By using an AWS client VPN, you can use a VPN
#  client on your home or work computer to establish a secure connection with your VPC. This works really well for
#  allowing you to use coding and database management tools with your servers just like they were sitting across the
#  desk from you. Another way you can use a VPN within AWS is a site-to-site VPN and this is one of the ways that you
#  can bridge your existing on-premise datacenter network or your entire office network with your VPC.

#  There are three types of elastic load balancers. Network load balancers are really fast, but they don't have many
#  features because they achieve that speed by not looking too closely at the traffic coming in. Gateway load balancers
#  are for switching traffic coming into virtual networking appliances made by vendors that aren't AWS, such as Cisco
#  virtual firewalls. Application load balancers are great for web traffic because they will look at the incoming
#  traffic and route it based on a set of rules. We will be using an application load balancer since we are running
#  web servers.

#  Amazon's primary storage service for EC2 servers is called Elastic Block Store, elastic because it can stretch in
#  size when you need it to.

# EFS Elastic file system its like storage between two EC2 instance

# S3 Simple Storage Service

#                               AWS CLI
#
# after installing cli type into terminal          aws configure
# type secret id and secret key region , output default

# aws s3api list-buckets     check correct credentials and return list of buckets in json format
# aws s3 ls    return list of buckets

# aws s3 cp <file on local machine>  s3://<bucket_name>/<folder name>
# aws s3 sync <target folder on computer>    synchronizes file on local with s3 bucket

# Let's use the AWS SDK, or Software Development Kit to interface with S3 from our source code on our server.

#  AWS Secrets Manager. You can find it by typing Secrets Manager into the search bar. With Secrets Manager, you will
#  store the key or passwords securely into Secrets Manager.

#  If you need to move a lot of data into AWS, check out the AWS Snow family of services. With an AWS Snowball, Amazon
#  will ship you a fancy hard drive array that you plug directly into your server, copy your files to it and mail it
#  back to AWS, where they will connect it to their network and load all of your data into S3. This can be much cheaper
#  from moving a lot of data than paying the data transfer costs for using S3 over the public internet.

#  CloudFront is a Content Delivery Network or CDN, that can mirror your S3 bucket all across the world

#  Database as a Service or DBaaS

#  I would recommend looking at the AWS Data Migration Service, which can take your on-premise relational database and
#  create a real-time in-sync clone of your database in the cloud so you can perform a smooth transition from your
#  on-premise data center into AWS.

# Relational Database Service (RDS)

# SQS is more popular and it's simpler to use, hence it's name, Simple Queue Service, but it can get expensive if you're
# sending it lots and lots of events, which is one reason why there's Kinesis. Simple Notification Service, or SNS, can
# be used to push out a message, such as an email or text message or an HTTP call to a web hook. So after your SQS queue
# has finished generating the report they were waiting on, SNS can send them an email and let them know that they can
# log back in and download their report. All the messaging services work a bit differently, so it's important to
# understand when to use the right tool for the right job.

# С помощью Amazon Kinesis можно просто собирать, обрабатывать и анализировать потоковые данные в режиме реального
# времени, чтобы своевременно получать аналитические результаты и быстро реагировать на новую информацию.

#  If you want to use Kubernetes to orchestrate your containers instead of ECS, Amazon has a service called Elastic
#  Kubernetes Service or EKS. You'll find a lot of similarities between ECS and EKS

# translate, recognition, textract, transcribe       services of machine learning
# Web Infrastructure Design Project

## Overview
This project aims to design a scalable, secured, and monitored web infrastructure for hosting the website www.foobar.com. The infrastructure is split into multiple servers, with each component (web server, application server, database) hosted on dedicated servers to ensure efficient resource utilization and scalability. Additionally, security measures such as firewalls and HTTPS implementation are incorporated, along with monitoring solutions to track performance, availability, and security of the infrastructure.

## Tasks Completed
### 1. Simple Web Stack
- Designed a basic web infrastructure with a single server hosting the website www.foobar.com.
- Components included a web server (Nginx), application server, and MySQL database.
- Explained the roles of each component and identified issues such as single point of failure (SPOF) and downtime during maintenance.

### 2. Secured and Monitored Web Infrastructure
- Expanded the infrastructure to include three servers, each with its own firewall.
- Implemented SSL certificate for HTTPS encryption to secure traffic.
- Integrated monitoring clients to collect data for performance, availability, and security monitoring.
- Explained the necessity of firewalls, HTTPS, and monitoring for enhancing security and ensuring the stability of the infrastructure.
- Identified potential issues such as terminating SSL at the load balancer level and having only one MySQL server capable of accepting writes.

### 3. Scale Up
- Split components (web server, application server, database) onto separate servers to design a scalable infrastructure.
- Utilized load balancing (HAproxy) to distribute incoming traffic across multiple servers for improved performance and reliability.
- Provided explanations for splitting components and utilizing load balancing to achieve scalability and efficient resource utilization.
- Addressed potential issues and limitations of the infrastructure design.

## Components
- **Web Server (Nginx)**: Serves static content to users' browsers.
- **Application Server**: Executes application code and generates dynamic content.
- **Database Server (MySQL)**: Stores and manages website data.
- **Firewalls**: Implemented for security to filter and control incoming and outgoing traffic.
- **SSL Certificate**: Ensures secure communication between users' browsers and servers.
- **Monitoring Clients**: Collects data for performance, availability, and security monitoring.
- **Load Balancer (HAproxy)**: Distributes incoming traffic across multiple servers to optimize performance and reliability.

## Issues Addressed
- **Single Point of Failure (SPOF)**: Mitigated by redundancy and load balancing to ensure high availability.
- **Security Concerns**: Addressed through firewalls and HTTPS implementation to protect against unauthorized access and data breaches.
- **Monitoring**: Implemented to track performance, availability, and security metrics and respond to issues promptly.

## Conclusion
By completing the tasks outlined in this project, a robust web infrastructure has been designed to host www.foobar.com. The infrastructure is scalable, secured, and monitored, capable of handling increased traffic and workload efficiently while ensuring the stability and security of the website.

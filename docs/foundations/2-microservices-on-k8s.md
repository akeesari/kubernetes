# Microservices on Kubernetes

In this chapter, we take a closer look at why Kubernetes is considered the go-to platform for deploying and managing microservices in the cloud. You’ll learn how it simplifies container orchestration, supports dynamic scaling, and ensures service resilience—all critical factors in building reliable, cloud-native applications. We'll also introduce key Azure services—like Azure Kubernetes Service (AKS), Azure Container Registry (ACR), Key Vault, PostgreSQL, Redis, Application Gateway, and Azure Front Door—that work together to form a secure and scalable microservices infrastructure.

## Introduction

Modern application development with microservices

Today’s software systems are increasingly built using microservices architecture, where applications are broken down into smaller, loosely coupled services. Each service is independently developed, deployed, and maintained—enabling faster release cycles, team autonomy, and better scalability.

However, this approach also introduces new challenges. Managing hundreds of services, coordinating deployments, monitoring health, and scaling them efficiently requires more than traditional infrastructure tools can offer.


## High Level Architecture

The following diagram shows the high level reference architecture for `Building Scalable Kubernertes Infrastructure for Microservices`. this also show the essential cloud components and how they interact with AKS.

[![Alt text](images/image-36.jpg){:style="border: 1px solid black; border-radius: 10px;"}](images/image-36.jpg){:target="_blank"}


## Why Kubernetes?

Kubernetes—often abbreviated as **K8s**—is the industry standard for container orchestration. It automates the deployment, scaling, and management of containerized applications, making it an ideal platform for running microservices at scale.

In the context of this book, we’ll be using **Azure Kubernetes Service (AKS)**, Microsoft’s managed Kubernetes offering. AKS provides all the capabilities of Kubernetes without the overhead of managing the control plane, making it easier to get started and focus on building applications.

Kubernetes brings several powerful features that are particularly well-suited to microservices environments:

* **Self-healing**: Automatically restarts failed containers and reschedules them as needed.
* **Auto-scaling**: Dynamically adjusts the number of running instances based on resource usage or demand.
* **Rolling updates and rollbacks**: Ensures smooth deployment with minimal downtime.
* **Service discovery and load balancing**: Manages internal communication between services efficiently.
* **Declarative configuration**: Infrastructure and application deployments are defined in YAML, supporting version control and repeatability.


## AKS Reference Architecture Components

While Kubernetes provides orchestration, it needs a strong supporting infrastructure to meet the demands of real-world microservices applications. Below, we explore key Azure resources and how they integrate with AKS to create a reliable, scalable, and secure platform.

**Azure Log Analytics Workspace**

*Purpose*: Centralized logging and telemetry collection.

*Role in Microservices*: Observability is crucial in distributed systems. Log Analytics integrates with Azure Monitor and Kubernetes to collect logs, metrics, and performance data from your clusters. It helps developers and operations teams quickly diagnose issues, understand system behavior, and make informed decisions.

**Azure Virtual Network (VNet)**

*Purpose*: Secure, isolated network space in Azure.

*Role in Microservices*: Kubernetes nodes and Pods must communicate securely across services. A VNet provides the foundation for network isolation, inter-service communication, private endpoints, and hybrid connectivity to on-prem resources or other cloud regions.

**Application Gateway:**

The Application Gateway serves as the entry point for client requests from the public DNS. It acts as a reverse proxy and load balancer, routing requests to the appropriate backend services. With features like SSL/TLS termination, Web Application Firewall (WAF) protection and backend pool configuration, the Application Gateway helps to decouple clients from services. 
Azure Application Gateway with Application Gateway Ingress Controller (AGIC) acts as a Layer 7 ingress controller for AKS. This allows for secure and scalable exposure of AKS-hosted microservices to the internet or other services.

**Azure Front Door and CDN Profile**

*Purpose*: Global HTTP load balancer with intelligent routing and content delivery network.

*Role in Microservices*: Front Door distributes traffic to Kubernetes services across regions with built-in **SSL offloading**, **caching**, and **Web Application Firewall (WAF)**. It ensures high availability, low latency, and secure access for frontend services or APIs exposed to the internet.

**Azure Container Registry (ACR)**

*Purpose*: Private registry to store and manage Docker container images.

*Role in Microservices*: Every microservice deployed in Kubernetes is packaged as a container. ACR serves as a secure, scalable place to host these container images. It integrates seamlessly with AKS for faster, more secure deployments.

**Azure Kubernetes Service (AKS)**

*Purpose*: Managed Kubernetes platform on Azure.

*Role in Microservices*: AKS is the heart of your cloud-native infrastructure. It abstracts away the complexity of Kubernetes management—handling upgrades, scaling, monitoring, and security—so you can focus on building and running microservices efficiently.

**Azure PostgreSQL Flexible Server**

*Purpose*: Managed PostgreSQL database service with high availability and performance.

*Role in Microservices*: Many microservices need structured, relational data storage. PostgreSQL Flexible Server offers a cost-effective, scalable, and secure backend for services that require ACID-compliant databases. It also supports VNet integration and private access for enhanced security.

**Azure Key Vault**

*Purpose*: Securely store and manage secrets, certificates, and encryption keys.

*Role in Microservices*: Secure configuration is a must in production. Key Vault allows your services to retrieve sensitive data like database connection strings, API keys, and certificates securely without hardcoding them in containers or source code.

**Azure Cache for Redis**

*Purpose*: In-memory data store for fast data access.

*Role in Microservices*: Microservices often benefit from caching to reduce latency and offload backend services. Azure Cache for Redis acts as a shared, high-performance cache layer—perfect for session storage, frequent reads, and pub/sub messaging patterns.

**Azure Storage Account**

*Purpose*: Massively scalable object, file, and blob storage.

*Role in Microservices*: Services may need persistent storage for logs, file uploads, images, or large binary data. Azure Storage supports secure and cost-effective options like **Blob Storage**, **File Share**, and **Queue Storage**, easily accessible from AKS Pods via private endpoints or identity-based access.


## How It All Comes Together

When Kubernetes is integrated with the broader ecosystem of Azure services, it forms a powerful foundation for running microservices at scale. Each component plays a distinct role in supporting a cloud-native architecture:

* **Azure Kubernetes Service (AKS)** serves as the core orchestration engine, running containerized applications reliably and efficiently.

*   **Azure Container Registry (ACR)** stores and manages container images that are deployed to AKS.
  
*   **Azure Virtual Network (VNet)** provides isolated and secure network boundaries, allowing private communication between services and resources.
    
*   **Azure PostgreSQL Flexible Server** serves as a managed relational database for data persistence needs across microservices.
    
*   **Azure Key Vault** securely stores secrets, connection strings, and certificates, ensuring secure communication and access.
    
*   **Azure Cache for Redis** enhances performance by providing low-latency access to frequently used data.
    
*   **Azure Front Door** and **Azure CDN Profile** enable global load balancing, SSL termination, and content acceleration for end-user traffic.
    
*   **Azure Storage Account** supports static file storage, backups, and shared file systems needed by services.
    
*   **Azure Log Analytics Workspace** is integrated with AKS to provide centralized monitoring, diagnostics, and logging.
    
*   **Private Endpoints** and **Private DNS Zones** are used extensively to enforce private network access between services, eliminating exposure to the public internet.

*   **Azure DNS Zone** is used to centrally manage custom domain names for services exposed via Application Gateway, Front Door.    

Together, these services create a robust, scalable, and secure infrastructure for microservices—aligned with the core goal of this book: **Building Scalable Kubernetes Infrastructure for Microservices**.

## Azure + Terraform = Production-Ready IaC

Microsoft Azure provides comprehensive support for containerized workloads, cloud-native development, and scalable microservices architecture. Whether you’re building new applications or modernizing legacy systems, Azure offers the tools and services necessary for success:

Azure’s global presence, enterprise-grade security, and integration with identity (Azure AD), monitoring, and DevOps pipelines make it an excellent platform for delivering modern, distributed applications at scale.

Terraform by HashiCorp provides a powerful, cloud-agnostic way to manage Azure infrastructure through code. Using the **Azure Provider (azurerm)**, teams can define and provision everything from virtual networks and Kubernetes clusters to databases and DNS zones in a repeatable, automated way.

By combining Terraform with Azure’s native services, you gain a highly scalable, version-controlled, and production-ready approach to building and managing modern microservices infrastructure.


## Reference
- [Microsoft MSDN - Microservices architecture on Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-microservices/aks-microservices){:target="_blank"}
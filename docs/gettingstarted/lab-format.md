Each lab in this book is carefully designed to simulate real-world scenarios and help you gain hands-on experience with building scalable infrastructure for microservices on Azure using Terraform and Kubernetes. The labs follow a consistent structure to ensure clarity, ease of understanding, and reusability.

Here’s what you can expect in every lab:

## Introduction

This section provides a brief overview of the lab's concepts and definitions. It serves as a quick introduction to get you familiarized with the lab and ready to perform the necessary actions. If you require in-depth knowledge on a specific topic, you can refer to the links provided at the end of each lab.

## Technical Scenario

This section outlines the purpose of the lab within a practical context. It explains where and how you can apply the implementation guide in real-world scenarios, encouraging you to relate the lab scenario to your own Microservice architecture with Kubernetes.

## Prerequisites

This section lists the tools, software, or any prerequisites that need to be installed or set up before starting the lab. Ensuring you have the necessary prerequisites in place beforehand will help you avoid interruptions during the lab.

For example:

```sh
- Active Azure subscription
- Download and Install Terraform
- Download and Install Azure CLI
```

## Objective

This section presents objective of tasks or steps to be implemented in the lab. It provides a comprehensive list of all the actions you will perform during the lab.

For example:

```sh
In this exercise, we will accomplish and learn how to implement the following:

- Task-1: Define and declare variables
- Task-2: Create an Azure service using Terraform
- Task-3: Initialize Terraform
- Task-4: Create a Terraform execution plan
- Task-5: Apply a Terraform execution plan
```
## Architecture Diagram (Optional)

This optional section provides an architecture diagram that illustrates the lab scenario. Architecture diagrams are helpful in visualizing the connections and relationships between components, making it easier to understand the overall scenario.

## Implementation detail

Step-by-step implementation details will be covered in this section.

For example:

login to Azure - Verify that you are logged into the correct Azure subscription before starting anything in Visual Studio Code.

```sh
# Login to Azure
az login 

# Shows current Azure subscription
az account show

# Lists all available Azure subscriptions
az account list

# Sets Azure subscription to desired subscription using ID
az account set <subscription_id>
```

Example of tasks:

## Task-1: Define and declare variable

Task-1 implementation details goes here

```sh
Source code or commands related to Task 1 will be placed here
```

## Task-2: Create a Azure service using Terraform

Task-2 implementation details goes here

```sh
Source code or commands related to Task 2 will be placed here
```

## Reference

This section will cover a list of references for further reading and additional actions.

For example:

References

- [https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-microservices/aks-microservices](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-microservices/aks-microservices){:target="_blank"}

!!! note
    
    The above lab format will be consistently followed throughout the book, providing clear implementation details for each task and guiding you through the practical steps necessary to complete the labs.

!!! Important
    Each lab in this book covers actual implementation details therefore it is always recommended to read the relevant MSDN documentation on particular azure service before start any lab so that is supper easy for you to work on these labs. you will see the links end of each lab for your reference.

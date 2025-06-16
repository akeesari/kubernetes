## Introduction

Setting up a strong Terraform foundation is crucial before diving into infrastructure provisioning. This chapter focuses on preparing the necessary Azure and Azure DevOps components that support Terraform state management, security, and version control. We'll walk through the steps to create a version-controlled Terraform project in Azure DevOps, configure secure credential storage using Azure Key Vault, and set up a remote backend for storing Terraform state.

The `Terraform environment` setup is a one-time activity that lays the foundation for automating infrastructure provisioning using Infrastructure as Code (IaC) principles. Once this setup is completed, you will be ready to create various Azure resources using Terraform in an automated and consistent manner.

## Technical Scenario

As a `Cloud Engineer`, you play a critical role in managing cloud infrastructure efficiently and effectively. As part of your responsibilities, you have been tasked with setting up the Terraform environment, which will empower your team to provision and manage cloud resources using Terraform.

By setting up the Terraform environment, you will provide your team with a centralized platform to automate the creation and management of cloud resources. This setup will streamline the deployment process, enhance collaboration, and improve the overall efficiency of your cloud infrastructure management.

## Prerequisites
  - Download & Install Terraform
  - Download & Install Azure CLI
  - Azure subscription
  - Register resource providers in the subscription
  - Visual studio code
  - Download & Install Git tools
  - Basic knowledge on Terraform

## Objective

In this exercise, our objective is to accomplish the following tasks and gain a deeper understanding of the Terraform environment setup:

**Azure DevOps setup**

- Task-1: Create a new project in azure DevOps
- Task-2: Create a new Azure DevOps Repo for terraform
- Task-3: Clone a new git repo
- Task-4: Add .gitignore file in the git repo for terraform

**Terraform environment setup**

- Task-5: Create terraform Service Principle 
- Task-6: Create new azure resource group
- Task-7: Create new azure storage account & container
- Task-8: Create new azure Key vault 
- Task-9: Create secrets in azure  Key Vault 
- Task-10: Setup Access Policy in Key Vault 
- Task-11: Configure Service Principal Role Assignment 

## High Level components

The following diagram illustrates the essential components used in the Terraform management setup in this lab.

[![Alt text](images/image-39.jpg){:style="border: 1px solid black; border-radius: 10px;"}](images/image-39.jpg){:target="_blank"}

## Implementation details

We'll start by creating the DevOps structure, followed by provisioning the Azure infrastructure for Terraform management. Credentials and secrets will be securely stored in Key Vault, and Terraform will use the Storage Account as a remote backend.

## Task-1: Create a new project in azure DevOps

We will create a new project in Azure DevOps to organize our Terraform-related activities and workflows. This project will serve as a central hub for managing our infrastructure as code.

It is always recommended to have separate project in azure DevOps for Infrastructure as Code maintenance. Here we are going to create new project called `IaC` and under this project we can create a new repo called `terraform` 

Here are the details of the new project:

Project Name - `IaC`

Project Description - `This project contains the source code related to Infrastructure as code (IaC), IaC is a method of provisioning and managing infrastructure using code and automation rather than manual configuration.`

Follow these steps for creating a new project in azure DevOps.

1. Sign in to your organization in Azure DevOps
1. Select New project.
1. Enter project name & description

Once the project is created then you can add more repos as needed.

For example:

- `terraform` - you can use this repo for terraform configuration
- `scripts` - you can use this repo for managing all kinds of scripts like PowerShell, Bash and CLI etc..
- `bicep` - you can use this repo for Microsoft Bicep scripts etc..

[![Alt text](images/image-1.jpg){:style="border: 1px solid black; border-radius: 10px;"}](images/image-1.jpg){:target="_blank"}


## Task-2: Create a new Azure DevOps Repo for terraform

We will create a dedicated Git repository within Azure DevOps to store our Terraform configurations and scripts. This repository will enable version control and collaboration among team members.

Here are the steps to create a new Git repository in Azure DevOps:

- Login into azure DevOps -  [azure DevOps](https://dev.azure.com/){:target="_blank"}
- Select the project where we want to create the repo
- Click on `Repos` left nav link
- From the repo drop-down, select `New repository`
- In the `Create a new repository` dialog, verify that Git is the repository type and enter a name for the new repository. 
- You can also add a README and create a `.gitignore` for the type of code you plan to manage in the repo.

- use lower case for the repos (best practice)
  - repo name - terraform 

for example: 

[![Alt text](images/image-2.png){:style="border: 1px solid black; border-radius: 10px;"}](images/image-2.png){:target="_blank"}

- Initialize the main branch with a README or gitignore

- Create new feature branch (develop) from main

[![Alt text](images/image-3.jpg){:style="border: 1px solid black; border-radius: 10px;"}](images/image-3.jpg){:target="_blank"}


## Task-3: Clone the git repo

We will clone the newly created Git repository to our local machine. This will allow us to work with the Terraform configurations locally and push changes to the remote repository.

Here we will use the Git CMD tool, open the git cmd tool in admin mode and follow these commands to clone the code locally.

```
C:\Users\anji.keesari>cd c:\Source\Repos\IaC

c:\Source\Repos\IaC>git clone https://keesari.visualstudio.com/IaC/_git/terraform
Cloning into 'terraform'...
remote: Azure Repos
remote: Found 4 objects to send. (26 ms)
Unpacking objects: 100% (4/4), 1.22 KiB | 62.00 KiB/s, done.

c:\Source\Repos\IaC>cd terraform

# open the folder in VS code
c:\Source\Repos\IaC\terraform>code .

c:\Source\Repos\IaC\terraform>
```

## Task-4: Add .gitignore file in the git repo for terraform

We will add a .gitignore file to the Git repository specifically tailored for Terraform. This file will exclude unnecessary files and directories from being tracked by Git, ensuring a cleaner and more manageable repository.

This is the first file you need to add in the source code before commit any files.

This .gitignore file will prevent Terraform state files, override files, local tfvars files, and CLI configuration files from being tracked by Git. These files contain sensitive information and can cause issues with consistency and conflicts if multiple users are working on the same Terraform project. It's important to not commit these files to your source code repository to maintain the integrity and security of your infrastructure code.

Here is the sample file:

``` title=".gitignore"
# Local .terraform directories
**/.terraform/*

# .tfstate files
*.tfstate
*.tfstate.*

# Crash log files
crash.log

# Exclude all .tfvars files, which are likely to contain sentitive data, such as
# password, private keys, and other secrets. These should not be part of version 
# control as they are data points which are potentially sensitive and subject 
# to change depending on the environment.
#
*.tfvars

# Ignore override files as they are usually used to override resources locally and so
# are not checked in
override.tf
override.tf.json
*_override.tf
*_override.tf.json

# Include override files you do wish to add to version control using negated pattern
#
# !example_override.tf

# Include tfplan files to ignore the plan output of command: terraform plan -out=tfplan
# example: *tfplan*

# Ignore CLI configuration files
.terraformrc
terraform.rc
```

## Terraform Management Setup

The azure resources which are managing and securing the terraform state and securing the service principle are called `Terraform management resources`

By following these steps, you can set up a Terraform environment for creating Azure resources. It's important to keep your configuration files and state file in a secure location, and to follow best practices for managing infrastructure as code.

Here we are going to use Azure Storage Account for storing the terraform state files and Azure Key vault for securing the secrets used for running the terraform configuration in azure.

Since these steps are part of terraform setup itself,  we can't create following resources using terraform, here we can use either az cli or PowerShell script to create following resources. I'll be showing the az cli and PowerShell script for creating these resources.

We are going to create separate azure resource group for managing terraform management specific azure resource like azure storage account and azure key vault.

We will start with service principe before creating azure storage account and azure key vault.

## Task-5: Create Terraform Service Principle Credentials

A Service Principal is an identity that Terraform can use to authenticate and manage Azure resources.  Terraform uses a Service Principal to authenticate with Azure and manage Azure resources, such as virtual machines, storage accounts, and databases.

Here's how you can create a Service Principal in Azure for use with Terraform:

- Log in to the Azure portal and go to the Azure Active Directory (AD) section.
- Click on "App registrations" and then click "New registration".
- Provide a name for the application and select "Accounts in this organizational directory only" as the supported account type.
- For the "Redirect URI" field, select "Web" and enter a valid URI. This URI can be any valid URI, but it must be accessible to the application.
- Click on "Register" to create the application registration.
Once the application is created, note down the "Application ID" and "Directory (tenant) ID" values. These will be used in the Terraform configuration.
- Create a client secret by clicking on "Certificates & secrets" and then "New client secret". Note down the client secret value that is generated. This value will be used in the Terraform configuration.


Now that you have created a Service Principal in Azure, you can use it in Terraform to authenticate with Azure and manage Azure resources. In your Terraform configuration file, you can add the following code to authenticate with Azure using the Service Principal:

``` tf title="provider.tf"
provider "azurerm" {
  subscription_id = "SUBSCRIPTION_ID"
  client_id       = "CLIENT_ID"
  client_secret   = "CLIENT_SECRET"
  tenant_id       = "TENANT_ID"
}

```

Replace SUBSCRIPTION_ID, CLIENT_ID, CLIENT_SECRET, and TENANT_ID with the values you obtained when creating the Service Principal in Azure. 
<!-- 
1. Assign a role to the service principal: Use the Azure portal or Azure CLI to assign a role to the service principal. This will determine the level of access that the service principal has to Azure resources. -->

additional az cli commands may be helpful.

``` ps1
az login
az ad app create --display-name <APP_NAME>
az ad app create --display-name "sp-tfmgmt-dev"
az ad app show --id <APP_ID> --query "appId"
az account show --query "tenantId"
```

[![Alt text](images/image-7.jpg){:style="border: 1px solid black; border-radius: 10px;"}](images/image-7.jpg){:target="_blank"}

## Task-6: Create new resource group

To maintain the Terraform management resources in Azure, we will create a separate resource group specifically for this purpose.


Resource Group Name - `rg-tfmgmt-dev` 

You can use the following Azure CLI command to create the resource group:

``` ps1
az group create --name <GROUP_NAME> --location <LOCATION>
```

For example:

``` ps1
az group create -n "rg-tfmgmt-dev"-l "east us"
```

[![Alt text](images/image-8.jpg){:style="border: 1px solid black; border-radius: 10px;"}](images/image-8.jpg){:target="_blank"}


## Task-7: Create new storage account & container

To store the Terraform remote state, we will create an Azure Storage Account. This will allow us to store the state file remotely and access it from anywhere, while also providing additional features such as versioning, locking, and auditing.

Terraform remote state is a way to store and manage Terraform's state files remotely. By default, Terraform stores the state file on the local file system, but this can cause problems when working in a team or when scaling up infrastructure. Remote state storage provides a centralized location for storing state files, which makes it easier to manage state across teams and across environments.

 Here is the command to create a new Azure Storage Account using the Azure CLI:

``` ps1
az storage account create --name <ACCOUNT_NAME> --resource-group <RESOURCE_GROUP_NAME> --location <LOCATION> --sku <SKU>
```

For example:

``` ps1
az storage account create -n "tfmgmtstates" -g "rg-tfmgmt-dev" -l "east us" --sku "Standard_LRS"

```
[![Alt text](images/image-9.jpg){:style="border: 1px solid black; border-radius: 10px;"}](images/image-9.jpg){:target="_blank"}

We also need blob container for storing terraform state files, Let's create new storage account container using az cli here

``` ps1
az storage container create --name <CONTAINER_NAME> --account-name <ACCOUNT_NAME> --account-key <ACCOUNT_KEY>
az storage container create -n "terraformstates" --account-name "tfmgmtstates" --account-key "koB5PQEGX5pEHVAWsyM0efP3aeFsuNhw8dzRXvqrLXXcD12VEIC4HkhNnwDAGWUJcZWb8Q3C8yxZ+AStXGHDGQ=="
```

[![Alt text](images/image-10.jpg){:style="border: 1px solid black; border-radius: 10px;"}](images/image-10.jpg){:target="_blank"}

## Task-8: Create new Key vault 

This Key Vault will be used for storing all kind of secrets related terraform management. it is very critical securing secrets like terraform service principle because these are actually used to authenticate Terraform to Azure and create azure resources in the Azure Portal.

create new azure key vault using az cli

``` ps1
az keyvault create --name <VAULT_NAME> --resource-group <RESOURCE_GROUP_NAME> --location <LOCATION>
az keyvault create -n "kv-tfstates-dev" -g "rg-tfmgmt-dev" -l "east us"

```

[![Alt text](images/image-11.jpg){:style="border: 1px solid black; border-radius: 10px;"}](images/image-11.jpg){:target="_blank"}

##  Task-9: Create secrets in Key Vault 

Terraform management secrets will be protected by storing in the azure key vault.

Here are the commands to create and store secrets in the Azure Key Vault using the Azure CLI:

``` ps1
az keyvault secret set --vault-name <VAULT_NAME> --name <SECRET_NAME> --value <SECRET_VALUE>
```

For example:

```ps1
az keyvault secret set --vault-name "kv-tfstates-dev" --name "tf-subscription-id" --value "1115d52c-5170-4366-b262-cc12cba2d222"
az keyvault secret set --vault-name "kv-tfstates-dev" --name "tf-client-id" --value "11183cf3-7184-457a-a71b-eb5fb7e02222"
az keyvault secret set --vault-name "kv-tfstates-dev" --name "tf-client-secret" --value "1118Q~eQTMTWEwpvK~CHeTIrU7l7xnhw9wE1z222"
az keyvault secret set --vault-name "kv-tfstates-dev" --name "tf-tenant-id" --value "1113c4a0-f87d-46ad-b4be-3ee05cefe222"
az keyvault secret set --vault-name "kv-tfstates-dev" --name "tf-access-key" --value "1115PQEGX5pEHVAWsyM0efP3aeFsuNhw8dzRXvqrLXXcD12VEIC4HkhNnwDAGWUJcZWb8Q3C8yxZ+AStXGHDG222"
```

[![Alt text](images/image-12.jpg){:style="border: 1px solid black; border-radius: 10px;"}](images/image-12.jpg){:target="_blank"}


Make sure to store sensitive information, such as passwords or access keys, as secrets in the Azure Key Vault to maintain security and compliance.

## Task-10: Setup Access Policy in Key Vault 

To grant access to the Terraform service principal to retrieve the secrets stored in the Azure Key Vault, we need to set up an access policy in the Key Vault.

Use the following command to set up the access policy using the Azure CLI:

``` ps1
az keyvault set-policy --name <VAULT_NAME> --object-id <OBJECT_ID> --secret-permissions <SECRET_PERMISSIONS> --key-permissions <KEY_PERMISSIONS>
```

For example:

``` ps1
az keyvault set-policy --name "kv-tfstates-dev" --object-id "a68e4529-b584-43c6-9ffd-4ca681da9efc" --secret-permissions get list --key-permissions get list
```

[![Alt text](images/image-6.jpg){:style="border: 1px solid black; border-radius: 10px;"}](images/image-6.jpg){:target="_blank"}


##  Task-11: Configure Service Principal Role Assignment

The new Service principle needs at least contributor access at subscription level where azure resources will be created, 
if you want avoid unnecessary issues during resources creation or azure DevOps terraform automation you can even provide owner role at subscription level so that we don't run any issues while creating azure resource from terraform configuration.


Use the following command to assign the role to the service principal using the Azure CLI:

``` ps1
az role assignment create --assignee-object-id <SERVICE_PRINCIPAL_OBJECT_ID> --role Owner --scope <SCOPE>
```

For example:

``` ps1
az role assignment create --assignee-object-id "a68e4529-b584-43c6-9ffd-4ca681da9efc" --role Owner --scope "/subscriptions/b635d52c-5170-4366-b262-cc12cba2d9be" 
```

Note:- make sure that you will get the service principle object id here instead of app registration object id
service principle object id will be found in `Enterprise Application`


[![Alt text](images/image-13.jpg){:style="border: 1px solid black; border-radius: 10px;"}](images/image-13.jpg){:target="_blank"}


That it! now you've setup terraform management for running your terraform configuration.

## Verify Azure resources

The final step in terraform management is to make sure that all the azure resources are created as expected, let's quickly review them manually. 

*   Go to Azure Portal
    
*   Confirm that the resource group, storage account, container, and Key Vault exist
    
*   Check the secrets are saved and accessible in Key Vault
    
*   Verify the service principal role assignments are in place

[![Alt text](images/image-14.jpg){:style="border: 1px solid black; border-radius: 10px;"}](images/image-14.jpg){:target="_blank"}


## References

- [Microsoft MSDN - Create a project in Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops&tabs=browser){:target="_blank"}
- [Microsoft MSDN - Create a new Git repo in your project](https://learn.microsoft.com/en-us/azure/devops/repos/git/create-new-repo?view=azure-devops){:target="_blank"}
- [Microsoft MSDN - Tutorial: Register an app with Microsoft Entra ID](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/walkthrough-register-app-azure-active-directory){:target="_blank"}
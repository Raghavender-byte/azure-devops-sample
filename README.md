# Azure DevOps CI/CD Sample Repository

This repository contains sample applications and pipelines to demonstrate CI/CD in Azure DevOps.

## Applications

1. **Java Application**
   - Simple calculator with JUnit tests
   - Maven/Gradle build files
   - Located in `java-app/`

2. **Python Application**
   - Simple calculator with pytest tests
   - Requirements file for dependencies
   - Located in `python-app/`

## Pipelines

1. **Java Pipeline** (`java-pipeline.yml`)
   - Builds with Maven
   - Runs JUnit tests
   - Publishes test results
   - Deploys artifact

2. **Python Pipeline** (`python-pipeline.yml`)
   - Sets up Python environment
   - Installs dependencies
   - Runs pytest with JUnit XML output
   - Publishes test results
   - Deploys artifact

3. **Full Deployment Pipeline** (`full-deployment-pipeline.yml`)
   - Combines both applications
   - Adds staging and production environments
   - Includes approval gates

## How to Test the Pipelines

1. **Set up Azure DevOps**
   - Create a new project
   - Push this repository to your Azure DevOps repo

2. **Create Pipelines**
   - Navigate to Pipelines > Create Pipeline
   - Select your repository
   - Choose "Existing Azure Pipelines YAML file"
   - Select one of the pipeline files from `.azure/` directory
   - Run the pipeline

3. **Trigger Pipeline Changes**
   - Make code changes to test the trigger
   - Push a failing test to see pipeline failure
   - Check test results in the pipeline runs

4. **Test Deployment Gates**
   - For the full deployment pipeline:
   - Set up environments in Azure DevOps
   - Configure approval checks
   - Test the promotion between stages

## Expected Outcomes

- Successful builds should show all tests passing
- Code changes should automatically trigger pipelines
- Test failures should fail the pipeline
- Deployment stages should only run after successful builds

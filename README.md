# Cloud Run Deployment to Query BigQuery on GCP

## **Objective**
The goal of this assignment is to create a Google Cloud Platform (GCP) account, set up a Cloud Run function, and deploy a serverless application that reads data from BigQuery and performs a simple aggregation query (e.g., `SUM(*)` on a given column).

---

## **Step 1: Set Up Google Cloud Platform (GCP) Account**
1. **Create a Google Cloud Account:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/).
   - If you don’t have an account, sign up and create a new project.
   - Enable billing (Cloud Run requires billing to be enabled).
   - Note your **Project ID** (you will use this throughout the assignment).

2. **Install Google Cloud SDK:**
   - Download and install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install).
   - Authenticate using:
     ```sh
     gcloud auth login
     ```
   - Set your project:
     ```sh
     gcloud config set project YOUR_PROJECT_ID
     ```

---

## **Step 2: Enable Required APIs**
In the Cloud Console, enable the following APIs:

```sh
gcloud services enable run.googleapis.com \
                         bigquery.googleapis.com \
                         cloudbuild.googleapis.com \
                         artifactregistry.googleapis.com
  ```

## **Step 3: Create a BigQuery Dataset and Table**
Before deploying your Cloud Run function, you need a dataset and a table in BigQuery.

1. **Open BigQuery Console:** [BigQuery](https://console.cloud.google.com/bigquery).
2. **Create a new dataset:**
   ```sh
   bq --location=US mk --dataset YOUR_PROJECT_ID:your_dataset
     ```
   
 ## **Step 4: Write Cloud Run Function**
   Now, create the application that queries BigQuery.

  
## **Step 5: Containerize the Application**
To deploy the application on Cloud Run, we need to package it as a container.

1. **Create a `Dockerfile` in your project directory:**
   ```dockerfile
   # Use an official Python runtime as a parent image
   FROM python:3.9-slim

   # Set the working directory in the container
   WORKDIR /app

   # Copy the current directory contents into the container at /app
   COPY . /app

   # Install required dependencies
   RUN pip install -r requirements.txt

   # Command to run the application
   CMD ["gunicorn", "-b", ":8080", "main:app"]

    ```
 ## **Step 6: Deploy to Cloud Run**
      Now that the application is containerized, we will deploy it to Cloud Run, making it accessible via a public URL.
   ###  Authenticate with Google Cloud
      Ensure you're authenticated with Google Cloud SDK and have set the correct project ID:
      ```sh
     gcloud auth login
     gcloud config set project YOUR_PROJECT_ID

## **Step 7: Automate Query Execution with Cloud Scheduler**
    To run the BigQuery query at scheduled intervals, we will use **Cloud Scheduler** to trigger the Cloud Run service.
 ### Enable Cloud Scheduler API
```sh
gcloud services enable cloudscheduler.googleapis.com
  ```

## **Step 8: Monitor and Debug the Cloud Run Service**
   Once the deployment is complete, it's important to monitor the Cloud Run service for performance, logs, and any potential errors.
 ###  View Cloud Run Logs
     To check logs for debugging and monitoring:
```sh
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=<YOUR_CLOUD_RUN_SERVICE>" --limit 100






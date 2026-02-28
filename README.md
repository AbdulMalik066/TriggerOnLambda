🚀 Calculator CI/CD Pipeline Project
📌 Project Overview

This project demonstrates a complete end-to-end CI/CD pipeline for a simple HTML Calculator application using:

Docker

GitHub Actions

DockerHub

AWS Lambda

Amazon SNS (Email/SMS Notifications)

Kubernetes (KillerKoda / EKS)

The pipeline automatically builds, pushes, deploys, and sends notifications whenever code is pushed to the main branch.

🏗 Architecture Flow
Developer Push
      ↓
GitHub Actions (CI/CD)
      ↓
Docker Image Build
      ↓
DockerHub Push
      ↓
AWS Lambda Trigger
      ↓
Amazon SNS
      ↓
Email / SMS Notification
      ↓
Kubernetes Pulls Latest Image
📂 Project Structure
calculator-ci-cd/
│
├── calculator.html
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── lambda/
│   └── lambda_function.py
└── README.md
🐳 Docker Setup
Dockerfile
FROM nginx:alpine
COPY calculator.html /usr/share/nginx/html/index.html
EXPOSE 80
Build Locally
docker build -t yourdockerhubusername/calculator:latest .
Push to DockerHub
docker push yourdockerhubusername/calculator:latest
☸ Kubernetes Deployment
deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: calculator-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: calculator
  template:
    metadata:
      labels:
        app: calculator
    spec:
      containers:
      - name: calculator-container
        image: yourdockerhubusername/calculator:latest
        imagePullPolicy: Always
        ports:
        - containerPort: 80
service.yaml
apiVersion: v1
kind: Service
metadata:
  name: calculator-service
spec:
  type: NodePort
  selector:
    app: calculator
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30007
Deploy
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
Access Application
kubectl port-forward service/calculator-service 8080:80

Open:

http://localhost:8080
🔄 GitHub Actions CI/CD Workflow

The workflow triggers on push to main.

Workflow Location
.github/workflows/ci-cd.yml
What It Does

Checkout code

Build Docker image

Login to DockerHub

Push image to DockerHub

Configure AWS credentials

Invoke Lambda function

Lambda sends SNS notification

🔔 AWS Lambda & SNS Notification Setup
📌 Overview

After successful Docker image push, GitHub Actions triggers AWS Lambda.
Lambda publishes a message to SNS, which sends Email/SMS notification.

1️⃣ Create SNS Topic

Go to AWS Console

Open SNS

Click Create Topic

Choose:

Type: Standard

Enter name:

calculator-notification

Create topic

Copy the Topic ARN

Example format:

arn:aws:sns:ap-south-1:123456789012:calculator-notification
2️⃣ Create Subscription

Open the SNS Topic

Click Create Subscription

Choose protocol:

Email

SMS

Enter:

Email address
OR

Phone number in format:

+919876543210

Confirm subscription (important)

Status must be:

Confirmed
3️⃣ Create AWS Lambda Function

Go to AWS Lambda

Create Function

Runtime: Python 3.x

Create function

4️⃣ Add Environment Variable

Go to:

Configuration → Environment Variables

Add:

Key: SNS_TOPIC_ARN
Value: <your-topic-arn>
5️⃣ Lambda Code

File: lambda/lambda_function.py

import boto3
import os

def lambda_handler(event, context):
    sns = boto3.client('sns')

    topic_arn = os.environ['SNS_TOPIC_ARN']

    sns.publish(
        TopicArn=topic_arn,
        Message='New Docker image built and pushed successfully!',
        Subject='CI/CD Notification'
    )

    return {"statusCode": 200}

Click Deploy after updating.

6️⃣ IAM Permission for Lambda

Lambda execution role must have:

sns:Publish

You can attach:

AmazonSNSFullAccess

OR custom policy:

{
  "Effect": "Allow",
  "Action": "sns:Publish",
  "Resource": "*"
}
🔐 GitHub Secrets Required

Add in:

GitHub → Repository → Settings → Secrets → Actions

DOCKER_USERNAME
DOCKER_PASSWORD
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
LAMBDA_FUNCTION_NAME
✅ End-to-End Execution

When developer pushes to main branch:

GitHub Actions starts pipeline

Docker image builds

Image pushes to DockerHub

Lambda function is invoked

SNS sends Email/SMS notification

Kubernetes pulls latest image (if imagePullPolicy: Always)

🎯 Key Features

✔ Automated Docker build & push
✔ Serverless AWS notification system
✔ Kubernetes deployment
✔ Image auto-pull with latest tag
✔ Secure credential handling via GitHub Secrets
✔ Production-style CI/CD architecture

📚 Skills Demonstrated

CI/CD Pipeline Design

Docker Containerization

Kubernetes Deployment

GitHub Actions Automation

AWS Lambda Integration

Amazon SNS Messaging

IAM Role Configuration

DevOps End-to-End Workflow

🚀 Future Improvements

Implement version tagging instead of latest

Use AWS EKS for production cluster

Add Helm charts

Add Terraform for Infrastructure as Code

Add monitoring (CloudWatch / Prometheus)

👨‍💻 Author

DevOps CI/CD Implementation Project
End-to-End Automation with Cloud & Kubernetes

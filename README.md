# Calculator CI/CD Pipeline Project

This project demonstrates a complete CI/CD pipeline using:

- Docker
- GitHub Actions
- AWS Lambda
- AWS SNS (SMS/Email Notification)
- DockerHub
- Kubernetes (KillerKoda / EKS)

## Workflow

1. Push code to GitHub
2. GitHub Actions builds Docker image
3. Image pushed to DockerHub
4. AWS Lambda triggered
5. SNS sends notification
6. Kubernetes pulls latest image automatically

## Tech Stack

- HTML
- Docker
- Kubernetes
- AWS Lambda
- SNS
- GitHub Actions

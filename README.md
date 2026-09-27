# Platform Engineer Technical Assignment

This repository contains my solution for the Platform Engineer technical assignment.

## Application

A small Python/FastAPI application deployed on AWS EC2 with:

- Nginx
- Gunicorn/Uvicorn
- PostgreSQL on Amazon RDS
- Application Load Balancer
- Terraform
- GitHub Actions
- CloudWatch
- AWS Secrets Manager

## Repository Structure

```text
app/                    Application source and tests
deployment/             Nginx, systemd and deployment scripts
terraform/              AWS infrastructure as code
.github/workflows/      CI/CD pipeline
architecture/           Architecture diagrams
docs/                   Technical documentation
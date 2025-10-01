# Foodly App - Docker Homework 2

A containerized Flask web application with PostgreSQL database demonstrating Docker fundamentals, volume management, and multi-service orchestration.

## What It Does

This project creates a simple "Hello World" Flask app that:
- Runs in a Docker container
- Logs every HTTP request to a persistent volume
- Uses PostgreSQL database for data storage
- Demonstrates Docker Compose multi-service setup

## Quick Start

```bash
# Start services
docker-compose up -d

# Access app
curl http://localhost:5000
# Response: "Hello from Foodly in Docker!"

# Stop services
docker-compose down
```

## Architecture

- **Web**: Flask app on port 5000
- **Database**: PostgreSQL on port 5432
- **Volumes**: `foodly_logs` (app logs), `db_data` (database)

## Files

```
├── app.py                # Flask app with request logging
├── Dockerfile           # Container configuration
├── docker-compose.yml   # Multi-service setup
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## Deliverables

### 📸 **Required Screenshots**

1. **Docker Images Output**


2. **Browser Verification**


3. **Log Persistence Demonstration**


4. **Docker Compose Services**


### 📝 **Technical Questions & Answers**

#### **Q: What's the difference between a container and an image?**
**A:** 


#### **Q: Why do we use a named volume instead of writing directly inside the container?**
**A:**


#### **Q: In your Dockerfile, what does WORKDIR do?**
**A:**


#### **Q: What does `docker-compose down -v` do compared to `docker-compose 
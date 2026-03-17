# DevOps Community Forum Analyzer

## Overview

DevOps Community Forum Analyzer is a data-driven analytics system that collects live DevOps discussions from Stack Overflow, processes engagement metrics, and presents topic-wise insights through a multi-page web dashboard.

The project demonstrates a complete engineering pipeline involving data ingestion, analytics computation, dashboard visualization, containerization, CI automation, and deployment readiness.

---

## Problem Statement

DevOps discussions across technical communities contain valuable information about trending tools, unresolved problems, and engagement patterns.

The objective of this project is to:

* identify trending DevOps topics
* measure engagement across technical discussions
* compare major DevOps domains such as CI/CD, Containers, Cloud, and Automation
* provide a deployable analytics dashboard

---

## System Architecture

Stack Overflow API
↓
fetch_data.py
↓
questions.json
↓
analyze.py
↓
analysis.json
↓
Flask Dashboard
↓
Docker Deployment

CI validation runs separately through GitHub Actions.

---

## Features

### Data Collection

* Fetches DevOps-tagged questions from Stack Overflow using Stack Exchange API
* Extracts metadata such as score, answer count, views, accepted answers, and tags

### Analytics Engine

Global engagement metrics:

* average score
* average answer count
* resolved percentage
* average views
* accepted resolution rate
* dominant category
* most viewed question

Topic-wise analytics:

* CI/CD
* Containers
* Cloud
* Automation

Each topic computes:

* average score
* average answer count
* resolved percentage
* average views
* accepted resolution rate

### Dashboard

* Overview page with KPI cards and tag distribution
* Topic Analytics page with per-topic metric cards and comparative charts
* Manual refresh support for triggering a fresh analytics cycle

### DevOps Implementation

* Dockerized deployment
* GitHub Actions CI pipeline
* Unit testing support
* Artifact generation in CI

---

## Tech Stack

* Python
* Flask
* Chart.js
* Docker
* GitHub Actions
* Stack Exchange API

---

## Project Structure

devops-forum-analyzer/
│
├── scraper/
│   └── fetch_data.py
│
├── analyzer/
│   └── analyze.py
│
├── dashboard/
│   └── app.py
│
├── templates/
│   ├── index.html
│   └── topics.html
│
├── static/
│   ├── style.css
│   ├── topics.css
│   ├── charts.js
│   └── topics_chart.js
│
├── data/
│   ├── questions.json
│   └── analysis.json
│
├── tests/
│   └── test_analyze.py
│
├── Dockerfile
├── requirements.txt
├── pipeline.py
├── docker-compose.yml
└── .github/workflows/ci.yml

---

## Prerequisites

Before running the project, ensure the following are installed:

* Python 3.11 or above
* Docker Desktop (if running containerized version)
* Git

---

## Clone Repository

```bash
git clone <repository-url>
cd devops-forum-analyzer
```

Replace `<repository-url>` with the repository link.

---

## Running Locally (Recommended for Development)

### Step 1: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run analytics pipeline

```bash
python pipeline.py
```

This fetches fresh data from Stack Overflow and generates:

* data/questions.json
* data/analysis.json

### Step 3: Start dashboard

```bash
python dashboard/app.py
```

### Step 4: Open browser

```text
http://127.0.0.1:5000
```

---

## Running with Docker (Recommended for Machine-Independent Execution)

### Step 1: Build Docker image

Run from project root (folder containing Dockerfile):

```bash
docker build -t forum-analyzer .
```

### Step 2: Run container

```bash
docker run -p 5000:5000 forum-analyzer
```

### Step 3: Open browser

```text
http://127.0.0.1:5000
```

---

## Running an Existing Docker Image Again

If image is already built:

```bash
docker run -p 5000:5000 forum-analyzer
```

---

## Manual Refresh Inside Dashboard

The dashboard includes a manual refresh option.

When triggered, it:

* fetches latest Stack Overflow data
* recomputes analytics
* updates JSON outputs
* reloads dashboard metrics

---

## Running Unit Tests

```bash
pytest
```

Expected result:

```text
1 passed
```

---

## CI Pipeline

GitHub Actions automatically performs:

* dependency installation
* unit testing
* analytics pipeline execution
* artifact generation

Generated artifact:

* analysis.json

---

## Troubleshooting

### Docker build error: Dockerfile not found

Ensure terminal is inside project root:

```bash
cd devops-forum-analyzer
```

### Flask import issue

Run dashboard only through:

```bash
python dashboard/app.py
```

### Port already in use

Stop previous process or container using port 5000.

---

## Future Scope

* Add Reddit and Dev.to as additional community sources
* Deploy on cloud platform
* Add historical trend tracking
* Introduce alerting for emerging DevOps topics

---

## Author

Pratham Mishra

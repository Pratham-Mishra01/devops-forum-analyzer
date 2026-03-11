# DevOps Community Forum Analyzer

## Overview

DevOps Community Forum Analyzer is a data-driven analytics system that collects live DevOps discussions from Stack Overflow, processes engagement metrics, and presents topic-wise insights through a multi-page web dashboard.

The project demonstrates a complete engineering pipeline involving data ingestion, analytics computation, dashboard visualization, containerization, and CI automation.

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
* Extracts relevant metadata such as score, answer count, views, and tags

### Analytics Engine

* Global engagement metrics:

  * average score
  * average answer count
  * resolved percentage
  * average views
  * accepted resolution rate

* Topic-wise analytics:

  * CI/CD
  * Containers
  * Cloud
  * Automation

### Dashboard

* Overview page with KPI cards and tag distribution
* Topic Analytics page with per-topic metrics and comparative charts

### DevOps Implementation

* Dockerized deployment
* GitHub Actions CI pipeline
* Unit testing support
* Docker image build verification

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
└── .github/workflows/ci.yml

---

## Installation

Clone repository:

git clone <repository-url>

Move into project folder:

cd devops-forum-analyzer

Install dependencies:

pip install -r requirements.txt

---

## Running Locally

Run pipeline:

python pipeline.py

Start dashboard:

python dashboard/app.py

Open browser:

http://127.0.0.1:5000

---

## Docker Deployment

Build image:

docker build -t forum-analyzer .

Run container:

docker run -p 5000:5000 forum-analyzer

---

## CI Pipeline

GitHub Actions automatically performs:

* dependency installation
* unit testing
* analytics pipeline execution
* Docker build verification

---

## Future Scope

* Add Reddit and Dev.to as additional community sources
* Deploy on cloud platform
* Add historical trend tracking
* Introduce alerting for emerging DevOps topics

---

## Author

Pratham Mishra

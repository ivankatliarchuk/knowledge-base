---
title: assessing migration readiness
summary: product readiness coordination checklist
authors: ["ivan k"]
tags: ["checklist", "architecture", "checklist", "migration", "heatmap", "example"]
date: 2021-03-21
source: https://docs.aws.amazon.com/whitepapers/latest/aws-migration-whitepaper/assessing-migration-readiness.html
published: true
---

## Migration Readiness Assessment Heatmap (example)

| Icon       |      Description         |
|:----------:|:-------------------------|
| ℹ️         | Assement to be completed |
| 🟨         | Warning                  |
| ✅         | Green                    |
|❗          |  Red                     |

### 🟨  Business Case

- ✅	Key Stakeholder Sign-off
- 🟨  High Level Business Case
- 🟨  Migration Funding Commitment
- 🟨  Specific Migration Workloads Committed
- 🟨  Detailed Business Case

### ✅ Landing Zone

- ✅	AWS Master Account/Sub-Accounts
- ✅	Existing Network & Data Center Architecture
- 🟨	Account Design & Configuration

### 🟨 Operating Model

- ✅	Current Operational Model
- ✅	Asset Management
- ✅	Service Catalog
- 🟨 Future Requirements
- 🟨 AMI/Patching
- 🟨 Backup
- 🟨 Config Management & Change Management
- 🟨 Cost Management
- 🟨 CI/CD Pipelines
- ❗	Managed Service Provider Identified
- ❗	BCP/DR
- ❗	Cloud Ready Operational Processes & Run Books

### 🟨  Customer Migration Project Plan

- 🟨 Determine Delivery Model & Approach
- 🟨 Project Management Capability
- ❗	Migration Plan

### 🟨  Customer Migration Project Plan

- 🟨 Server & Infrastructure Discovery Data
- 🟨 Workload Owner Buy-In or Aligment
- ❗	Application Discovery Data
- ❗	Migration Scope Scored & Targeted for Optimisation

### 🟨  Security & Compliance

- ✅	3rd Party Risk
- ✅	Identity &Access Management
- ✅	Infrastructure Security
- ✅	Data Protection
- ✅	Compliance Design
- 🟨 Shared Responsiblity Model Understood
- 🟨 [Security RACI](https://loopio.com/blog/raci-chart-security-questionnaires/)
- 🟨 Security Cartography
- 🟨 Cloud Security Readiness Tested
- 🟨 Logging & Monitoring
- ❗	Incident Response

### 🟨  Skills & COE

- ✅	Single Threaded Leader
- ✅	Design or Evolve COE
- 🟨 COE Resource Commitment
-❗ Expirience Baseline
-❗ Organisational Training

### ❗  Migration Process & Experience

- 🟨 Migration Experience
- ❗	Identification of Pilot Applications

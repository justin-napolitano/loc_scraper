---
slug: github-loc-scraper
id: github-loc-scraper
title: Python-based US Supreme Court Case Data Scraper
repo: justin-napolitano/loc_scraper
githubUrl: https://github.com/justin-napolitano/loc_scraper
generatedAt: '2025-11-24T21:35:31.540Z'
source: github-auto
summary: >-
  A Python scraper for extracting US Supreme Court case data from the Library of Congress, utilizing
  Google Cloud Platform for scalable execution.
tags:
  - python
  - docker
  - beautifulsoup
  - gcloud
seoPrimaryKeyword: us supreme court case data scraper
seoSecondaryKeywords:
  - python web scraper
  - google cloud storage
  - docker deployment
  - cloud run jobs
  - library of congress api
  - data processing pipelines
seoOptimized: true
topicFamily: datascience
topicFamilyConfidence: 0.9
kind: project
entryLayout: project
showInProjects: true
showInNotes: false
showInWriting: false
showInLogs: false
---

A Python-based scraper designed to extract US Supreme Court case data from the Library of Congress digital collections. The project integrates with Google Cloud Platform (GCP) to run scraping jobs as scalable Cloud Run jobs, storing results in GCP buckets for downstream processing.

---

## Features

- Scrapes US Supreme Court case metadata from the Library of Congress public API.
- Converts search results into JSON format.
- Uploads scraped data to Google Cloud Storage buckets.
- Designed as GCP Cloud Run jobs for scalable, cloud-native execution.
- Includes scripts for building Docker images, deploying jobs, and managing workflows.

## Tech Stack

- Python 3
- Google Cloud Platform (Cloud Run, Cloud Storage, Cloud Build)
- Docker
- Bash scripting
- BeautifulSoup for HTML parsing

## Getting Started

### Prerequisites

- Google Cloud account with billing enabled
- Installed and configured [gcloud CLI](https://cloud.google.com/sdk/docs/install)
- Docker installed locally

### Installation

1. Clone the repository:

```bash
git clone https://github.com/justin-napolitano/loc_scraper.git
cd loc_scraper
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

### Build and Deploy

1. Build the Docker image using Cloud Build:

```bash
gcloud builds submit --config cloudbuild.yaml .
```

2. Deploy the scraping job to Cloud Run:

```bash
./deploy.sh
```

### Running the Job

Trigger the Cloud Run job manually or via scheduler to start scraping.

## Project Structure

```
loc_scraper/
├── build.sh              # Build script
├── cloudbuild.yaml       # Cloud Build configuration
├── deploy.sh             # Deployment script for Cloud Run job
├── Dockerfile            # Docker image specification
├── execute_job.sh        # Script to execute the scraping job
├── job_create.sh         # Script to create GCP job
├── logs/                 # Log files directory
├── output_2/             # Sample output JSON files from scraping
├── post-image.jpeg       # Featured image for documentation
├── quickstart/           # Quickstart instructions and scripts
├── readme.md             # Project README
├── requirements.txt      # Python dependencies
├── requirements_cloud.txt# Cloud-specific dependencies
├── run.sh                # Run script
└── src/                  # Source code
    ├── loc_scraper.py    # Main scraper implementation
    ├── loc_pdf_downloader.py # PDF downloader utility
    └── steps.md          # Setup and development steps
```

## Future Work / Roadmap

- Complete integration with chatbot APIs for enhanced data analysis.
- Expand scraping to include more collections or metadata fields.
- Implement automated scheduling and monitoring of scraping jobs.
- Add data processing pipelines to build research tools from scraped data.
- Improve error handling and logging for robustness.

---

For more details, see the `index.md` and `readme.md` files in the repo for background and usage notes.



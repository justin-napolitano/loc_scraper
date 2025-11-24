---
slug: github-loc-scraper-note-technical-overview
id: github-loc-scraper-note-technical-overview
title: loc_scraper Overview
repo: justin-napolitano/loc_scraper
githubUrl: https://github.com/justin-napolitano/loc_scraper
generatedAt: '2025-11-24T18:40:51.708Z'
source: github-auto
summary: >-
  The **loc_scraper** is a Python tool that extracts US Supreme Court case data
  from the Library of Congress. It runs on Google Cloud Platform (GCP),
  utilizing Cloud Run for scalable scraping jobs and storing results in GCP
  buckets.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

The **loc_scraper** is a Python tool that extracts US Supreme Court case data from the Library of Congress. It runs on Google Cloud Platform (GCP), utilizing Cloud Run for scalable scraping jobs and storing results in GCP buckets.

### Key Features

- Scrapes case metadata from the Library of Congress API.
- Outputs data in JSON format.
- Constructs cloud-native jobs.
  
### Tech Stack

- Python 3
- GCP (Cloud Run, Cloud Storage)
- Docker
- BeautifulSoup for HTML parsing

### Quick Start

1. Clone the repo:

    ```bash
    git clone https://github.com/justin-napolitano/loc_scraper.git
    cd loc_scraper
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Build the Docker image:

    ```bash
    gcloud builds submit --config cloudbuild.yaml .
    ```

4. Deploy the job:

    ```bash
    ./deploy.sh
    ```

### Gotchas

Make sure your Google Cloud account is set up with billing enabled. Check that you have the `gcloud CLI` and Docker installed before starting.

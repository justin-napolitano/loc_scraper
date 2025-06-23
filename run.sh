#!/bin/bash

# Navigate to the directory of this script (important for cron)
cd "$(dirname "$0")"

# Create a logs folder if it doesn't exist
mkdir -p logs

# Get a timestamp
timestamp=$(date +%Y%m%d_%H%M%S)

# Build the Docker image (optional: remove if built already)
docker build -t loc-scraper . >> logs/build_$timestamp.log 2>&1

# Run the container and log output
docker run \
  -v $(pwd)/src/output:/app/src/output \
  loc-scraper "$@" >> logs/run_$timestamp.log 2>&1

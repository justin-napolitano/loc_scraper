FROM python:3.11-slim

# Create working directory
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy your source code
COPY src/ ./src/

# Default to src directory
WORKDIR /app/src

# Ensure output dir exists inside the container
RUN mkdir -p /app/src/output

# Default command (can override at runtime)
ENTRYPOINT ["python", "loc_local.py"]

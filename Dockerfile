# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script and dependencies
COPY cronjob-script.py /app/
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default environment variables
ENV JOB_NAME="default-job" \
    VERSION="v1" \
    INTERVAL_MINUTES=5

# Command to run the script
CMD ["python", "cron_task.py"]

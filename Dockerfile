FROM python:3.10-slim

WORKDIR /app

# Copy requirements.txt first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code
COPY code/ ./code/

# Environment variables
ENV COMPUTE_SERVICE_LOG_LEVEL=INFO
ENV COMPUTE_SERVICE_ENABLE_BATCH_PROCESSING=True
ENV COMPUTE_SERVICE_MAX_BATCH_SIZE=1000

# Expose the port
EXPOSE 5000

# Run the service
CMD ["python", "code/service_api.py"] 
# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy dependency file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create necessary directories and set up a non-root user for security
RUN mkdir -p data results config \
    && groupadd -r jules && useradd -r -g jules -d /app jules \
    && chown -R jules:jules /app

# Switch to the non-root user
USER jules

# Copy the rest of the application code
COPY --chown=jules:jules . .

# Run run_system.py in loop mode for production by default
CMD ["python", "run_system.py", "--loop"]

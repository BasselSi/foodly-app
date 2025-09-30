# Use Python 3.10 slim as the base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Create logs directory
RUN mkdir -p /app/logs

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port (change if your app uses a different port)
EXPOSE 5000

# Run the application (change app.py to your main file if needed)
CMD ["python", "app.py"]
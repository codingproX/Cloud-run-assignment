# Use official Python runtime as base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Run Flask app
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]

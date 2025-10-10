# Use an appropriate Python base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements first (for better Docker layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files to container
COPY . .

# Expose the Flask application port
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Run the Flask application
# Use 0.0.0.0 to make it accessible from outside the container
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]


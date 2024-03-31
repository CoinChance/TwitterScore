# Use the official Python base image
FROM python:3.12.2-slim

# Set the working directory in the container
WORKDIR /app

# Copy the required files into the container
COPY requirements.txt .
COPY app.py .
COPY twitter_helper.py .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Define the command to run your Flask application
CMD ["python", "app.py" ]

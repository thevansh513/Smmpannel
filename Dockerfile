# Base image: lightweight Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose port (Railway sets $PORT)
EXPOSE 5000

# Run app
CMD ["python", "app.py"]

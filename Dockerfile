FROM ubuntu:latest
LABEL authors="bexruz"

# Base image
FROM python:3.12-slim

# Working directory
WORKDIR /project

# Dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose the application port
EXPOSE 8000

# Command to run FastAPI app
CMD ["uvicorn", "project.main:app", "--host", "0.0.0.0", "--port", "8000"]


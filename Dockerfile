# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Ensure the project directory is correctly detected
RUN ls /app

# Expose port 8000 for Django
EXPOSE 8000

# Start the Django application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]

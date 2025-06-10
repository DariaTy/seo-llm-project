# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available for the container (if running a web service, e.g., API)
EXPOSE 5000

# Run the application
CMD ["python", "./your_main_script.py"]

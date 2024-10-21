# Dockerfile

# Use Python base image
#FROM python:3.9

# Set the working directory
#WORKDIR /app

# Copy requirements file
#COPY requirements.txt .

# Install dependencies
#RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
#COPY . .

# Set the command to run the application
#CMD ["python", "src/main.py"]


#---------------------------------

# Use Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the working directory
COPY . .

# Set the command to run the application
CMD ["python", "-m", "src.main"]


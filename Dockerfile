# Use an official Python runtime as a parent image
FROM python:3.12.4-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY Pipfile Pipfile.lock ./

# Install any needed packages specified in Pipfile
RUN pip install pipenv && pipenv install --system

# Copy the rest of the application code into the container
COPY . .

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
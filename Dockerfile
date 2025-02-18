# Use an official Python runtime as a parent image
FROM ubuntu

# Set the working directory in the container
WORKDIR /app

RUN apt update -y && apt install pip -y && apt install postgresql-client -y
RUN apt install python3.12-venv -y

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install dependencies
#RUN pip install --upgrade pip && pip install -r requirements.txt
RUN python3 -m venv venv && \
    venv/bin/pip install --no-cache-dir --upgrade pip && \
    venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /app/

# Expose the port Flask is running on
EXPOSE 5000

# Command to run the application
#CMD ["python", "app.py"]
# Use the virtual environment for running the app
CMD ["venv/bin/python", "app.py"]

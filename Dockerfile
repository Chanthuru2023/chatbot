FROM mcr.microsoft.com/vscode/devcontainers/python:3.10

# Install any additional packages you need here
RUN pip install --upgrade pip
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# Set the working directory in the container
WORKDIR /workspace

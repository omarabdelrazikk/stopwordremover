# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the local directory's contents into the container at /usr/src/app
COPY . .

# Install spacy
RUN pip install spacy && \
    python -m spacy download en_core_web_sm

CMD ["python", "spacyyy.py"]

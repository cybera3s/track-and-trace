FROM python:3.10.9-bullseye

# Add meta data
LABEL maintainer="Ario"
LABEL email="cybera.3s@gmail.com"

# Get as much information from your running application
ENV PYTHONUNBUFFERED 1

# Set and create workdir
WORKDIR /app

# Install dependencies
ADD requirements.txt .
RUN pip install -r requirements.txt

# Copy project
ADD . .

# Create and assign user
RUN adduser app
USER app

# copy entrypoint.sh
COPY ./entrypoint.sh .

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
FROM python:3.10

LABEL Maintainer="callumjfortune"

# Install necessary dependencies
RUN apt-get update -y && apt-get install -y \
    libgl1-mesa-glx \
    build-essential \
    libffi-dev \
    openssl \
    libssl-dev \
    python3 \
    python3-pip

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/app/src

COPY ["main.py", "util.py", "requirements.txt", "./"]
COPY ["models/license_plate.pt", "./models/"]
COPY ["samples/sample.mp4", "./samples/"]

# Upgrade pip and install Python packages
RUN python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt

# CMD ["python3", "main.py"]
CMD ["python3", "main.py"]

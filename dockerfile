FROM python:3.11

LABEL Maintainer = "callumjfortune"

WORKDIR /usr/app/src

COPY ["main.py", "util.py", "requirements.txt", "./"]
COPY ["models/license_plate.pt", "./models/"]
COPY ["samples/sample.mp4", "./samples/"]


RUN apt-get update -y && apt-get install libgl1 -y

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]

FROM python:3.13-slim


RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && apt-get clean


COPY requirements.txt /app/requirements.txt
RUN pip3 install --upgrade pip && pip install -r /app/requirements.txt


COPY . /app


WORKDIR /app


ENTRYPOINT ["pytest"]


CMD ["--browser", "chrome"]

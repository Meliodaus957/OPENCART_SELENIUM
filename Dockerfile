FROM ubuntu:20.04

# Создаем рабочую папку и копируем файлы
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    netcat-traditional \
    python3 \
    python3-pip \
    && apt-get clean


# Копируем код и скрипт ожидания
COPY . /app
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Запускаем wait-for-it и pytest после того, как OpenCart будет доступен
ENTRYPOINT ["/app/wait-for-it.sh"]
FROM ubuntu:20.04

# Создаем рабочую папку и копируем файлы
WORKDIR /app
COPY requirements.txt /app
COPY tests /app
COPY pytest.ini /app



# Устанавливаем зависимости
RUN apt-get update && apt-get install -y default-jre wget vim jq python3-venv


# Копируем код и скрипт ожидания
COPY . /app
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh


RUN python3 -m venv venv
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

# Запускаем wait-for-it и pytest после того, как OpenCart будет доступен
ENTRYPOINT ["/app/wait-for-it.sh"]
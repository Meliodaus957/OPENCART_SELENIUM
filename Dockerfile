FROM ubuntu:20.04


# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    default-jre \
    wget \
    vim \
    jq \
    python3-venv \
    python3-pip

# Создаем рабочую папку и копируем файлы
WORKDIR /app
COPY requirements.txt /app
COPY tests /app
COPY pytest.ini /app

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y default-jre wget vim jq python3-venv python3-pip

# Копируем код и скрипт ожидания
COPY . /app
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Создаем виртуальное окружение и устанавливаем зависимости
RUN python3 -m venv /app/venv

# Обновляем pip внутри виртуального окружения и устанавливаем зависимости
RUN /app/venv/bin/pip3 install --upgrade pip
RUN /app/venv/bin/pip3 install -r requirements.txt

# Запускаем wait-for-it и pytest после того, как OpenCart будет доступен
ENTRYPOINT ["/app/wait-for-it.sh"]

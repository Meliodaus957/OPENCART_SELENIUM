FROM python:3.13-slim

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    netcat-traditional \
    && apt-get clean

# Создаем рабочую папку и копируем файлы
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем код и скрипт ожидания
COPY . /app
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Запускаем wait-for-it и pytest после того, как OpenCart будет доступен
ENTRYPOINT ["/app/wait-for-it.sh", "opencart:8080", "--"]

# Команда, которая будет выполнена после того, как wait-for-it.sh завершит ожидание
CMD ["pytest", "-v", "tests/test_opencart.py", "--base_url=http://opencart:8080", "--browser=chrome", "--bv=latest", "--executor=selenoid"]
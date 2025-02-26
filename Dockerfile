FROM jenkins/jenkins:lts

USER root

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Создаем рабочую папку и копируем файлы
WORKDIR /app
COPY requirements.txt /app
COPY tests /app
COPY pytest.ini /app
COPY . /app
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Создаем виртуальное окружение и устанавливаем зависимости
RUN python3 -m venv /app/venv

# Обновляем pip внутри виртуального окружения и устанавливаем зависимости
RUN /app/venv/bin/pip install --upgrade pip
RUN /app/venv/bin/pip install -r requirements.txt

USER jenkins

# Запускаем wait-for-it и pytest после того, как OpenCart будет доступен
ENTRYPOINT ["/app/wait-for-it.sh"]

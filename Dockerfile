FROM jenkins/jenkins:lts-jdk17

USER root

# Устанавливаем зависимости
RUN apt update
RUN apt install -y python3
RUN python3 --version
RUN apt install -y python3-pip
RUN apt install -y python3-venv


# Создаем рабочую папку и копируем файлы
WORKDIR /app
COPY requirements.txt /app
COPY tests /app
COPY pytest.ini /app
COPY . /app
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh



# Обновляем pip внутри виртуального окружения и устанавливаем зависимости
RUN pip install --upgrade pip --break-system-packages
RUN pip install -r requirements.txt --break-system-packages


USER jenkins

# Запускаем wait-for-it и pytest после того, как OpenCart будет доступен
ENTRYPOINT ["/app/wait-for-it.sh"]

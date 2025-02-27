FROM jenkins/jenkins:lts-jdk17

USER root

# Устанавливаем зависимости
RUN apt update && apt install -y python3 python3-pip python3-venv

# Создаем рабочую папку и копируем файлы
WORKDIR /app
COPY requirements.txt /app
COPY tests /app
COPY pytest.ini /app
COPY . /app
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Создаем виртуальное окружение и устанавливаем зависимости
RUN python3 -m venv venv
RUN source venv/bin/activate

# Обновляем pip внутри виртуального окружения и устанавливаем зависимости
RUN pip3 install --upgrade pip
RUN pip3 install --break-system-packages -r requirements.txt


USER jenkins

# Запускаем wait-for-it и pytest после того, как OpenCart будет доступен
ENTRYPOINT ["/app/wait-for-it.sh"]

# FROM jenkins/jenkins:lts-jdk17
#
# USER root
#
# # Устанавливаем зависимости
# RUN apt update
# RUN apt install -y python3
# RUN python3 --version
# RUN apt install -y python3-pip
# RUN apt install -y python3-venv
#
#
# # Создаем рабочую папку и копируем файлы
# WORKDIR /app
# COPY requirements.txt /app
# COPY . /app
#
#
#
#
# # Обновляем pip внутри виртуального окружения и устанавливаем зависимости
# RUN pip install --upgrade pip --break-system-packages
# RUN pip install -r requirements.txt --break-system-packages
#
#
# USER jenkins
#
#

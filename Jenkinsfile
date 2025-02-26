pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Meliodaus957/OPENCART_SELENIUM'
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    // Строим Docker-образы через Docker Compose
                    sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} build'
                }
            }
        }

        stage('Start Services') {
            steps {
                script {
                    // Поднимаем сервисы через Docker Compose
                    sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} up -d'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Запуск тестов через Docker Compose, как указано в конфигурации
                    sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} run --rm tests'
                }
            }
        }

        stage('Stop Services') {
            steps {
                script {
                    // Останавливаем все сервисы после завершения тестов
                    sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} down'
                }
            }
        }
    }

    post {
        always {
            // Очистка после выполнения
            cleanWs()
        }
    }
}
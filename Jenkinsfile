pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
        OPENCART_URL = "http://opencart:8080"
        SELENOID_URL = "selenoid:4444/wd/hub"
        BROWSER = "chrome"
        BROWSER_VERSION = "latest"
        THREADS = "2"
        SELENOID_IMAGE = 'selenoid/selenoid:latest'
        NETWORK_NAME = 'selenoid'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Meliodaus957/OPENCART_SELENIUM'
            }
        }

        stage('Start Selenoid') {
            steps {
                script {
                    // Запуск контейнера Selenoid в сети selenoid
                    sh '''
                        docker run -d --name selenoid --network $NETWORK_NAME \
                        -p 4444:4444 \
                        aerokube/selenoid:latest
                    '''
                }
            }
        }

        stage('Start Docker Compose') {
            steps {
                script {
                    // Поднимаем контейнеры с помощью docker-compose
                    sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} up -d'
                }
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Устанавливаем python3-venv и pip в контейнере
                    sh 'apt-get update'
                    sh 'apt-get install -y python3-pip python3-venv'

                    // Создаем виртуальное окружение
                    sh 'python3 -m venv venv'

                    // Активируем виртуальное окружение и устанавливаем зависимости из requirements.txt
                    sh '. venv/bin/activate && pip install --upgrade pip'
                    sh '. venv/bin/activate && pip install -r requirements.txt'

                    // Проверяем, где находится pytest
                    sh '. venv/bin/activate && which pytest'
                    sh '. venv/bin/activate && pytest --version'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '''
                    . venv/bin/activate
                    pytest -v tests/test_opencart.py --alluredir=allure-results \
                        --base_url=${OPENCART_URL} --browser=${BROWSER} \
                        --bv=${BROWSER_VERSION} --executor=${SELENOID_URL}
                    '''
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    sh 'allure generate allure-results --clean -o allure-report'
                    sh 'allure open allure-report'
                }
            }
        }
    }

    post {
        always {
            script {
                sh 'docker-compose -f ${DOCKER_COMPOSE_FILE} down'
            }
        }
    }
}
